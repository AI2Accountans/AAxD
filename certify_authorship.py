import hashlib
import json
import os
import sys
import time

try:
    from algosdk import account, mnemonic
    from algosdk.v2client import algod
    from algosdk.transaction import PaymentTxn
    import qrcode
except ImportError as e:
    print("==================================================")
    print("Hubo un error cargando las dependencias:")
    print(e)
    print("Si te faltan librerías, ejecuta:")
    print("pip install py-algorand-sdk qrcode[pil] Pillow")
    print("==================================================")
    sys.exit(1)

def get_sha256_hash(filepath):
    """Genera el hash SHA-256 de un archivo, equivalente a su 'huella digital' matemática."""
    with open(filepath, 'rb') as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

def main():
    print("\n--- SISTEMA DE PRUEBA DE AUTORIA (Algorand & GitHub) ---")
    
    pdf_en = "AA_D_en.pdf"
    pdf_es = "AA_D_es.pdf"
    
    if not os.path.exists(pdf_en) or not os.path.exists(pdf_es):
        print(f"\n[ERROR] No se encontraron los archivos {pdf_en} o {pdf_es} en la carpeta actual.")
        print("Asegúrate de compilar los .tex a .pdf con ese nombre exacto antes de ejecutar este script.")
        return
        
    hash_en = get_sha256_hash(pdf_en)
    hash_es = get_sha256_hash(pdf_es)
    
    print("\n[+] Hashes SHA-256 Generados Localmente:")
    print(f"    EN PDF: {hash_en}")
    print(f"    ES PDF: {hash_es}")
    
    print("\n[+] Generando nueva cuenta de Algorand MAINNET temporal...")
    private_key, address = account.generate_account()
    print(f"    Address (Dirección): {address}")
    
    print("\n" + "="*70)
    print("  ACCIÓN REQUERIDA: FONDEAR CUENTA")
    print("="*70)
    print("Para poder registrar la transacción en la blockchain principal, necesitamos una fracción mínima de ALGO.")
    print("Por favor, sigue estos pasos:")
    print("  1. Abre tu Pera Wallet (o cualquier billetera de Algorand en MainNet).")
    print(f"  2. Envía 0.15 ALGO a esta dirección temporal:\n     {address}")
    print("="*70)
    
    input("\nUna vez que hayas enviado los fondos desde Pera Wallet, presiona Enter para continuar...")
    
    # Nos conectamos a un nodo público gratuito de la MainNet (Algonode)
    print("\n[+] Conectando a Algorand MainNet...")
    algod_address = "https://mainnet-api.algonode.cloud"
    algod_client = algod.AlgodClient("", algod_address)
    
    try:
        params = algod_client.suggested_params()
    except Exception as e:
        print(f"[ERROR] No se pudo conectar a la red: {e}")
        return
    
    # Creamos el JSON que irá inyectado inmutablemente en la blockchain
    note_dict = {
        "type": "authorship_proof",
        "author": "Richard G. Gasca Buelvas",
        "license": "Apache 2.0",
        "hosting": "GitHub Open Source",
        "documents": {
            "AA_D_en.pdf": hash_en,
            "AA_D_es.pdf": hash_es
        }
    }
    note = json.dumps(note_dict).encode()
    
    # Enviamos una transacción de 0 ALGO a nosotros mismos, pero con la 'nota' cargada.
    print("[+] Firmando transacción y estampando los hashes en la blockchain...")
    txn = PaymentTxn(
        sender=address,
        sp=params,
        receiver=address,
        amt=0,
        note=note
    )
    
    signed_txn = txn.sign(private_key)
    try:
        txid = algod_client.send_transaction(signed_txn)
        print(f"    ID de Transacción: {txid}")
        
        print("[+] Esperando confirmación en la red...")
        txinfo = algod_client.pending_transaction_info(txid)
        while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
            time.sleep(2)
            txinfo = algod_client.pending_transaction_info(txid)
        
        print(f"    [OK] Confirmado en la ronda de bloques: {txinfo.get('confirmed-round')}")
        
        # Explorador Pera para MainNet
        explorer_url = f"https://explorer.perawallet.app/tx/{txid}"
        print(f"\n[+] Puedes verificar la transacción pública aquí: \n    {explorer_url}")
        
        print("\n[+] Generando código QR...")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(explorer_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("authorship_qr.png")
        
        print("\n" + "="*70)
        print(" ¡PROCESO FINALIZADO CON ÉXITO!")
        print("="*70)
        print(" 1. El código QR 'authorship_qr.png' se ha creado en esta carpeta.")
        print(" 2. El código fuente LaTeX ya está preparado para leer esta imagen.")
        print(" 3. Ahora solo debes recompilar tus archivos .tex para generar los PDFs finales")
        print("    (los cuales ya incluirán el código QR de autoría en la portada).")
        print(" 4. Puedes subir el framework y el PDF a GitHub con Licencia Apache de forma segura.")
        
    except Exception as e:
        print(f"\n[ERROR] al procesar la transacción: {e}")
        print("Asegúrate de haber enviado suficientes fondos (recomendado 0.15 ALGO) a la dirección temporal para cubrir el saldo mínimo y las comisiones.")

if __name__ == '__main__':
    main()
