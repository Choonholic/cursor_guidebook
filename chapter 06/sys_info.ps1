# 현재 메모리 사용량과 전체 메모리 용량
$memoryInfo = Get-CimInstance Win32_OperatingSystem
$currentMemoryUsage = $memoryInfo.TotalVisibleMemorySize - $memoryInfo.FreePhysicalMemory
$totalMemory = $memoryInfo.TotalVisibleMemorySize

Write-Host "메모리 정보:"
Write-Host "현재 메모리 사용량: $([math]::Round($currentMemoryUsage / 1MB, 2)) MB"
Write-Host "전체 메모리 용량: $([math]::Round($totalMemory / 1MB, 2)) MB"
Write-Host ""

# 시스템 드라이브 사용량과 전체 크기
$systemDrive = Get-PSDrive -Name (Get-PSDrive | Where-Object { $_.Root -eq 'C:\' }).Name
Write-Host "시스템 드라이브 정보:"
Write-Host "사용량: $([math]::Round($systemDrive.Used / 1GB, 2)) GB"
Write-Host "전체 크기: $([math]::Round($systemDrive.Used / 1GB + $systemDrive.Free / 1GB, 2)) GB"
Write-Host ""

# IP 주소
$ipAddresses = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike "169.254.*" }).IPAddress
Write-Host "IP 주소:"
if ($ipAddresses) {
    $ipAddresses | ForEach-Object { Write-Host "- $_" }
} else {
    Write-Host "IP 주소를 찾을 수 없습니다."
}
Write-Host ""

# DNS 주소 (IPv4만 표시)
$dnsAddresses = Get-DnsClientServerAddress | Select-Object -ExpandProperty ServerAddresses | Where-Object { $_ -match "^\d{1,3}(\.\d{1,3}){3}$" }
Write-Host "DNS 주소 (IPv4):"
if ($dnsAddresses) {
    $dnsAddresses | ForEach-Object { Write-Host "- $_" }
} else {
    Write-Host "IPv4 DNS 주소를 찾을 수 없습니다."
}
