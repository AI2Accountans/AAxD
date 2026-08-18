param(
    [Parameter(Mandatory=$true)]
    [string]$DfrntToken,
    
    [Parameter(Mandatory=$true)]
    [string]$DataProductPath, # Formato: username/data_product_name (ej: d34817fa-402c-404a-975e-c8381df4dc1d/sandbox)

    [Parameter(Mandatory=$false)]
    [string]$InstanceFile = "..\Momento0\Output\GS2XBRLGL2JSONLD.jsonld"
)

# Endpoint de DFRNT para TerminusDB (para esquemas/datos alojados)
$PathParts = $DataProductPath -split '/'
$Team = $PathParts[0]
$Db = $PathParts[1]
$Endpoint = "https://studio.dfrnt.com/api/hosted/${Team}/api/document/${Team}/${Db}"

$Headers = @{
    "Authorization" = "Token $DfrntToken"
    "Content-Type" = "application/json"
}

Write-Host "Iniciando despliegue de instancias contables hacia: $DataProductPath"
Write-Host "Endpoint: $Endpoint"

# Verificar que el archivo de instancias exista
# Intentar resolver la ruta relativa
$ResolvedPath = Resolve-Path $InstanceFile -ErrorAction SilentlyContinue
if ($null -eq $ResolvedPath) {
    # Probar con ruta relativa simple si falla
    if (Test-Path $InstanceFile) {
        $ResolvedPath = $InstanceFile
    } else {
        Write-Error "El archivo de instancias $InstanceFile no se encontró."
        exit
    }
}

# Leer el contenido de las instancias
$JsonContent = Get-Content -Path $ResolvedPath -Raw

try {
    # Hacemos un POST para insertar/actualizar las instancias
    $Uri = $Endpoint + "?author=agent&message=Cargando%20instancias%20Momento%20Cero"
    $Response = Invoke-RestMethod -Uri $Uri `
                                  -Method Post `
                                  -Headers $Headers `
                                  -Body $JsonContent

    Write-Host "¡Instancias del Momento 0 desplegadas con éxito!" -ForegroundColor Green
    $Response | ConvertTo-Json -Depth 5 | Write-Host
} catch {
    Write-Error "Error al desplegar las instancias:"
    Write-Error $_.Exception.Message
    if ($_.ErrorDetails) {
        Write-Error $_.ErrorDetails.Message
    }
}
