param(
  [string]$Root = "fastair"
)

function New-Folder($p) {
  if (-not (Test-Path $p)) { New-Item -ItemType Directory -Path $p | Out-Null }
}
function New-File($p) {
  $dir = Split-Path $p
  if ($dir) { New-Folder $dir }
  if (-not (Test-Path $p)) { New-Item -ItemType File -Path $p | Out-Null }
}

# Główne katalogi
$dirs = @(
  "$Root/app/api",
  "$Root/app/core",
  "$Root/app/db/migrations",
  "$Root/app/common",
  "$Root/app/domains/aircraft",
  "$Root/app/domains/flights",
  "$Root/app/domains/tickets",
  "$Root/app/domains/bookings",
  "$Root/app/domains/users",
  "$Root/app/tests",
  "$Root/docker"
)
$dirs | ForEach-Object { New-Folder $_ }

# Puste pliki
$files = @(
  "$Root/app/main.py",
  "$Root/app/api/routers.py",
  "$Root/app/api/deps.py",
  "$Root/app/api/errors.py",
  "$Root/app/core/config.py",
  "$Root/app/core/logging.py",
  "$Root/app/core/security.py",
  "$Root/app/db/base.py",
  "$Root/app/db/session.py",
  "$Root/app/common/dto.py",
  "$Root/app/common/utils.py",
  "$Root/app/common/events.py",
  "$Root/app/tests/conftest.py",
  "$Root/app/tests/test_health.py"
)

# Domeny – każda z zestawem plików
$domains = @("aircraft","flights","tickets","bookings","users")
foreach ($d in $domains) {
  $files += @(
    "$Root/app/domains/$d/models.py",
    "$Root/app/domains/$d/schemas.py",
    "$Root/app/domains/$d/repo.py",
    "$Root/app/domains/$d/service.py",
    "$Root/app/domains/$d/router.py"
  )
}

$files | ForEach-Object { New-File $_ }

Write-Host "✅ Struktura projektu FastAir została utworzona w: $Root"
