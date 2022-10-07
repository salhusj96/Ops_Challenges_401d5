Set-ADDefaultDomainPasswordPolicy -ComplexityEnabled $True -MinPasswordLength 14
Set-SmbServerConfiguration -EnableSMB1Protocol $false