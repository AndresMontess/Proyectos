$sourceFolder = "C:\Users\usuario\Pictures\sucesion"
$destinationFolder = "C:\carpeta\destino"

for ($i=1; $i -le 24; $i++) {
    $folderName = "2023-04-17 sucesion$i"
    $folderToMove = Join-Path $sourceFolder $folderName
    
    if (Test-Path $folderToMove -PathType Container) {
        Get-ChildItem $folderToMove -Filter *.jpg | Move-Item -Destination $destinationFolder
    }
}
