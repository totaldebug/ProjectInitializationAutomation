Function Create-Project{
    param(
        [Parameter(Mandatory=$true)][ValidateSet('user','org')][string]$Type="user", 
        [Parameter(Mandatory=$true)][string]$Project, 
        [string]$flag
    )

    $fields = $Project.split("{/}")

    $User = $fields[0] 
    $Project = $fields[1]

    
    python remote.py $Type $User $Project $flag

}