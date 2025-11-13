Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Install-PackageProvider -Name NuGet -Force
Install-Module PowershellGet -Force
Install-Module -Name PSWindowsUpdate -Force

$folder = "C:\IHDTemp"

$name = $env:COMPUTERNAME
$time = (Get-Date).toString("MM-dd-yyyy")
$filex = "C:\IHDTemp\Update$name+$time.log"

$global:UpdateName = "KB5068861"
$CurrentVersion = 7171
#Reduce the Extra files in the IHD Temp foler
if (Test-Path $folder)
{
    $files = Get-ChildItem -Path $folder
    foreach ($file in $files)
    {
        try
        {
            Remove-Item -Path $file.FullName -Force
            Write-Host "Deleted file: $($file.FullName)"
        }
        catch
        {
            Write-Host "failed to delete: $($file.FullName)"
        }
    }
}
else
{
    Write-Host "Folder not found"
}

#updates windows and does not force update right awya
Get-WindowsUpdate -Install -AcceptAll -IgnoreReboot | Out-File "$filex" -Force



#This is to get the full version of windows so we can identify 24h2 vs 25h2 and if it is on this months version
function Get-FullWindowsVersion {
    # Get registry info
    $reg = Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"
    $productName = $reg.ProductName
    # Some systems have a “DisplayVersion” (e.g. “22H2”, etc.)
    $displayVersion = $null
    if ($reg.PSObject.Properties.Name -contains "DisplayVersion") {
        $displayVersion = $reg.DisplayVersion
    }
    # Fallback: sometimes “ReleaseId” is used (older Windows 10 versions) :contentReference[oaicite:0]{index=0}
    if (-not $displayVersion -and ($reg.PSObject.Properties.Name -contains "ReleaseId")) {
        $displayVersion = $reg.ReleaseId
    }
    $build = $reg.CurrentBuild
    # Windows also has an "UBR" (Update Build Revision) for minor patches :contentReference[oaicite:1]{index=1}
    $ubr = 0
    try {
        $ubr = (Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" -Name UBR -ErrorAction Stop).UBR
    } catch {
        # If UBR not present, ignore
    }

    # Compose a descriptive version string
    # Example: "Windows 11 Pro 24H2 (Build 26000.1234)"
    $parts = @()
    if ($productName) { $parts += $productName }
    if ($displayVersion) { $parts += $displayVersion }
    if ($build) {
        if ($ubr -gt 0) {
            $parts += "Build $build.$ubr"
        } else {
            $parts += "Build $build"
        }
    }
    $versionString = $parts -join " "
    return $versionString
}

# Main
$fullVersion = Get-FullWindowsVersion

# Replace characters invalid in file names
# E.g. remove or replace : * ? " < > | \ / etc.
$cleanName = $fullVersion -replace '[:\\\/\*\?"<>\|]', '_'


function isUpdated([string]$UFile)
{
        $fileCount = (Get-Content -Path $UFile).Length
        if($filecount -ne 0)
        {
            for($x =0;$x -lt $fileCount; $x++)
            {
                $fileline =$fileContent[$x]
                if($fileline -like "*$UpdateName*")
                {
                    Write-Output("$fileline")
                    return $true
                }
               
            }
        }
        else {
            return $false
        }  
            return $false
}


$test = isUpdated($filex)


#This 
if(!$test){
    if($cleanName.Contains("24H2") -and !$cleanName.Contains($Currentversion)){
        $updateFile2 = "https://catalog.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/d8b7f92b-bd35-4b4c-96e5-46ce984b31e0/public/windows11.0-kb5043080-x64_953449672073f8fb99badb4cc6d5d7849b9c83e8.msu"
        $updateFile= "https://catalog.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/5315757b-0dc6-4282-a148-c7bf0b6b0e90/public/windows11.0-kb5068861-x64_acc4fe9c928835c0d44cdc0419d1867dbd2b62b2.msu"
        $Folder = "C:\IHDTemp"
        $updatePath= "$Folder\$time.msu"
        $updatePath2= "$Folder\$time.msu"

        $client = New-Object System.Net.WebClient  
        $client.DownloadFile($updateFile, $updatePath)
        $client2 = New-Object System.Net.WebClient  
        $client2.DownloadFile($updateFile2, $updatePath2)

        $updatePathAug = "$Folder\$time.msu /quiet /norestart"
        $updatePathAug2 = "$Folder\$time.msu /quiet /norestart"
        Start-Process -FilePath "wusa.exe" -ArgumentList $updatePathAug -Wait
        Start-Process -FilePath "wusa.exe" -ArgumentList $updatePathAug2 -Wait
    }
    elseif($cleanName.Contains("25H2") -and !$cleanName.Contains($Currentversion)){
        $updateFile = "https://catalog.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/5315757b-0dc6-4282-a148-c7bf0b6b0e90/public/windows11.0-kb5068861-x64_acc4fe9c928835c0d44cdc0419d1867dbd2b62b2.msu"
        $updateFile2= "https://catalog.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/d8b7f92b-bd35-4b4c-96e5-46ce984b31e0/public/windows11.0-kb5043080-x64_953449672073f8fb99badb4cc6d5d7849b9c83e8.msu"
        $Folder = "C:\IHDTemp"
        $updatePath= "$Folder\$time.msu"
        $updatePath2= "$Folder\$time.msu"


        $client = New-Object System.Net.WebClient  
        $client.DownloadFile($updateFile, $updatePath)
        $client2 = New-Object System.Net.WebClient  
        $client2.DownloadFile($updateFile2, $updatePath2)
        $updatePathAug = "$Folder\$time.msu /quiet /norestart"
        $updatePathAug2 = "$Folder\$time.msu /quiet /norestart"
        Start-Process -FilePath "wusa.exe" -ArgumentList $updatePathAug -Wait
        Start-Process -FilePath "wusa.exe" -ArgumentList $updatePathAug2 -Wait
    }
    else {
        Write-Output("Fully Updated, update log does not exist or device had no update at request time")
    }
}
else{
    Write-Output("Fully Updated, No MSI download required")

}
