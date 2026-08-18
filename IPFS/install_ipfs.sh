#!/usr/bin/env bash

# Script para instalar y configurar un nodo IPFS (Kubo) Privado y Seguro en Ubuntu (DigitalOcean)
# Diseñado para entornos que manejan información altamente confidencial.

set -euo pipefail

# Colores para salida
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # Sin color

echo -e "${GREEN}=== Iniciando Instalación de IPFS Privado y Seguro ===${NC}"

# 1. Verificar que se ejecuta como root
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}Error: Este script debe ejecutarse como root (usa sudo).${NC}"
  exit 1
fi

# 2. Instalar dependencias necesarias
echo -e "${YELLOW}[1/8] Instalando dependencias necesarias (curl, tar, wget)...${NC}"
apt-get update -y && apt-get install -y curl tar wget

# 3. Obtener la última versión estable de Kubo (IPFS)
echo -e "${YELLOW}[2/8] Obteniendo la última versión de Kubo (IPFS)...${NC}"
LATEST_VERSION=$(curl -s https://dist.ipfs.tech/kubo/versions | tail -n 1)
if [ -z "$LATEST_VERSION" ]; then
  LATEST_VERSION="v0.32.0" # Versión de respaldo por seguridad
  echo -e "${YELLOW}No se pudo auto-detectar la versión, usando la versión por defecto: ${LATEST_VERSION}${NC}"
else
  echo -e "${GREEN}Última versión detectada: ${LATEST_VERSION}${NC}"
fi

# Descargar
ARCH="linux-amd64"
DOWNLOAD_URL="https://dist.ipfs.tech/kubo/${LATEST_VERSION}/kubo_${LATEST_VERSION}_${ARCH}.tar.gz"
echo -e "Descargando desde: ${DOWNLOAD_URL}"
wget -q --show-progress "$DOWNLOAD_URL" -O kubo.tar.gz

# Extraer e Instalar
tar -xf kubo.tar.gz
cd kubo
bash install.sh
cd ..
rm -rf kubo kubo.tar.gz
echo -e "${GREEN}Kubo instalado correctamente. Versión: $(ipfs --version)${NC}"

# 4. Crear usuario y grupo de sistema para IPFS (Seguridad)
echo -e "${YELLOW}[3/8] Creando usuario de sistema 'ipfs'...${NC}"
if ! id -u ipfs >/dev/null 2>&1; then
  useradd -r -m -d /var/lib/ipfs -s /usr/sbin/nologin ipfs
  echo -e "${GREEN}Usuario 'ipfs' creado.${NC}"
else
  echo -e "${GREEN}El usuario 'ipfs' ya existe.${NC}"
fi

# Directorio de trabajo
IPFS_PATH="/var/lib/ipfs"
mkdir -p "$IPFS_PATH"
chown -R ipfs:ipfs "$IPFS_PATH"

# 5. Inicializar el repositorio de IPFS bajo el perfil de servidor
echo -e "${YELLOW}[4/8] Inicializando repositorio IPFS con perfil 'server'...${NC}"
if [ ! -f "$IPFS_PATH/config" ]; then
  sudo -u ipfs env IPFS_PATH="$IPFS_PATH" ipfs init --profile server
  echo -e "${GREEN}Repositorio IPFS inicializado.${NC}"
else
  echo -e "${YELLOW}El repositorio ya estaba inicializado. Saltando paso.${NC}"
fi

# 6. Configurar IPFS como Red Privada (Private Swarm)
echo -e "${YELLOW}[5/8] Configurando Red Privada y eliminando nodos bootstrap públicos...${NC}"

# Generar Clave de Enjambre (Swarm Key)
SWARM_KEY_PATH="$IPFS_PATH/swarm.key"
if [ ! -f "$SWARM_KEY_PATH" ]; then
  # Generar una clave de 32 bytes en formato hex (64 caracteres) usando openssl para evitar problemas de pipefail
  HEX_KEY=$(openssl rand -hex 32)
  echo -e "/key/swarm/psk/1.0.0/\n/base16/\n${HEX_KEY}" > "$SWARM_KEY_PATH"
  chmod 400 "$SWARM_KEY_PATH"
  chown ipfs:ipfs "$SWARM_KEY_PATH"
  echo -e "${GREEN}Clave Swarm privada generada y guardada en ${SWARM_KEY_PATH}${NC}"
else
  echo -e "${YELLOW}Ya existe una clave Swarm en ${SWARM_KEY_PATH}. Se mantendrá la actual.${NC}"
fi

# Eliminar todos los bootstrap públicos
sudo -u ipfs env IPFS_PATH="$IPFS_PATH" ipfs bootstrap rm --all
echo -e "${GREEN}Nodos de bootstrap públicos eliminados. Tu nodo ahora está aislado.${NC}"

# Configurar que el API y el Gateway solo escuchen en Localhost (127.0.0.1)
# Esto evita que cualquier puerto quede expuesto públicamente en DigitalOcean.
sudo -u ipfs env IPFS_PATH="$IPFS_PATH" ipfs config Addresses.API "/ip4/127.0.0.1/tcp/5001"
sudo -u ipfs env IPFS_PATH="$IPFS_PATH" ipfs config Addresses.Gateway "/ip4/127.0.0.1/tcp/8081"
# Deshabilitar AutoConf ya que interfiere con el modo de red privada forzada
sudo -u ipfs env IPFS_PATH="$IPFS_PATH" ipfs config --json AutoConf.Enabled false
echo -e "${GREEN}Direcciones API, Gateway (puerto 8081) y AutoConf configurados correctamente.${NC}"

# 7. Crear el servicio de Systemd para IPFS
echo -e "${YELLOW}[6/8] Creando servicio systemd para IPFS...${NC}"
SERVICE_FILE="/etc/systemd/system/ipfs.service"

cat <<EOF > "$SERVICE_FILE"
[Unit]
Description=IPFS Daemon (Private Network)
After=network.target

[Service]
Type=simple
User=ipfs
Group=ipfs
Environment="IPFS_PATH=$IPFS_PATH"
# Forzar a que falle si no encuentra la clave swarm.key (protección contra conexiones accidentales a red pública)
Environment="LIBP2P_FORCE_PNET=1"
ExecStart=/usr/local/bin/ipfs daemon --migrate=true
Restart=on-failure
KillSignal=SIGINT

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable ipfs
echo -e "${GREEN}Servicio ipfs.service configurado y habilitado para inicio automático.${NC}"

# 8. Iniciar el servicio
echo -e "${YELLOW}[7/8] Iniciando servicio IPFS...${NC}"
systemctl restart ipfs

# Esperar unos segundos a que levante
sleep 3
if systemctl is-active --quiet ipfs; then
  echo -e "${GREEN}¡IPFS está activo y ejecutándose en modo privado!${NC}"
else
  echo -e "${RED}Error: El servicio IPFS no pudo iniciarse correctamente. Revisa 'journalctl -u ipfs'${NC}"
  exit 1
fi

# Obtener la identidad del nodo (Peer ID)
PEER_ID=$(sudo -u ipfs env IPFS_PATH="$IPFS_PATH" ipfs id -f "<id>")

# 9. Mostrar información de conexión importante
echo -e "${GREEN}=== INSTALACIÓN COMPLETADA ===${NC}"
echo -e "${YELLOW}Información crítica para configurar tu cliente local:${NC}"
echo -e "--------------------------------------------------------"
echo -e "1. ${GREEN}Peer ID de este nodo:${NC} ${PEER_ID}"
echo -e "2. ${GREEN}Contenido de tu swarm.key:${NC}"
echo -e "$(cat "$SWARM_KEY_PATH")"
echo -e "--------------------------------------------------------"
echo -e "${RED}ATENCIÓN:${NC} Copia el contenido de la clave swarm.key de arriba tal cual y"
echo -e "guárdala en tu cliente local en ~/.ipfs/swarm.key (o en la carpeta de configuración de tu cliente)."
echo -e "Sin esta clave exacta, ningún cliente podrá conectarse a este nodo."
echo -e ""
echo -e "${YELLOW}Para verificar el estado en el servidor:${NC} systemctl status ipfs"
echo -e "${YELLOW}Para ver los logs:${NC} journalctl -u ipfs -n 50 -f"
