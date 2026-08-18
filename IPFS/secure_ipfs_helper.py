#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import base64
import datetime
import subprocess
import getpass

# 1. Asegurar que las dependencias estén instaladas
try:
    import requests
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
except ImportError:
    print("==================================================================")
    print("Faltan dependencias críticas. Instalando 'requests' y 'cryptography'...")
    print("==================================================================")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "cryptography"])
        import requests
        from cryptography.fernet import Fernet
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
        print("¡Instalación exitosa!\n")
    except Exception as e:
        print(f"\n[ERROR] No se pudieron instalar las dependencias automáticamente: {e}")
        print("Por favor, abre una terminal (cmd/PowerShell) y ejecuta:")
        print("pip install requests cryptography")
        input("\nPresiona Enter para salir...")
        sys.exit(1)

# Configuración básica
IPFS_API_URL = "http://127.0.0.1:5001/api/v0"
REGISTRY_FILE = "ipfs_registry.json.enc"

# Funciones de Encriptación (AES-256 mediante Fernet + PBKDF2 con 480k iteraciones)
def derivar_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_bytes(data: bytes, password: str) -> bytes:
    salt = os.urandom(16)
    key = derivar_key(password, salt)
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    # Guardamos el salt al principio del archivo (16 bytes)
    return salt + encrypted_data

def decrypt_bytes(encrypted_data_with_salt: bytes, password: str) -> bytes:
    if len(encrypted_data_with_salt) < 16:
        raise ValueError("El archivo está corrupto o es inválido.")
    salt = encrypted_data_with_salt[:16]
    actual_encrypted = encrypted_data_with_salt[16:]
    key = derivar_key(password, salt)
    f = Fernet(key)
    return f.decrypt(actual_encrypted)

