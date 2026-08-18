import subprocess
import os
import sys

# Ensure UTF-8 output encoding for Windows terminal compatibility
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def upload_to_github():
    repo_dir = r"c:\Users\IPHIX\Documents\Projects\DFRNT"
    target_folder = "World Economic Forum"
    
    print(f"=== Iniciando proceso de carga a GitHub para '{target_folder}' ===")
    print(f"Directorio del Repositorio: {repo_dir}\n")
    
    try:
        # 1. git add
        print(f"[1/3] Añadiendo carpeta '{target_folder}' a Git staging...")
        res_add = subprocess.run(["git", "add", target_folder, "Documentacion/World Economic Forum"], cwd=repo_dir, capture_output=True, text=True)
        if res_add.returncode != 0:
            print(f"[ERROR] en 'git add': {res_add.stderr}")
            return
        print("  -> Archivos añadidos a staging exitosamente.")
        
        # 2. git commit
        commit_msg = "feat: add World Economic Forum section with AI-First WEF vs A&AD benchmark HTML"
        print(f"\n[2/3] Creando commit: '{commit_msg}'...")
        res_commit = subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo_dir, capture_output=True, text=True)
        print("  -> Output Commit:")
        commit_out = res_commit.stdout.strip() if res_commit.stdout else "Sin cambios pendientes."
        print(f"     {commit_out}")
        
        # 3. git push
        print("\n[3/3] Subiendo cambios a GitHub ('git push origin main')...")
        res_push = subprocess.run(["git", "push", "origin", "main"], cwd=repo_dir, capture_output=True, text=True)
        if res_push.returncode == 0:
            print("\n[ÉXITO] La carpeta 'World Economic Forum' fue subida correctamente a GitHub.")
            if res_push.stdout:
                print(res_push.stdout)
        else:
            print(f"\n[RESPUESTA PUSH] {res_push.stdout} {res_push.stderr}")
            
    except Exception as e:
        print(f"[ERROR INESPERADO] {e}")

if __name__ == "__main__":
    upload_to_github()
