<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:fo="http://www.w3.org/1999/XSL/Format"
                xmlns:vf="https://w3id.org/valueflows/ont/vf#">

  <xsl:output method="xml" indent="yes" encoding="UTF-8"/>

  <!-- =================================================================== -->
  <!-- CONFIGURACIÓN DE PÁGINA XSL-FO PARA PDF                             -->
  <!-- =================================================================== -->
  <xsl:template match="/">
    <fo:root>
      <fo:layout-master-set>
        <fo:simple-page-master master-name="A4-Portrait"
                               page-height="29.7cm"
                               page-width="21.0cm"
                               margin-top="2.0cm"
                               margin-bottom="2.0cm"
                               margin-left="2.0cm"
                               margin-right="2.0cm">
          <fo:region-body margin-top="1.5cm" margin-bottom="1.5cm"/>
          <fo:region-before extent="1.2cm"/>
          <fo:region-after extent="1.0cm"/>
        </fo:simple-page-master>
      </fo:layout-master-set>

      <fo:page-sequence master-reference="A4-Portrait">
        
        <!-- ENCABEZADO SUPERIOR -->
        <fo:static-content flow-name="xsl-region-before">
          <fo:block font-family="Helvetica, Arial, sans-serif" font-size="8pt" color="#64748B" text-align="right" border-bottom="0.5pt solid #CBD5E1" padding-bottom="4pt">
            ISO/IEC 15944-4: Accounting &amp; Economic Ontology — Smart Contract Ledger
          </fo:block>
        </fo:static-content>

        <!-- PIE DE PÁGINA -->
        <fo:static-content flow-name="xsl-region-after">
          <fo:block font-family="Helvetica, Arial, sans-serif" font-size="8pt" color="#94A3B8" text-align="center">
            Página <fo:page-number/> | Documento Validado bajo Esquema XSD REA / Valueflows
          </fo:block>
        </fo:static-content>

        <!-- CUERPO PRINCIPAL -->
        <fo:flow flow-name="xsl-region-body">
          <xsl:apply-templates select="vf:BusinessTransaction"/>
        </fo:flow>
      </fo:page-sequence>
    </fo:root>
  </xsl:template>

  <!-- =================================================================== -->
  <!-- PLANTILLA PRINCIPAL: TRANSACTION & AGREEMENT                        -->
  <!-- =================================================================== -->
  <xsl:template match="vf:BusinessTransaction">
    <!-- Título Principal -->
    <fo:block font-family="Helvetica, Arial, sans-serif" font-size="18pt" font-weight="bold" color="#1E3A8A" space-after="6pt">
      Acuerdo Comercial ISO/IEC 15944-4
    </fo:block>

    <!-- Subtítulo e Información del Registro -->
    <fo:block font-family="Helvetica, Arial, sans-serif" font-size="10pt" color="#475569" space-after="15pt" border-bottom="2pt solid #1E3A8A" padding-bottom="6pt">
      Transacción ID: <fo:inline font-weight="bold" color="#0F172A"><xsl:value-of select="vf:transactionId"/></fo:inline>
      &#160;|&#160; Emisión: <fo:inline font-weight="bold"><xsl:value-of select="vf:issueDate"/></fo:inline>
    </fo:block>

    <!-- Caja de Jurisdicción -->
    <xsl:if test="vf:governingJurisdiction">
      <fo:block font-family="Helvetica, Arial, sans-serif" font-size="9pt" background-color="#F1F5F9" padding="8pt" border-left="3pt solid #3B82F6" space-after="15pt">
        <fo:inline font-weight="bold" color="#1E293B">Jurisdicción Aplicable: </fo:inline>
        <xsl:value-of select="vf:governingJurisdiction"/>
      </fo:block>
    </xsl:if>

    <!-- Datos del Acuerdo (Agreement) -->
    <xsl:apply-templates select="vf:agreement"/>

    <!-- Compromisos REA (Commitments Table) -->
    <fo:block font-family="Helvetica, Arial, sans-serif" font-size="12pt" font-weight="bold" color="#1E3A8A" space-before="15pt" space-after="8pt">
      Compromisos Económicos (REA Commitments Layer)
    </fo:block>

    <xsl:choose>
      <xsl:when test="vf:commitments/vf:commitment">
        <fo:table table-layout="fixed" width="100%" border-collapse="collapse" space-after="15pt">
          <fo:table-column column-width="20%"/>
          <fo:table-column column-width="15%"/>
          <fo:table-column column-width="20%"/>
          <fo:table-column column-width="20%"/>
          <fo:table-column column-width="10%"/>
          <fo:table-column column-width="15%"/>

          <!-- Encabezado de la Tabla -->
          <fo:table-header background-color="#1E3A8A" color="#FFFFFF" font-family="Helvetica, Arial, sans-serif" font-size="9pt" font-weight="bold">
            <fo:table-row text-align="center">
              <fo:table-cell padding="5pt" border="0.5pt solid #1E3A8A"><fo:block>ID Compromiso</fo:block></fo:table-cell>
              <fo:table-cell padding="5pt" border="0.5pt solid #1E3A8A"><fo:block>Acción REA</fo:block></fo:table-cell>
              <fo:table-cell padding="5pt" border="0.5pt solid #1E3A8A"><fo:block>Proveedor</fo:block></fo:table-cell>
              <fo:table-cell padding="5pt" border="0.5pt solid #1E3A8A"><fo:block>Receptor</fo:block></fo:table-cell>
              <fo:table-cell padding="5pt" border="0.5pt solid #1E3A8A"><fo:block>Cantidad</fo:block></fo:table-cell>
              <fo:table-cell padding="5pt" border="0.5pt solid #1E3A8A"><fo:block>Vencimiento</fo:block></fo:table-cell>
            </fo:table-row>
          </fo:table-header>

          <!-- Filas de la Tabla -->
          <fo:table-body font-family="Helvetica, Arial, sans-serif" font-size="8.5pt">
            <xsl:for-each select="vf:commitments/vf:commitment">
              <fo:table-row>
                <xsl:attribute name="background-color">
                  <xsl:choose>
                    <xsl:when test="position() mod 2 = 0">#F8FAFC</xsl:when>
                    <xsl:otherwise>#FFFFFF</xsl:otherwise>
                  </xsl:choose>
                </xsl:attribute>
                
                <fo:table-cell padding="4pt" border="0.5pt solid #CBD5E1"><fo:block font-weight="bold"><xsl:value-of select="vf:id"/></fo:block></fo:table-cell>
                <fo:table-cell padding="4pt" border="0.5pt solid #CBD5E1" text-align="center">
                  <fo:block color="#0284C7" font-weight="bold"><xsl:value-of select="vf:action"/></fo:block>
                </fo:table-cell>
                <fo:table-cell padding="4pt" border="0.5pt solid #CBD5E1"><fo:block><xsl:value-of select="vf:provider"/></fo:block></fo:table-cell>
                <fo:table-cell padding="4pt" border="0.5pt solid #CBD5E1"><fo:block><xsl:value-of select="vf:receiver"/></fo:block></fo:table-cell>
                <fo:table-cell padding="4pt" border="0.5pt solid #CBD5E1" text-align="right">
                  <fo:block font-weight="bold">
                    <xsl:value-of select="vf:resourceQuantity/vf:value"/>&#160;<xsl:value-of select="vf:resourceQuantity/vf:unitSymbol"/>
                  </fo:block>
                </fo:table-cell>
                <fo:table-cell padding="4pt" border="0.5pt solid #CBD5E1" text-align="center"><fo:block color="#475569"><xsl:value-of select="vf:due"/></fo:block></fo:table-cell>
              </fo:table-row>
            </xsl:for-each>
          </fo:table-body>
        </fo:table>
      </xsl:when>
      <xsl:otherwise>
        <fo:block font-family="Helvetica, Arial, sans-serif" font-size="9pt" color="#64748B" font-style="italic" space-after="10pt">
          No hay compromisos registrados en esta transacción.
        </fo:block>
      </xsl:otherwise>
    </xsl:choose>

    <!-- Reciprocidad y Dualidad REA -->
    <xsl:if test="vf:reciprocities/vf:reciprocity">
      <fo:block font-family="Helvetica, Arial, sans-serif" font-size="11pt" font-weight="bold" color="#0F172A" space-before="10pt" space-after="6pt">
        Dualidad Ontológica REA (Reciprocidad Give &amp; Take)
      </fo:block>
      <xsl:for-each select="vf:reciprocities/vf:reciprocity">
        <fo:block font-family="Helvetica, Arial, sans-serif" font-size="8.5pt" background-color="#EFF6FF" padding="6pt" border-left="3pt solid #2563EB" space-after="6pt">
          <fo:inline font-weight="bold">Vínculo de Dualidad: </fo:inline>
          Incremento [<fo:inline color="#16A34A" font-weight="bold"><xsl:value-of select="vf:incrementCommitmentRef"/></fo:inline>]
          &#160;&#8644;&#160;
          Decremento [<fo:inline color="#DC2626" font-weight="bold"><xsl:value-of select="vf:decrementCommitmentRef"/></fo:inline>]
          <xsl:if test="vf:note">
            &#10;| <xsl:value-of select="vf:note"/>
          </xsl:if>
        </fo:block>
      </xsl:for-each>
    </xsl:if>
  </xsl:template>

  <!-- =================================================================== -->
  <!-- PLANTILLA DE AGENTES Y CONTRATO                                     -->
  <!-- =================================================================== -->
  <xsl:template match="vf:agreement">
    <fo:block font-family="Helvetica, Arial, sans-serif" font-size="11pt" font-weight="bold" color="#0F172A" space-after="4pt">
      Contrato: <xsl:value-of select="vf:name"/>
    </fo:block>
    <fo:block font-family="Helvetica, Arial, sans-serif" font-size="9pt" color="#64748B" space-after="10pt">
      ID Contrato: <xsl:value-of select="vf:id"/> &#160;|&#160; Fecha Creación: <xsl:value-of select="vf:created"/>
    </fo:block>

    <!-- Tabla de Agentes (Comprador vs Vendedor) -->
    <fo:table table-layout="fixed" width="100%" space-after="15pt">
      <fo:table-column column-width="50%"/>
      <fo:table-column column-width="50%"/>
      <fo:table-body font-family="Helvetica, Arial, sans-serif" font-size="9pt">
        <fo:table-row>
          <fo:table-cell padding="8pt" background-color="#F8FAFC" border="0.5pt solid #E2E8F0">
            <fo:block font-weight="bold" color="#1E3A8A" space-after="4pt">AGENTE COMPRADOR (BUYER)</fo:block>
            <fo:block font-weight="bold" color="#0F172A"><xsl:value-of select="vf:buyer/vf:name"/></fo:block>
            <fo:block color="#64748B">ID: <xsl:value-of select="vf:buyer/vf:id"/></fo:block>
            <xsl:if test="vf:buyer/vf:primaryLocation">
              <fo:block color="#64748B">Ubicación: <xsl:value-of select="vf:buyer/vf:primaryLocation"/></fo:block>
            </xsl:if>
          </fo:table-cell>

          <fo:table-cell padding="8pt" background-color="#F8FAFC" border="0.5pt solid #E2E8F0">
            <fo:block font-weight="bold" color="#1E3A8A" space-after="4pt">AGENTE VENDEDOR (SELLER)</fo:block>
            <fo:block font-weight="bold" color="#0F172A"><xsl:value-of select="vf:seller/vf:name"/></fo:block>
            <fo:block color="#64748B">ID: <xsl:value-of select="vf:seller/vf:id"/></fo:block>
            <xsl:if test="vf:seller/vf:primaryLocation">
              <fo:block color="#64748B">Ubicación: <xsl:value-of select="vf:seller/vf:primaryLocation"/></fo:block>
            </xsl:if>
          </fo:table-cell>
        </fo:table-row>
      </fo:table-body>
    </fo:table>
  </xsl:template>

</xsl:stylesheet>