# Gestión del Registro Local Encriptado (Base de Datos Local de Metadatos)
def cargar_registro(password: str) -> dict:
    if not os.path.exists(REGISTRY_FILE):
        # Crear un registro nuevo
        print("[Info] No se encontró un registro existente. Se creará uno nuevo con esta contraseña.")
        return {"verification": "OK", "files": []}
    
    try:
        with open(REGISTRY_FILE, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = decrypt_bytes(encrypted_data, password)
        registry = json.loads(decrypted_data.decode("utf-8"))
        if registry.get("verification") == "OK":
            return registry
        else:
            raise ValueError()
    except Exception:
        raise ValueError("Contraseña incorrecta o archivo de datos corrupto.")

def guardar_registro(registry: dict, password: str):
    try:
        data = json.dumps(registry).encode("utf-8")
        encrypted_data = encrypt_bytes(data, password)
        with open(REGISTRY_FILE, "wb") as f:
            f.write(encrypted_data)
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el registro local: {e}")

# Verificación de conexión con el Servidor IPFS mediante el túnel SSH
def verificar_conexion_ipfs() -> bool:
    try:
        response = requests.post(f"{IPFS_API_URL}/version", timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Interfaz de Consola
def mostrar_menu():
    print("\n" + "="*60)
    print("     GESTOR SEGURO DE ARCHIVOS IPFS - AUDITORIA & CONTABILIDAD")
    print("="*60)
    print(" [1] Listar y organizar mis archivos")
    print(" [2] Encriptar y subir un archivo confidencial")
    print(" [3] Descargar y desencriptar un archivo")
    print(" [4] Desanclar (Eliminar) un archivo de IPFS")
    print(" [5] Cambiar Contraseña Maestra (Re-encriptar registro)")
    print(" [6] Salir")
    print("="*60)

def listar_archivos(registry: dict):
    files = registry.get("files", [])
    if not files:
        print("\n[!] No tienes ningún archivo registrado en tu red privada de IPFS.")
        return
    
    print("\n" + "-"*90)
    print(f"{'No.':<4} | {'Cliente':<15} | {'Año':<6} | {'Categoría':<15} | {'Archivo Original':<25} | {'Tamaño':<10}")
    print("-"*90)
    for idx, f in enumerate(files, 1):
        # Formatear tamaño
        sz = f.get('size_bytes', 0)
        if sz < 1024:
            sz_str = f"{sz} B"
        elif sz < 1024*1024:
            sz_str = f"{sz/1024:.1f} KB"
        else:
            sz_str = f"{sz/(1024*1024):.1f} MB"
            
        print(f"{idx:<4} | {f.get('client', 'N/A'):<15} | {f.get('year', 'N/A'):<6} | {f.get('category', 'N/A'):<15} | {f.get('original_name', 'N/A')[:25]:<25} | {sz_str:<10}")
    print("-"*90)
    
    ver_detalles = input("\n¿Deseas ver los detalles/CID de algún archivo? (Escribe el número o Presiona Enter para volver): ")
    if ver_detalles.isdigit():
        idx = int(ver_detalles) - 1
        if 0 <= idx < len(files):
            f = files[idx]
            print("\n--- DETALLES DEL ARCHIVO ---")
            print(f"Nombre Original: {f['original_name']}")
            print(f"Cliente:         {f['client']}")
            print(f"Año:             {f['year']}")
            print(f"Categoría:       {f['category']}")
            print(f"Fecha de Subida: {f['date_added']}")
            print(f"Tamaño Original: {f['size_bytes']} bytes")
            print(f"IPFS CID (Hash): {f['cid']}")
            print(f"Estado en IPFS:  Encriptado con AES-256")
        else:
            print("[!] Número inválido.")

def subir_archivo(registry: dict, password: str):
    if not verificar_conexion_ipfs():
        print("\n[ERROR] No se pudo conectar a la API de IPFS (puerto 5001).")
        print("Asegúrate de haber iniciado el túnel SSH ejecutando 'connect_ipfs.bat'.")
        return

    filepath = input("\nIntroduce la ruta completa del archivo local (ej. C:\\Documentos\\auditoria.xlsx): ").strip('"')
    if not os.path.exists(filepath):
        print("[ERROR] El archivo no existe en la ruta proporcionada.")
        return

    # Solicitar metadatos para organizar
    print("\n--- Clasificación del Documento ---")
    client = input("Nombre del Cliente (ej. Empresa ABC): ").strip()
    year = input("Año Contable / Auditoría (ej. 2025): ").strip()
    category = input("Categoría (ej. Impuestos, Balances, Contratos): ").strip()
    
    if not client or not year or not category:
        print("[ERROR] Todos los campos de clasificación son obligatorios para mantener el orden.")
        return

    original_name = os.path.basename(filepath)
    size_bytes = os.path.getsize(filepath)

    print("\nLeyendo y encriptando archivo con AES-256...")
    try:
        with open(filepath, "rb") as f:
            file_data = f.read()
        
        # Encriptar
        encrypted_data = encrypt_bytes(file_data, password)
    except Exception as e:
        print(f"[ERROR] No se pudo encriptar el archivo: {e}")
        return

    print("Subiendo datos encriptados a tu nodo IPFS en DigitalOcean...")
    try:
        # Enviar archivo como multipart/form-data
        files = {
            'file': (original_name + ".enc", encrypted_data)
        }
        response = requests.post(f"{IPFS_API_URL}/add", files=files, timeout=30)
        
        if response.status_code != 200:
            print(f"[ERROR] IPFS respondió con código: {response.status_code}")
            return
            
        res_json = response.json()
        cid = res_json.get("Hash")
        
        if not cid:
            print("[ERROR] No se recibió el hash CID de IPFS.")
            return

        # Registrar en la base de datos local encriptada
        nuevo_registro = {
            "original_name": original_name,
            "cid": cid,
            "client": client,
            "year": year,
            "category": category,
            "size_bytes": size_bytes,
            "date_added": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        registry["files"].append(nuevo_registro)
        guardar_registro(registry, password)
        
        print("\n" + "="*50)
        print("   ¡ARCHIVO SUBIDO E INDEXADO CON EXITO!")
        print("="*50)
        print(f"Archivo:   {original_name}")
        print(f"IPFS CID:  {cid}")
        print(f"Seguridad: Encriptado localmente antes del envío.")
        print("="*50)

    except Exception as e:
        print(f"[ERROR] Fallo al interactuar con IPFS: {e}")

def descargar_archivo(registry: dict, password: str):
    if not verificar_conexion_ipfs():
        print("\n[ERROR] No se pudo conectar a la API de IPFS (puerto 5001).")
        print("Asegúrate de que el túnel SSH está abierto.")
        return

    files = registry.get("files", [])
    if not files:
        print("\n[!] No tienes ningún archivo registrado para descargar.")
        return

    # Listar para selección rápida
    print("\nSelecciona el archivo que deseas descargar:")
    for idx, f in enumerate(files, 1):
        print(f" [{idx}] {f['client']} ({f['year']}) - {f['original_name']}")
    
    seleccion = input("\nIntroduce el número de archivo: ")
    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(files)):
        print("[!] Selección inválida.")
        return
        
    file_info = files[int(seleccion) - 1]
    cid = file_info["cid"]
    original_name = file_info["original_name"]

    # Carpeta de destino
    dest_dir = input(f"\nIntroduce la ruta de la carpeta de destino (Presiona Enter para guardar en la carpeta actual): ").strip('"')
    if not dest_dir:
        dest_dir = os.getcwd()
    elif not os.path.exists(dest_dir):
        print("[ERROR] La carpeta de destino no existe.")
        return

    dest_filepath = os.path.join(dest_dir, original_name)

    print(f"\nDescargando archivo encriptado de IPFS ({cid})...")
    try:
        response = requests.post(f"{IPFS_API_URL}/cat", params={"arg": cid}, timeout=60)
        if response.status_code != 200:
            print(f"[ERROR] No se pudo descargar de IPFS. Código de estado: {response.status_code}")
            return
        
        encrypted_content = response.content
    except Exception as e:
        print(f"[ERROR] Error al descargar de IPFS: {e}")
        return

    print("Desencriptando archivo localmente...")
    try:
        decrypted_content = decrypt_bytes(encrypted_content, password)
        
        with open(dest_filepath, "wb") as f:
            f.write(decrypted_content)
            
        print("\n" + "="*50)
        print("   ¡ARCHIVO DESCARGADO Y DESENCRIPTADO!")
        print("="*50)
        print(f"Guardado en: {dest_filepath}")
        print("="*50)
    except Exception as e:
        print(f"[ERROR] No se pudo desencriptar el archivo: {e}")
        print("Esto puede deberse a una clave incorrecta o a corrupción de datos.")

def eliminar_archivo(registry: dict, password: str):
    if not verificar_conexion_ipfs():
        print("\n[ERROR] No se pudo conectar a la API de IPFS (puerto 5001).")
        print("Asegúrate de que el túnel SSH está abierto.")
        return

    files = registry.get("files", [])
    if not files:
        print("\n[!] No tienes ningún archivo registrado para eliminar.")
        return

    # Listar para selección rápida
    print("\nSelecciona el archivo que deseas eliminar de tu nodo y registro:")
    for idx, f in enumerate(files, 1):
        print(f" [{idx}] {f['client']} ({f['year']}) - {f['original_name']}")
    
    seleccion = input("\nIntroduce el número de archivo: ")
    if not seleccion.isdigit() or not (1 <= int(seleccion) <= len(files)):
        print("[!] Selección inválida.")
        return
        
    idx = int(seleccion) - 1
    file_info = files[idx]
    cid = file_info["cid"]

    confirmar = input(f"\n¿Estás seguro de que deseas desanclar (pin rm) el archivo '{file_info['original_name']}' de IPFS y quitarlo de tu registro? (s/n): ")
    if confirmar.lower() != 's':
        print("Operación cancelada.")
        return

    print(f"\nDesanclando (unpinning) {cid} en el servidor...")
    try:
        response = requests.post(f"{IPFS_API_URL}/pin/rm", params={"arg": cid}, timeout=10)
        if response.status_code == 200:
            print("[+] Archivo desanclado exitosamente del nodo.")
        else:
            # A veces ya estaba desanclado
            print(f"[!] Advertencia del servidor IPFS al desanclar: {response.text}")
    except Exception as e:
        print(f"[!] Error al desanclar de IPFS: {e}. Se procederá a eliminar del registro local.")

    # Eliminar de la base de datos
    del files[idx]
    guardar_registro(registry, password)
    print("[+] Archivo eliminado del registro local.")
    print("\n* Nota: El espacio físico en el Droplet se liberará cuando se ejecute el Garbage Collector de IPFS (ipfs repo gc).")

def cambiar_contrasena(registry: dict, actual_password: str):
    print("\n--- Cambio de Contraseña Maestra ---")
    nueva_pass = getpass.getpass("Introduce tu NUEVA contraseña maestra: ")
    if not nueva_pass or len(nueva_pass) < 6:
        print("[ERROR] La nueva contraseña debe tener al menos 6 caracteres.")
        return
    
    confirmar_pass = getpass.getpass("Confirma tu nueva contraseña: ")
    if nueva_pass != confirmar_pass:
        print("[ERROR] Las contraseñas no coinciden.")
        return
    
    # Guardar el registro usando la nueva contraseña
    guardar_registro(registry, nueva_pass)
    print("[+] Registro local re-encriptado con la nueva contraseña con éxito.")
    print("Usa tu nueva contraseña en los próximos inicios.")
    return nueva_pass

# Flujo Principal
def main():
    print("="*60)
    print("  INICIO DE SESION - GESTOR DE ARCHIVOS CONFIDENCIALES IPFS")
    print("="*60)
    
    # Solicitar la contraseña de forma oculta en terminal
    password = getpass.getpass("Introduce tu contraseña maestra: ")
    if not password:
        print("[ERROR] La contraseña no puede estar vacía.")
        input("\nPresiona Enter para salir...")
        sys.exit(1)
        
    try:
        registry = cargar_registro(password)
    except ValueError as e:
        print(f"\n[ERROR] {e}")
        input("\nPresiona Enter para salir...")
        sys.exit(1)

    # Informar estado del túnel SSH
    if verificar_conexion_ipfs():
        print("\n[✓] Conexión establecida exitosamente con el nodo IPFS remoto (túnel SSH activo).")
    else:
        print("\n[!] ADVERTENCIA: No se detecta conexión con el nodo IPFS en 'localhost:5001'.")
        print("    Asegúrate de ejecutar el archivo 'connect_ipfs.bat' para abrir el túnel SSH.")
        print("    Aún puedes listar tus archivos, pero no podrás subir o descargar nada.")

    while True:
        try:
            mostrar_menu()
            opcion = input("Elige una opción (1-6): ").strip()
            if opcion == "1":
                listar_archivos(registry)
            elif opcion == "2":
                subir_archivo(registry, password)
            elif opcion == "3":
                descargar_archivo(registry, password)
            elif opcion == "4":
                eliminar_archivo(registry, password)
            elif opcion == "5":
                nueva_pass = cambiar_contrasena(registry, password)
                if nueva_pass:
                    password = nueva_pass
            elif opcion == "6":
                print("\nCerrando sesión de forma segura. ¡Hasta luego!")
                break
            else:
                print("[!] Opción no válida. Intenta de nuevo.")
        except KeyboardInterrupt:
            print("\nSesión cerrada por el usuario.")
            break
        except Exception as e:
            print(f"\n[ERROR INESPERADO] {e}")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
