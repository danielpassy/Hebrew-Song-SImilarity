#script.ps1
param([String]$folderpath, [String]$otherparam)
Write-Output $folderpath
Write-Output $otherparam
wsl ls -l $folderpath $otherparam