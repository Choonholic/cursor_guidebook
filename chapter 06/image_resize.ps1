$files = Get-ChildItem -Path . -Filter *.png
New-Item -ItemType Directory -Path resized -Force

foreach ($file in $files) {
    $fileName = [System.IO.Path]::GetFileNameWithoutExtension($file)
    & magick $file.FullName -resize 512x512 "resized/${fileName}_512.png"
    & magick $file.FullName -resize 256x256 "resized/${fileName}_256.png"
    & magick $file.FullName -resize 128x128 "resized/${fileName}_128.png"
}
