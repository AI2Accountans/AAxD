# Gestor Seguro de Archivos IPFS - DigitalOcean y Windows

Este proyecto contiene las herramientas necesarias para configurar y operar tu propio nodo de IPFS privado y seguro en DigitalOcean, encriptando todos tus archivos confidenciales localmente con **AES-256** antes de subirlos.

---

## Estructura del Proyecto

*   **`install_ipfs.sh`**: Script para configurar e instalar IPFS en tu Droplet de DigitalOcean en modo de red privada aislada.
*   **`connect_ipfs.bat`**: Script de Windows para iniciar el túnel SSH seguro.
*   **`secure_ipfs_helper.py`**: Aplicación local en Python para encriptar, subir, descargar, desencriptar y organizar tus archivos contables y de auditoría.

---

## Instrucciones de Instalación y Uso

### Paso 1: Configurar el Servidor (DigitalOcean)

1. Conéctate por SSH a tu Droplet:
   ```bash
   ssh root@TU_IP_DEL_DROPLET
   ```
2. Crea el archivo del instalador en tu servidor:
   ```bash
   nano install_ipfs.sh
   ```
3. Copia todo el contenido del archivo local `install_ipfs.sh` de este proyecto y pégalo dentro de la terminal de nano. Guarda con `Ctrl+O`, presiona `Enter` y sal con `Ctrl+X`.
4. Concede permisos de ejecución al script y arráncalo:
   ```bash
   chmod +x install_ipfs.sh
   sudo ./install_ipfs.sh
   ```
5. El script instalará Kubo (IPFS), generará un `swarm.key` de enjambre privado, aislará el nodo eliminando los bootstrap públicos y configurará el daemon en systemd de forma segura. Al terminar, imprimirá la información del estado del servicio.

---

### Paso 2: Conectar el Cliente (Windows)

1. En tu máquina local Windows, haz doble clic sobre el archivo **`connect_ipfs.bat`**.
2. Introduce la **dirección IP de tu Droplet** y presiona `Enter`.
3. Introduce el **usuario de SSH** (ej. `root`) y presiona `Enter`.
4. El script abrirá un canal SSH encriptado y reenviará los puertos de IPFS (5001 y 8080) locales a tu servidor.
5. **Deja esta ventana abierta** todo el tiempo que uses el gestor de archivos. Al cerrarla se corta la comunicación de forma segura.

---

### Paso 3: Ejecutar el Gestor de Archivos (Windows)

1. Abre una terminal de Windows (CMD o PowerShell) en esta carpeta y ejecuta:
   ```cmd
   python secure_ipfs_helper.py
   ```
2. El script detectará si te falta alguna librería de Python (como `requests` o `cryptography`) y la instalará automáticamente si es necesario.
3. Te pedirá establecer o introducir una **Contraseña Maestra**.
   *   **IMPORTANTE**: Esta contraseña encripta tu índice local (`ipfs_registry.json.enc`) y los archivos subidos. Si la olvidas, perderás el acceso a los archivos.
4. El programa te mostrará un menú interactivo:
    *   **Opción 1:** Listar archivos subidos, organizados y clasificados por Cliente, Año y Categoría.
    *   **Opción 2:** Seleccionar un archivo de tu PC local, clasificarlo, encriptarlo con AES-256 y subirlo a IPFS.
    *   **Opción 3:** Descargar y desencriptar un archivo de IPFS a la carpeta que elijas.
    *   **Opción 4:** Desanclar y remover archivos del nodo IPFS y el registro local.
    *   **Opción 5:** Cambiar la contraseña maestra (re-encriptando el registro con la nueva clave).

---

## Características de Seguridad

1.  **Red Privada Completa (Private Swarm):** Tu nodo está aislado de la red global de IPFS usando una clave pre-compartida (`swarm.key`). Nadie fuera de tu red privada puede ver o transferir bloques.
2.  **Cifrado en Tránsito y Reposo (AES-256 + HMAC-SHA256):** Los archivos se cifran de extremo a extremo (Client-Side Encryption). IPFS solo almacena trozos de datos encriptados ilegibles.
3.  **Firewall a Nivel de Puerto:** El API de IPFS está configurada para escuchar solo en `127.0.0.1`. Esto significa que no hay puertos administrativos expuestos directamente a internet en DigitalOcean. El acceso se restringe al túnel SSH autenticado.
