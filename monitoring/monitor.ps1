# Monitoring Script (PowerShell)
# This script collects system metrics and inserts them into a SQL Server database.

# Collect system metrics
date = Get-Date
$cpu = Get-WmiObject Win32_Processor | Measure-Object LoadPercentage -Average | Select-Object -ExpandProperty Average
$mem = (Get-WmiObject Win32_OperatingSystem).FreePhysicalMemory

# Insert into SQL Server
Invoke-Sqlcmd -ServerInstance "localhost" -Database "PoC_DB" -Query \
"INSERT INTO HealthMetrics (Timestamp, CPU, FreeMemory)
 VALUES ('$date', $cpu, $mem)"
Write-Output "Metrics recorded at $date"