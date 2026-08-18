<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:vf="https://w3id.org/valueflows/ont/vf#">

  <xsl:output method="html" doctype-system="about:blank" indent="yes" encoding="UTF-8"/>

  <xsl:template match="/">
    <html lang="es">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>ISO/IEC 15944-4 REA Contract Viewer — DFRNT Audit Ledger</title>
        <link rel="preconnect" href="https://fonts.googleapis.com"/>
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin=""/>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;family=Outfit:wght@500;600;700&amp;display=swap" rel="stylesheet"/>
        
        <style>
          :root {
            --primary: #4F46E5;
            --primary-dark: #3730A3;
            --primary-light: #EEF2FF;
            --secondary: #0EA5E9;
            --success: #10B981;
            --success-light: #ECFDF5;
            --warning: #F59E0B;
            --bg-main: #F8FAFC;
            --card-bg: #FFFFFF;
            --text-main: #0F172A;
            --text-muted: #64748B;
            --border-color: #E2E8F0;
            --radius-lg: 16px;
            --radius-md: 10px;
            --shadow-md: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
          }

          * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
          }

          body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-main);
            color: var(--text-main);
            line-height: 1.6;
            padding: 2rem 1rem;
          }

          .container {
            max-width: 960px;
            margin: 0 auto;
          }

          /* BILINGUAL VISIBILITY */
          .lang-en {
            display: none;
          }

          /* HEROSHOT HEADER */
          .header-banner {
            background: linear-gradient(135deg, #1E1B4B 0%, #312E81 50%, #4F46E5 100%);
            color: white;
            padding: 2.5rem 2rem;
            border-radius: var(--radius-lg);
            box-shadow: 0 20px 30px -10px rgba(79, 70, 229, 0.3);
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
          }

          .header-banner::after {
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
            border-radius: 50%;
            pointer-events: none;
          }

          .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
          }

          .badge-iso {
            display: inline-block;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            color: #E0E7FF;
            font-size: 0.75rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            padding: 0.35rem 0.85rem;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
          }

          /* LANGUAGE SWITCH TOGGLE */
          .lang-switch {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 3px;
            display: flex;
            gap: 2px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 10;
          }

          .btn-lang {
            background: transparent;
            border: none;
            color: #C7D2FE;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.25rem 0.65rem;
            border-radius: 15px;
            cursor: pointer;
            transition: all 0.2s ease;
          }

          .btn-lang.active {
            background: #FFFFFF;
            color: #1E1B4B;
            box-shadow: 0 2px 6px rgba(0,0,0,0.15);
          }

          .header-banner h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
          }

          .header-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
            margin-top: 1.25rem;
            padding-top: 1.25rem;
            border-top: 1px solid rgba(255, 255, 255, 0.15);
            font-size: 0.9rem;
            color: #C7D2FE;
          }

          .header-meta span strong {
            color: white;
          }

          /* CARDS */
          .card {
            background: var(--card-bg);
            border-radius: var(--radius-lg);
            padding: 1.75rem;
            margin-bottom: 2rem;
            border: 1px solid var(--border-color);
            box-shadow: var(--shadow-md);
          }

          .card-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 600;
            color: var(--primary-dark);
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
          }

          .card-title::before {
            content: '';
            display: inline-block;
            width: 4px;
            height: 1.25rem;
            background-color: var(--primary);
            border-radius: 2px;
          }

          /* AGENTS GRID */
          .agents-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.25rem;
          }

          .agent-box {
            background: #F8FAFC;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 1.25rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
          }

          .agent-box:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px -3px rgba(0, 0, 0, 0.05);
          }

          .agent-type-tag {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            float: right;
          }

          .tag-buyer { background: #E0F2FE; color: #0369A1; }
          .tag-seller { background: #F3E8FF; color: #6B21A8; }

          .agent-name {
            font-weight: 700;
            font-size: 1.05rem;
            color: var(--text-main);
            margin: 0.5rem 0 0.25rem 0;
          }

          .agent-detail {
            font-size: 0.85rem;
            color: var(--text-muted);
          }

          .related-party-badge {
            display: inline-block;
            background: #FEF3C7;
            color: #92400E;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
            margin-top: 0.35rem;
          }

          /* TABLE STYLING */
          .table-container {
            overflow-x: auto;
          }

          table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
            text-align: left;
          }

          th {
            background-color: #F1F5F9;
            color: var(--text-muted);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.05em;
            padding: 0.85rem 1rem;
            border-bottom: 2px solid var(--border-color);
          }

          td {
            padding: 1rem;
            border-bottom: 1px solid var(--border-color);
            vertical-align: middle;
          }

          tr:last-child td {
            border-bottom: none;
          }

          tr:hover td {
            background-color: #F8FAFC;
          }

          .action-pill {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: lowercase;
          }

          .action-deliver-service { background-color: #E0F2FE; color: #0369A1; }
          .action-pay { background-color: #DCFCE7; color: #15803D; }
          .action-transfer { background-color: #F3E8FF; color: #7E22CE; }

          .quantity-box {
            font-weight: 700;
            color: var(--text-main);
          }

          /* RECIPROCITY CARD */
          .reciprocity-box {
            background: linear-gradient(90deg, #EFF6FF 0%, #EEF2FF 100%);
            border-left: 4px solid var(--primary);
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            padding: 1rem 1.25rem;
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 1rem;
          }

          .reciprocity-flow {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-weight: 600;
            font-size: 0.9rem;
          }

          .chip-inc { background: #DCFCE7; color: #166534; padding: 0.2rem 0.6rem; border-radius: 6px; }
          .chip-dec { background: #FEE2E2; color: #991B1B; padding: 0.2rem 0.6rem; border-radius: 6px; }

          footer {
            text-align: center;
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 2rem;
          }
        </style>

        <script>
          function setLanguage(lang) {
            const isEs = (lang === 'es');
            document.querySelectorAll('.lang-es').forEach(el => el.style.display = isEs ? 'inline' : 'none');
            document.querySelectorAll('.lang-en').forEach(el => el.style.display = isEs ? 'none' : 'inline');
            
            document.getElementById('btn-es').classList.toggle('active', isEs);
            document.getElementById('btn-en').classList.toggle('active', !isEs);
            document.documentElement.lang = lang;
          }
        </script>
      </head>
      <body>
        <div class="container">
          <xsl:apply-templates select="vf:BusinessTransaction"/>

          <footer>
            <p>ISO/IEC 15944-4 Accounting &amp; Economic Ontology — Powered by DFRNT &amp; BaseX</p>
          </footer>
        </div>
      </body>
    </html>
  </xsl:template>

  <!-- =================================================================== -->
  <!-- MAIN TRANSACTION TEMPLATE                                           -->
  <!-- =================================================================== -->
  <xsl:template match="vf:BusinessTransaction">
    <!-- BANNER DE ENCABEZADO CON SELECTOR BILINGÜE -->
    <header class="header-banner">
      <div class="header-top">
        <div class="badge-iso">ISO/IEC 15944-4 REA Ontology</div>
        <div class="lang-switch">
          <button id="btn-es" class="btn-lang active" onclick="setLanguage('es')">ES</button>
          <button id="btn-en" class="btn-lang" onclick="setLanguage('en')">EN</button>
        </div>
      </div>
      
      <h1>
        <span class="lang-es">Contrato &amp; Transacción Comercial</span>
        <span class="lang-en">Contract &amp; Business Transaction</span>
      </h1>
      
      <div class="header-meta">
        <span>
          <span class="lang-es">Transacción ID: </span>
          <span class="lang-en">Transaction ID: </span>
          <strong><xsl:value-of select="vf:transactionId"/></strong>
        </span>
        <span>
          <span class="lang-es">Fecha: </span>
          <span class="lang-en">Issue Date: </span>
          <strong><xsl:value-of select="vf:issueDate"/></strong>
        </span>
        <xsl:if test="vf:governingJurisdiction">
          <span>
            <span class="lang-es">Jurisdicción: </span>
            <span class="lang-en">Jurisdiction: </span>
            <strong><xsl:value-of select="vf:governingJurisdiction"/></strong>
          </span>
        </xsl:if>
      </div>
    </header>

    <!-- CONTRATO Y AGENTES -->
    <xsl:apply-templates select="vf:agreement"/>

    <!-- TABLA DE COMPROMISOS REA -->
    <section class="card">
      <h2 class="card-title">
        <span class="lang-es">Compromisos Económicos (Capa de Planificación REA)</span>
        <span class="lang-en">Economic Commitments (REA Planning Layer)</span>
      </h2>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>
                <span class="lang-es">ID Compromiso</span>
                <span class="lang-en">Commitment ID</span>
              </th>
              <th>
                <span class="lang-es">Acción REA</span>
                <span class="lang-en">REA Action</span>
              </th>
              <th>
                <span class="lang-es">Proveedor</span>
                <span class="lang-en">Provider</span>
              </th>
              <th>
                <span class="lang-es">Receptor</span>
                <span class="lang-en">Receiver</span>
              </th>
              <th>
                <span class="lang-es">Monto / Cantidad</span>
                <span class="lang-en">Amount / Quantity</span>
              </th>
              <th>
                <span class="lang-es">Vencimiento</span>
                <span class="lang-en">Due Date</span>
              </th>
            </tr>
          </thead>
          <tbody>
            <xsl:for-each select="vf:commitments/vf:commitment">
              <tr>
                <td><strong><xsl:value-of select="vf:id"/></strong></td>
                <td>
                  <span class="action-pill action-{vf:action}">
                    <xsl:value-of select="vf:action"/>
                  </span>
                </td>
                <td><xsl:value-of select="vf:provider"/></td>
                <td><xsl:value-of select="vf:receiver"/></td>
                <td>
                  <span class="quantity-box">
                    <xsl:value-of select="vf:resourceQuantity/vf:value"/>&#160;<xsl:value-of select="vf:resourceQuantity/vf:unitSymbol"/>
                  </span>
                </td>
                <td><xsl:value-of select="vf:due"/></td>
              </tr>
            </xsl:for-each>
          </tbody>
        </table>
      </div>
    </section>

    <!-- RECIPROCIDAD Y DUALIDAD REA -->
    <xsl:if test="vf:reciprocities/vf:reciprocity">
      <section class="card">
        <h2 class="card-title">
          <span class="lang-es">Dualidad Ontológica REA (Reciprocidad Give &amp; Take)</span>
          <span class="lang-en">REA Ontological Duality (Give &amp; Take Reciprocity)</span>
        </h2>
        <xsl:for-each select="vf:reciprocities/vf:reciprocity">
          <div class="reciprocity-box">
            <div class="reciprocity-flow">
              <span>
                <span class="lang-es">Incremento (Give):</span>
                <span class="lang-en">Increment (Give):</span>
              </span>
              <span class="chip-inc"><xsl:value-of select="vf:incrementCommitmentRef"/></span>
              <span>&#8644;</span>
              <span>
                <span class="lang-es">Decremento (Take):</span>
                <span class="lang-en">Decrement (Take):</span>
              </span>
              <span class="chip-dec"><xsl:value-of select="vf:decrementCommitmentRef"/></span>
            </div>
            <xsl:if test="vf:note">
              <div class="agent-detail"><xsl:value-of select="vf:note"/></div>
            </xsl:if>
          </div>
        </xsl:for-each>
      </section>
    </xsl:if>
  </xsl:template>

  <!-- =================================================================== -->
  <!-- AGREEMENT TEMPLATE                                                  -->
  <!-- =================================================================== -->
  <xsl:template match="vf:agreement">
    <section class="card">
      <h2 class="card-title">
        <span class="lang-es">Acuerdo Marco: </span>
        <span class="lang-en">Framework Agreement: </span>
        <xsl:value-of select="vf:name"/>
      </h2>
      <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:1.25rem;">
        <span class="lang-es">ID Contrato: </span>
        <span class="lang-en">Contract ID: </span>
        <strong><xsl:value-of select="vf:id"/></strong> 
        &#160;|&160; 
        <span class="lang-es">Fecha Creación: </span>
        <span class="lang-en">Creation Date: </span>
        <strong><xsl:value-of select="vf:created"/></strong>
      </div>

      <div class="agents-grid">
        <!-- BUYER BOX -->
        <div class="agent-box">
          <span class="agent-type-tag tag-buyer">
            <span class="lang-es">Comprador</span>
            <span class="lang-en">Buyer</span>
          </span>
          <div class="agent-name"><xsl:value-of select="vf:buyer/vf:name"/></div>
          <div class="agent-detail">ID: <xsl:value-of select="vf:buyer/vf:id"/></div>
          <xsl:if test="vf:buyer/vf:primaryLocation">
            <div class="agent-detail">
              <span class="lang-es">Ubicación: </span>
              <span class="lang-en">Location: </span>
              <xsl:value-of select="vf:buyer/vf:primaryLocation"/>
            </div>
          </xsl:if>
          <xsl:if test="vf:buyer/vf:isRelatedParty = 'true'">
            <div class="related-party-badge">
              <span class="lang-es">Parte Relacionada (NIC 24): </span>
              <span class="lang-en">Related Party (IAS 24): </span>
              <xsl:value-of select="vf:buyer/vf:relatedPartyType"/>
            </div>
          </xsl:if>
        </div>

        <!-- SELLER BOX -->
        <div class="agent-box">
          <span class="agent-type-tag tag-seller">
            <span class="lang-es">Vendedor</span>
            <span class="lang-en">Seller</span>
          </span>
          <div class="agent-name"><xsl:value-of select="vf:seller/vf:name"/></div>
          <div class="agent-detail">ID: <xsl:value-of select="vf:seller/vf:id"/></div>
          <xsl:if test="vf:seller/vf:primaryLocation">
            <div class="agent-detail">
              <span class="lang-es">Ubicación: </span>
              <span class="lang-en">Location: </span>
              <xsl:value-of select="vf:seller/vf:primaryLocation"/>
            </div>
          </xsl:if>
          <xsl:if test="vf:seller/vf:isRelatedParty = 'true'">
            <div class="related-party-badge">
              <span class="lang-es">Parte Relacionada (NIC 24): </span>
              <span class="lang-en">Related Party (IAS 24): </span>
              <xsl:value-of select="vf:seller/vf:relatedPartyType"/>
            </div>
          </xsl:if>
        </div>
      </div>
    </section>
  </xsl:template>

</xsl:stylesheet>
