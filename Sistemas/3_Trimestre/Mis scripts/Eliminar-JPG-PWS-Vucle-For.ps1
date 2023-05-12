$folderPath = "C:\Users\usuario\Pictures\Escritura Isla Cristina"

for ($i=1; $i -le 6; $i++) {
    $folderName = "2023-04-17 escrituraic$i"
    $folderToDelete = Join-Path $folderPath $folderName
    
    if (Test-Path $folderToDelete -PathType Container) {
        Remove-Item $folderToDelete -Recurse -Force
    }
}
