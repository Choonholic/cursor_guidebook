# sys_info.txt 초기화
$outputFile = "sys_info.txt"
if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

# 로그를 파일과 화면에 동시에 출력하는 함수
function Write-Log {
    param (
        [string]$Message
    )
    Write-Host $Message
    Add-Content -Path $outputFile -Value $Message
}

# 현재 메모리 사용량과 전체 메모리 용량
$memoryInfo = Get-CimInstance Win32_OperatingSystem
$currentMemoryUsage = $memoryInfo.TotalVisibleMemorySize - $memoryInfo.FreePhysicalMemory
$totalMemory = $memoryInfo.TotalVisibleMemorySize

Write-Log "메모리 정보:"
Write-Log "현재 메모리 사용량: $([math]::Round($currentMemoryUsage / 1MB, 2)) MB"
Write-Log "전체 메모리 용량: $([math]::Round($totalMemory / 1MB, 2)) MB"
Write-Log ""

# 시스템 드라이브 사용량과 전체 크기
$systemDrive = Get-PSDrive -Name (Get-PSDrive | Where-Object { $_.Root -eq 'C:\' }).Name
Write-Log "시스템 드라이브 정보:"
Write-Log "사용량: $([math]::Round($systemDrive.Used / 1GB, 2)) GB"
Write-Log "전체 크기: $([math]::Round($systemDrive.Used / 1GB + $systemDrive.Free / 1GB, 2)) GB"
Write-Log ""

# IP 주소
$ipAddresses = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notlike "169.254.*" }).IPAddress
Write-Log "IP 주소:"
if ($ipAddresses) {
    $ipAddresses | ForEach-Object { Write-Log "- $_" }
} else {
    Write-Log "IP 주소를 찾을 수 없습니다."
}
Write-Log ""

# DNS 주소 (IPv4만 표시)
$dnsAddresses = Get-DnsClientServerAddress | Select-Object -ExpandProperty ServerAddresses | Where-Object { $_ -match "^\d{1,3}(\.\d{1,3}){3}$" }
Write-Log "DNS 주소 (IPv4):"
if ($dnsAddresses) {
    $dnsAddresses | ForEach-Object { Write-Log "- $_" }
} else {
    Write-Log "IPv4 DNS 주소를 찾을 수 없습니다."
}
Write-Host ""

# 화면에만 출력
Write-Host "정보가 'sys_info.txt'에 저장되었습니다."
