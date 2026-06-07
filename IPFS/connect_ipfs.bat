@echo off
title Conexión Segura IPFS (Túnel SSH)
color 0B
echo ==========================================================
echo       CONEXION SEGURA AL SERVIDOR IPFS (DIGITALOCEAN)
echo ==========================================================
echo Este script creará un túnel SSH encriptado para que puedas
echo acceder al API (5001) y al Gateway (8080) del IPFS remoto
echo de forma 100%% segura, como si estuviera en tu computadora.
echo ==========================================================
echo.

:: Solicitar datos de conexión
set /p IP_DROPLET="1. Introduce la direccion IP de tu Droplet: "
set /p USER_DROPLET="2. Introduce tu usuario SSH (por defecto 'root'): "
if "%USER_DROPLET%"=="" set USER_DROPLET=root

echo.
echo ==========================================================
echo Intentando abrir el túnel SSH seguro...
echo Se mapeará:
echo   - Local localhost:5001  -> Remoto 127.0.0.1:5001 (API)
echo   - Local localhost:8080  -> Remoto 127.0.0.1:8081 (Gateway redireccionado)
echo.
echo IMPORTANTE: Si te solicita confirmación de clave de host, escribe 'yes'.
echo Deja esta ventana abierta mientras uses IPFS. Para cerrar el túnel, cierra esta ventana.
echo ==========================================================
echo.

:: Ejecutar el túnel SSH. 
:: -N indica no ejecutar comandos remotos (solo tunelizar)
:: -L define el reenvío de puertos locales
ssh -N -L 5001:127.0.0.1:5001 -L 8080:127.0.0.1:8081 %USER_DROPLET%@%IP_DROPLET%

if %errorlevel% neq 0 (
    color 0C
    echo.
    echo [ERROR] La conexion SSH falló o fue cerrada.
    echo Asegúrate de tener configurada tu clave SSH o contraseña correcta,
    echo y que el puerto 22 del Droplet esté abierto.
    pause
)
