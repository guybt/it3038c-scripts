function getIP{
    (get-netipaddress).ipv4address | Select-String "10.*"
}

$IP = getIP

$User = $env:UserName

$Hostname = $env:computername

$Version = $HOST.Version.Major

$Date = Get-Date -UFormat "%A, %B %d %Y"

$BODY = "This machine's IP is $IP. User is $User. Hostname is $Hostname. Powershell Version is $Version. Today's Date is $Date"

Send-MailMessage -To "guybt@mail.uc.edu" -From "guybt@mail.uc.edu" -Subject "Braiden Guy IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential)
