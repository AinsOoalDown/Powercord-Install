#Get script location
$location = Get-Location

#move to documents
Set-Location $env:USERPROFILE\Documents
Get-Package -Provider chocolatey -Force
#install dependencies
Install-Package nodejs -Force -ProviderName chocolatey
Install-Package git -Force -ProviderName chocolatey
Install-Package discord-canary -Force -ProviderName chocolatey



#download powercord
git clone https://github.com/powercord-org/powercord

Set-Location .\powercord
#install more dependencies
npm i
#run powercord
npm run plug

#install PyGithub
pip3 install PyGithub requests
#install GitPython
pip install GitPython

#Set location back to original
Set-Location $location

#Run python plugin installer
Start-Process .\Install_Plugins.py