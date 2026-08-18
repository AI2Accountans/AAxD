import subprocess
import os
import sys

def upload_to_github():
    repo_dir = r"c:\Users\IPHIX\Documents\Projects\DFRNT"
    target_folder = "World Economic Forum"
    
    print(f"🚀 Iniciando proceso de carga a GitHub para '{target_folder}'...")
    print(f"📁 Directorio del Repositorio: {repo_dir}\n")
    
    try:
        # 1. git add
        print(f"1️⃣ Añadiendo carpeta '{target_folder}' a Git staging...")
        res_add = subprocess.run(["git", "add", target_folder, "Documentacion/World Economic Forum"], cwd=repo_dir, capture_output=True, text=True)
        if res_add.returncode != 0:
            print(f"❌ Error en 'git add': {res_add.stderr}")
            return
        print("   ✓ Archivos añadidos a staging.")
        
        # 2. git commit
        commit_msg = "feat: add World Economic Forum section with AI-First WEF vs A&AD benchmark HTML"
        print(f"2️⃣ Creando commit: '{commit_msg}'...")
        res_commit = subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_dir, capture_output=True, text=True)
        print("   Output Commit:")
        print("  ", res_commit.stdout.strip() if res_commit.stdout else "Sin cambios pendientes en el commit.")
        
        # 3. git push
        print("3️⃣ Subiendo cambios a GitHub ('git push origin main')...")
        res_push = subprocess.run(["git", "push", "origin", "main"], cwd=repo_dir, capture_output=True, text=True)
        if res_push.returncode == 0:
            print("✅ ¡Éxito! La carpeta 'World Economic Forum' fue subida correctamente a GitHub.")
            if res_push.stdout:
                print(res_push.stdout)
        else:
            print(f"⚠️ Respuesta del Push: {res_push.stdout} {res_push.stderr}")
            
    except Exception as e:
        print(f"💥 Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    upload_to_github()
