#Self-elevate the script if required
#if (-Not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
#    if ([int](Get-CimInstance -Class Win32_OperatingSystem | Select-Object -ExpandProperty BuildNumber) -ge 6000) {
#     $CommandLine = "-File `"" + $MyInvocation.MyCommand.Path + "`" " + $MyInvocation.UnboundArguments
#     Start-Process -FilePath PowerShell.exe -Verb Runas -ArgumentList $CommandLine
#     Exit
#    }
#   }
#move to documents
Set-Location $env:USERPROFILE\Documents
Get-Package -Provider chocolatey -Force
#install dependencies
Install-Package nodejs git discord-canary -Force -ProviderName chocolatey

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
#install plugins
.\Install_Plugins.py