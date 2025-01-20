$files = Get-ChildItem -Path . -Filter 'text*.txt' | Sort-Object Name
$mergedFile = 'text_combined.txt'
Remove-Item -Path $mergedFile -ErrorAction SilentlyContinue

foreach ($file in $files) {
    Get-Content $file.FullName | Add-Content $mergedFile
}
