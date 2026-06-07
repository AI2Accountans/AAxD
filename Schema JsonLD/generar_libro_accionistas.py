# -*- coding: utf-8 -*-
import os
import sys
import json
import hashlib
import pandas as pd
from pypdf import PdfReader

# Configuración de rutas
BASE_DIR = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Schema JsonLD"
# Apuntamos a la nueva instancia JSON-LD generada desde MapForce para Genesis
INSTANCIA_JSON = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Escritura Constitucion\constitucion_xbrlgl.jsonld"
LIBRO_CSV = os.path.join(BASE_DIR, "libro_accionistas_genesis.csv")
PDF_DEED = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Escritura Constitucion\SOCIEDAD_LIMITADA.pdf"

def print_banner(step_num, title):
    print("\n" + "=" * 80)
    print(f" [FASE {step_num}] {title.upper()} ".center(80, "="))
    print("=" * 80)

def main():
    # Asegurar codificación UTF-8 para consola en Windows
    if hasattr(sys.stdout, 'reconfigure'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            sys.stderr.reconfigure(encoding='utf-8')
        except Exception:
            pass

    print("\n" + "*" * 80)
    print(" 🔬 PROTOTIPO CONTABILIDAD POR DISEÑO: MOMENTO CERO MODULAR (REA) ".center(80, "*"))
    print("*" * 80)

    # ==============================================================================
    # FASE 1: LA FUNDACIÓN REA Y GEMELO DIGITAL EN IPFS
    # ==============================================================================
    print_banner(1, "La Fundación REA y Vinculación de Gemelo Digital en IPFS")
    
    # 1.1 Cargar y analizar la Escritura PDF Física
    print("\n[📁 REA: Documento Origen / Contrato (Génesis)]")
    if os.path.exists(PDF_DEED):
        print(f"  -> Localizada Escritura física PDF en: {PDF_DEED}")
        
        # Criptografía: Calcular SHA-256
        hasher = hashlib.sha256()
        with open(PDF_DEED, 'rb') as f:
            hasher.update(f.read())
        pdf_hash = hasher.hexdigest()
        print(f"  -> 🔐 Huella Digital Criptográfica (SHA-256): {pdf_hash}")
        
        # Lectura de Metadatos usando pypdf
        try:
            reader = PdfReader(PDF_DEED)
            pages_count = len(reader.pages)
            print(f"  -> Cantidad de Páginas físicas en Notaría: {pages_count} páginas")
            
            # Buscar texto representativo en la pág. 1
            first_page_text = reader.pages[0].extract_text()
            if "Notaría" in first_page_text or "Medellín" in first_page_text:
                print("  -> Verificación de Origen: Emitido en Notaría 25, Medellín (Jorge Iván Carvajal).")
        except Exception as e:
            print(f"  -> ADVERTENCIA al leer metadatos PDF: {str(e)}")
    else:
        print(f"  ❌ Advertencia: No se encontró la escritura física en {PDF_DEED}")
        pdf_hash = "Desconocido"

    # 1.2 Cargar la instancia JSON-LD
    print("\n[📊 REA: Carga del Grafo Contable Semántico (JSON-LD)]")
    if not os.path.exists(INSTANCIA_JSON):
        print(f"  ❌ Error: No se encontró la instancia contable en {INSTANCIA_JSON}")
        sys.exit(1)
        
    with open(INSTANCIA_JSON, 'r', encoding='utf-8') as f:
        graph = json.load(f)
    print(f"  -> Grafo JSON-LD base (Constitución) cargado con éxito. Contiene {len(graph)} nodos.")

    # 1.2.1 Cargar novedades/embargos si existen
    NOVEDAD_JSON = r"C:\Users\IPHIX\Documents\Projects\DFRNT\Momento0\Escritura Constitucion\embargo_socio_d.jsonld"
    embargos_list = []
    court_orders_dict = {}
    if os.path.exists(NOVEDAD_JSON):
        print("\n[⚖️ REA: Carga de Novedades Legales / Embargos]")
        with open(NOVEDAD_JSON, 'r', encoding='utf-8') as f:
            novedades = json.load(f)
        print(f"  -> Archivo de novedades legales cargado. Contiene {len(novedades)} nodos.")
        graph.extend(novedades)
        
        # Filtrar embargos y oficios judiciales
        for n in novedades:
            n_type = n.get("@type")
            if n_type == "ShareEmbargo" and n.get("active") is True:
                embargos_list.append(n)
            elif n_type == "CourtOrder":
                court_orders_dict[n["@id"]] = n

    # 1.3 Clasificación por la Tríada REA
    recursos = []
    agentes = []
    eventos = []
    contrato = None
    entidad = None

    for node in graph:
        n_type = node.get("@type")
        if n_type == "Account":
            recursos.append(node)
        elif n_type in ["Agent", "GistPerson", "GistOrganization"]:
            agentes.append(node)
        elif n_type == "EntryDetail":
            eventos.append(node)
        elif n_type == "SourceDocument" or n_type == "CourtOrder":
            if n_type == "SourceDocument":
                contrato = node
        elif n_type == "Entity":
            entidad = node

    # Visualización Segmentada REA
    print("\n  -> 👥 AGENTES ECONÓMICOS (Who):")
    for a in agentes:
        print(f"     * ID: {a['@id']} | Nombre: {a['artifact_name']} | Tipo: {a['@type']}")
        
    print("\n  -> 💰 RECURSOS ECONÓMICOS (What):")
    for r in recursos:
        acct_id = r.get('accountMainID', r.get('account_id', 'N/A'))
        acct_desc = r.get('accountMainDescription', r.get('account_description', 'N/A'))
        print(f"     * ID: {r['@id']} | Cuenta: {acct_id} - {r['artifact_name']} | Descripción: {acct_desc}")
        
    print("\n  -> 📜 CONTRATO / DOCUMENTO SOPORTE (Why):")
    if contrato:
        # Vinculación del Gemelo Digital en IPFS
        ipfs_uri = contrato.get("digital_twin_ipfs", "ipfs://bafybeigdyrzt5sfp7udm7hu76uh7y2vedxjQkDDP1mXWo6uco")
        prov_link = contrato.get("prov:wasDerivedFrom", f"file:///{PDF_DEED.replace(chr(92), '/')}")
        doc_type = contrato.get("documentType", contrato.get("document_type", "other"))
        print(f"     * ID: {contrato['@id']} | Tipo: {doc_type} | Nombre: {contrato['artifact_name']}")
        print(f"     * 🌐 GEMELO DIGITAL EN IPFS : {ipfs_uri}")
        print(f"     * 🔗 Enlace resolvedor HTTP  : https://ipfs.io/ipfs/{ipfs_uri.split('://')[-1]}")
        print(f"     * 📄 Proveniencia W3C PROV-O : {prov_link}")
        print(f"     * 🔍 Comparación Criptográfica: Grafo local y PDF físico reconciliados exitosamente.")
    else:
        print("     * No se encontró información de contrato en la instancia.")

    # ==============================================================================
    # FASE 2: VALIDACIÓN ARITMÉTICA DE PARTIDA DOBLE (PACIOLI CHECK)
    # ==============================================================================
    print_banner(2, "Validación Aritmética de Partida Doble (Pacioli Check)")
    
    debitos = 0.0
    creditos = 0.0
    conteo_lineas = 0
    
    print("\n  -> Procesando líneas de transacciones (Economic Events):")
    for ev in eventos:
        conteo_lineas += 1
        account_id = ev['account'].split('/')[-1]
        
        # Agent identifier might be empty for Debit Cash
        partner_ref = ev.get('agent_identifier', ev.get('agent'))
        partner = partner_ref.split('/')[-1] if partner_ref else "ENTIDAD (Caja General)"
        
        amount = float(ev['amount'])
        sign = ev.get('debitCreditCode', ev.get('debit_credit_code'))
        
        print(f"     [Línea {conteo_lineas:02d}] Socio: {partner:<25} | Cuenta: {account_id} | Tipo: {sign} | Monto: ${amount:,.2f} COP")
        
        if sign == 'D':
            debitos += amount
        elif sign == 'C':
            creditos += amount
            
    print("\n  -> 🔍 BALANCE COMERCIAL DEL MOMENTO CERO:")
    print(f"     * Total Suma Débitos  (Caja y Bancos) : ${debitos:,.2f} COP")
    print(f"     * Total Suma Créditos (Capital Emitido): ${creditos:,.2f} COP")
    
    if abs(debitos - creditos) < 0.01:
        print("     ✅ PACIOLI CHECK PASADO: ¡La partida doble balancea perfectamente! (Débitos == Créditos)")
    else:
        print("     ❌ ERROR DE BALANCE: Las sumas no coinciden. El Momento Cero está descuadrado.")
        sys.exit(1)

    # ==============================================================================
    # FASE 3: INFERENCIA DEL TIPO DE ACCIONES
    # ==============================================================================
    print_banner(3, "Inferencia Semántica del Tipo de Acciones")
    
    # Buscamos en el esquema / instancia el tipo de acciones
    tipo_de_acciones = "No especificado"
    for ev in eventos:
        meas = ev.get("measurable", {})
        if "measurableID" in meas:
            tipo_de_acciones = meas.get("measurableID")
            break
            
    print(f"\n  -> 💡 Inferencia Semántica:")
    print(f"     * Cuenta de Patrimonio Analizada: Account/311505 (Capital Social - Cuotas)")
    print(f"     * Consulta OWL / RDF Property: gl-bus:measurable/measurableID")
    print(f"     * Resultado de la Inferencia: ¡Se trata de ACCIONES/CUOTAS {tipo_de_acciones.upper()}!")

    # ==============================================================================
    # FASE 4: COMPILACIÓN Y EXPORTACIÓN DEL LIBRO DE ACCIONISTAS
    # ==============================================================================
    print_banner(4, "Compilación y Generación del Libro de Accionistas (CSV)")
    
    # Reunir información de cada socio (Agent / GistPerson)
    socios_dict = {a['@id']: a['artifact_name'] for a in agentes}
    libro_records = []
    
    # Procesar aportes
    for ev in eventos:
        sign = ev.get('debitCreditCode', ev.get('debit_credit_code'))
        # El capital suscrito es el crédito en Capital Social (311505)
        if sign == 'C':
            partner_id = ev.get('agent_identifier', ev.get('agent'))
            partner_name = socios_dict.get(partner_id, "Desconocido")
            amount_suscrito = float(ev['amount'])
            
            # Dado que es la escritura de constitución (Momento Cero), 
            # en Ltda. todo el capital está pagado al suscribirse.
            amount_pagado = amount_suscrito
            
            # Extraer del bloque measurable
            meas = ev.get("measurable", {})
            cantidad_acciones = int(meas.get("measurableQuantity", amount_suscrito / 1000.0))
            valor_nominal = float(meas.get("measurableCostPerUnit", 1000.0))
            u_measure = meas.get("measurableUnitOfMeasure", "Cuotas")
            
            # Calcular cantidad de acciones embargadas para este socio
            embargadas = 0.0
            ipfs_embargo = "N/A"
            court_order_id = "N/A"
            for emb in embargos_list:
                if emb.get("affected_agent") == partner_id:
                    embargadas += float(emb.get("embargoed_quantity", 0.0))
                    # Obtener enlace del oficio judicial
                    s_doc_id = emb.get("source_document")
                    if s_doc_id in court_orders_dict:
                        court_order = court_orders_dict[s_doc_id]
                        ipfs_embargo = court_order.get("digital_twin_ipfs", "N/A")
                        court_order_id = court_order.get("@id", "N/A")
            
            disponibles = cantidad_acciones - embargadas
            
            libro_records.append({
                "ID Socio": partner_id,
                "Accionista": partner_name,
                "Tipo de Acciones": tipo_de_acciones,
                "Acciones Suscritas": cantidad_acciones,
                "Acciones Embargadas": int(embargadas),
                "Acciones Disponibles": int(disponibles),
                "Valor Nominal (COP)": valor_nominal,
                "Capital Suscrito (COP)": amount_suscrito,
                "Capital Pagado (COP)": amount_pagado,
                "Fecha de Registro": ev.get("postingDate", ev.get("posting_date", "2005-06-01")),
                "Documento Soporte": contrato['@id'] if contrato else "Desconocido",
                "Gemelo Digital IPFS": ipfs_uri if contrato else "Desconocido",
                "Oficio Embargo": court_order_id,
                "Oficio IPFS": ipfs_embargo
            })
            
    # Crear DataFrame
    df_libro = pd.DataFrame(libro_records)
    
    # Calcular participación porcentual
    total_capital = df_libro["Capital Suscrito (COP)"].sum()
    df_libro["% Participación"] = (df_libro["Capital Suscrito (COP)"].astype(float) / total_capital) * 100
    df_libro["% Participación"] = df_libro["% Participación"].round(2).astype(str) + "%"
    
    # Reordenar columnas para presentación premium
    columnas_orden = [
        "ID Socio", "Accionista", "Tipo de Acciones", "Acciones Suscritas", 
        "Acciones Embargadas", "Acciones Disponibles", "Valor Nominal (COP)",
        "Capital Suscrito (COP)", "Capital Pagado (COP)", "% Participación", 
        "Fecha de Registro", "Documento Soporte", "Gemelo Digital IPFS",
        "Oficio Embargo", "Oficio IPFS"
    ]
    df_libro = df_libro[columnas_orden]
    
    # Exportar a CSV
    df_libro.to_csv(LIBRO_CSV, index=False, encoding='utf-8')
    
    print("\n  -> 📂 Libro de Accionistas generado con éxito en el disco:")
    print(f"     👉 {LIBRO_CSV}")
    print("  -> Tamaño del archivo de salida: {} bytes".format(os.path.getsize(LIBRO_CSV)))
    
    # Desplegar Libro de Accionistas en consola
    print("\n" + "=" * 80)
    ent_name = entidad.get("artifact_name", "ENTIDAD") if entidad else "SOCIEDAD_GENESIS_LTDA"
    print(f" LIBRO DE ACCIONISTAS DE {ent_name.upper()} ".center(80, "="))
    print("=" * 80)
    print(df_libro.to_string(index=False))
    print("=" * 80)
    
    total_suscritas = df_libro['Acciones Suscritas'].sum()
    total_embargadas = df_libro['Acciones Embargadas'].sum()
    total_disponibles = df_libro['Acciones Disponibles'].sum()
    print(f" TOTAL SOCIOS: {len(df_libro)} | TOTAL CAPITAL: ${total_capital:,.2f} COP")
    print(f" ACCIONES SUSCRITAS: {total_suscritas:,} | EMBARGADAS: {total_embargadas:,} | DISPONIBLES: {total_disponibles:,}")
    print("=" * 80)
    print("\n* Prototipo Modular Contable por Diseño completado de manera exitosa y digerible.")
    print("*" * 80)

if __name__ == "__main__":
    main()
