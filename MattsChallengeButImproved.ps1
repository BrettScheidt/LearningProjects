param( [string] $folder,[string] $file1,[string]$file2)
Get-Module -Name Microsoft.PowerShell.Management

function run
{
param( [string] $folder,[string] $file1,[string]$file2)

    if($folder -eq $null -or $folder -eq "  " -or $folder -eq "")
    {
        $folder = "C:\MattScript"
    }
    if($file1 -eq $null -or $file1 -eq "  "-or $file1 -eq "")
    {
        $file1="$folder\file1.txt"
    }
    if($file2 -eq $null -or $file2 -eq "  "-or $file2 -eq "")
    {
        $file2="$folder\file2.txt"
    }
    $logfile="$folder\log.txt"
    Write-Output "$folder       $file1          $file2"
    verifyLocationFolder($folder)
    verifyLocationFiles "$file1" "$file2"
    clearLog($logfile)
    comparefiles "$file1" "$file2" "$logfile"
    $pattern = Read-Host -Prompt "What pattern to find"
    findPattern "$file1" "$pattern"
    findPattern "$file2" "$pattern"
}

function verifyLocationFolder
{
param([string] $location)
    if(Test-Path -Path $location -PathType Container)
    {
        Write-Output "Folder Exists"
    }
    else
    {
        New-Item -Path $folder -ItemType Directory
        Write-Output "Folder Does not Exist, Making folder"
    }
}
function verifyLocationFiles
{
param([string] $file1, [string] $file2)
if((Test-Path -Path $file1 -PathType Leaf) -and (Test-Path -Path $file2 -PathType Leaf))
{
    Write-Output "File and file2 exist"
}
elseif((Test-Path -Path $file1 -PathType Leaf) -and !(Test-Path -Path $file2 -PathType Leaf))
{
    Copy-Item -Path $file1 -Destination $file2
    Write-Output "Back up did not exist, backup made"
}
elseif((Test-Path -Path $file2 -PathType Leaf) -and !(Test-Path -Path $file1 -PathType Leaf))
{
    Copy-Item -Path $file2 -Destination $file1
    Write-Output "Orginal File missing recovering from backup"
}
else
{
    Write-Output "Neither File Exists, making files"
    New-Item -Path $file1 -ItemType File
    "Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos." | Out-File -FilePath $file1
    "Blicke gesehen, und möcht' ich nun deinen so oft entweihten Namen nie wieder nennen hören! Am 19. Junius Wo ich neulich mit meiner Tänzerin und." | Out-File -FilePath $file1 -Append
    Copy-Item -path $file1 -Destination $file2
}
}
function clearLog
{
param([string] $logfile)
    if(Test-Path -Path $logfile -PathType Leaf)
    {
        Remove-Item -Path $logfile
    }
    New-Item -Path $logfile -ItemType File
}
function comparefiles
{
param([string] $file1, [string] $file2, [string] $logfile)
    $file1Content = Get-Content -Path $file1
    $file2Content = Get-Content -Path $file2

    $fileCount = (Get-Content -Path $file1).Length
    $file2Count =(Get-Content -Path $file2).Length

    for($count =0;$count -lt $file2Count; $count++)
    {
    
    $file2line =$file2Content[$count]
    $exists = $false
        for($count1=0;$count1 -lt $fileCount;$Count1++)
        {
            $fileline = $file1Content[$count1]
        
            if($fileline -eq $file2line)
            {
                $exists=$true
                if($fileline -cne $file2line)
                {
                    $temp=$count+1
                    "Case Change on line $temp" | Out-File -FilePath $logfile -Append  
                }
                continue
            }
            if($exists -eq $false -and $count1 -eq ($fileCount -1))
            {
                $temp=$count+1
                "File2 Line $temp was removed that contained content of $file2line" | Out-File -FilePath $logfile -Append  
            }
        }
    }

    for($count =0;$count -lt $fileCount; $count++)
    {
        $fileline =$file1Content[$count]
        $exists= $false
        for($count1=0;$count1 -lt $file2Count;$count1++)
        {
            $file2line = $file2Content[$count1]
            if($fileline -eq $file2line)
            {
                $exists=$true
                continue
            }
            if(!$exists -and $count1 -eq ($file2count -1))
            {
                $temp=$count+1
                "File1 Line $temp was add with the following content $fileline" | Out-File -FilePath $logfile -Append    
            }
        }
    }
}
function findPattern
{
param([string]$file,[string]$pattern)

    $fileCount = (Get-Content -Path $file).Length
    $fileContent = Get-Content -Path $file
    for($x =0;$x -lt $fileCount; $x++)
    {
        $fileline =$fileContent[$x]
        if($fileline -like "*$pattern*")
        {
            $temp = $x+1
            "Line $temp on current contains pattern on file $file" | Out-File -FilePath $logfile -Append

        }
    }
}

run($folder,$file1,$file2)