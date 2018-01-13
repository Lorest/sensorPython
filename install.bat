@echo off
cls
echo Installation en cours ...
Set "URL=https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe"
set "MyDownload_Folder=python"
If Not Exist "%MyDownload_Folder%" MD "%MyDownload_Folder%"
Set "Zip=%MyDownload_Folder%\python-3.6.3.exe"
Powershell.exe -command "(New-Object System.Net.WebClient).DownloadFile('%URL%','%Zip%')"
echo Telecharger : ok
python\python-3.6.3.exe /quiet InstallAllUsers=0 SimpleInstall=1 TargetDir="%cd%\python" Shortcuts=0 Include_pip=1
python\Scripts\pip.exe install asyncio
python\Scripts\pip.exe install websockets
test.bat