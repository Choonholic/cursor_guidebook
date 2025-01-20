$pdfFiles = Get-ChildItem -Path . -Filter '*.pdf' | Group-Object { $_.BaseName -replace '_\d+$' }

foreach ($group in $pdfFiles) {
    $outputFile = $group.Name + '_merged.pdf'
    $inputFiles = $group.Group | Sort-Object Name | ForEach-Object { '"' + $_.FullName + '"' }

    # Use Start-Process to run pdftk with arguments
    $arguments = $inputFiles + "cat output `"$outputFile`""
    Start-Process -FilePath "pdftk" -ArgumentList $arguments -NoNewWindow -Wait
}
