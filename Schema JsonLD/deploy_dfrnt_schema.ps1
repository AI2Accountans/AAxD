param(
    [Parameter(Mandatory=$true)]
    [string]$DfrntToken,
    
    [Parameter(Mandatory=$true)]
    [string]$DataProductPath, # Formato: username/data_product_name (ej: iphix/atlas_empresarial)

    [Parameter(Mandatory=$false)]
    [string]$SchemaFile = ".\merged_schema_zachman_dfrnt.json"
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

Write-Host "Iniciando despliegue del esquema hacia: $DataProductPath"
Write-Host "Endpoint: $Endpoint"

if (-not (Test-Path $SchemaFile)) {
    Write-Error "El archivo de esquema $SchemaFile no se encontro."
    exit
}

# Leer el contenido del esquema
$JsonContent = Get-Content -Path $SchemaFile -Raw

try {
    # Hacemos un POST/PUT para actualizar el esquema (graph_type=schema)
    $Uri = $Endpoint + "?graph_type=schema&author=agent&message=Actualizando%20esquema%20Sunder%20Zachman"
    $Response = Invoke-RestMethod -Uri $Uri `
                                  -Method Post `
                                  -Headers $Headers `
                                  -Body $JsonContent

    Write-Host "¡Esquema desplegado con exito!" -ForegroundColor Green
    $Response | ConvertTo-Json -Depth 5 | Write-Host
} catch {
    Write-Error "Error al desplegar el esquema:"
    Write-Error $_.Exception.Message
    if ($_.ErrorDetails) {
        Write-Error $_.ErrorDetails.Message
    }
}
