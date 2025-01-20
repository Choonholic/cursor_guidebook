Get-ChildItem -Path . -Filter *.png
New-Item -ItemType Directory -Path converted -Force

foreach ($file in $files) {
    $fileName = [System.IO.Path]::GetFileNameWithoutExtension($file)
    & magick $file.FullName -format webp "converted/$fileName.webp"
}
