# Self-elevate the script if required
#if (-Not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')) {
#    if ([int](Get-CimInstance -Class Win32_OperatingSystem | Select-Object -ExpandProperty BuildNumber) -ge 6000) {
#     $CommandLine = "-File `"" + $MyInvocation.MyCommand.Path + "`" " + $MyInvocation.UnboundArguments
#     Start-Process -FilePath PowerShell.exe -Verb Runas -ArgumentList $CommandLine
#     Exit
#    }
#   }
#
Set-Location $env:USERPROFILE\Documents
Get-Package -Provider chocolatey -Force
Install-Package nodejs npm git discord-canary -Force -ProviderName chocolatey
git clone https://github.com/powercord-org/powercord
Set-Location .\powercord
npm i
npm run plug
