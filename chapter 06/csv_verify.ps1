# CSV 파일 경로
$filePath = "data.csv"

# 필수 열 인덱스 정의 (0부터 시작)
$requiredColumns = @(0, 2, 4) # 첫 번째, 세 번째, 다섯 번째 열

# 데이터 검증 함수
function Test-CSV {
    param (
        [string]$Path
    )

    if (-Not (Test-Path $Path)) {
        Write-Host "파일이 존재하지 않습니다: $Path"
        return
    }

    $csvData = Import-Csv -Path $Path
    if ($csvData.Count -eq 0) {
        Write-Host "CSV 파일이 비어 있습니다."
        return
    }

    # 첫 번째 행의 머리글 확인
    $header = (Get-Content -Path $Path -First 1).Split(',')
    $expectedColumnCount = $header.Length
    Write-Host "머리글 열 개수: $expectedColumnCount"

    $rowNumber = 1 # 머리글을 제외한 데이터 행 번호
    foreach ($row in $csvData) {
        $rowNumber++
        $errors = @()
        $warnings = @()

        # 열 개수 검증
        $columns = $row.PSObject.Properties.Name
        if ($columns.Count -ne $expectedColumnCount) {
            $errors += "열 개수 부족 (기대: $expectedColumnCount, 실제: $($columns.Count))"
        }

        # 필수 열 비어 있는지 확인
        foreach ($colIndex in $requiredColumns) {
            $colName = $header[$colIndex]
            if (-Not $row.$colName) {
                $errors += "필수 열 ($colName)이 비어 있음"
            }
        }

        # 데이터 형식 검증
        # 두 번째 열: 정수 형식
        $intColumn = $header[1]
        if ($row.$intColumn -and -Not ([int]::TryParse($row.$intColumn, [ref]0))) {
            $errors += "정수 열 ($intColumn)이 정수 형식이 아님"
        }

        # 네 번째 열: YYYY-MM-DD 날짜 형식
        $dateColumn = $header[3]
        if ($row.$dateColumn -and -Not ($row.$dateColumn -match "^\d{4}-\d{2}-\d{2}$")) {
            $errors += "날짜 열 ($dateColumn)이 YYYY-MM-DD 형식이 아님"
        }

        # 여섯 번째 열: 문자열 형식 (0으로 시작하지 않아야 함)
        $stringColumn = $header[5]
        if ($row.$stringColumn -and $row.$stringColumn -match "^0") {
            $warnings += "문자열 열 ($stringColumn)이 0으로 시작 (경고)"
        }

        # 결과 출력
        if ($errors.Count -gt 0) {
            Write-Host "행 $rowNumber 오류: $($errors -join ', ')"
        }
        if ($warnings.Count -gt 0) {
            Write-Host "행 $rowNumber 경고: $($warnings -join ', ')"
        }
    }

    Write-Host "CSV 검증 완료."
}

# 실행
Test-CSV -Path $filePath
