Function Create-Project{
    param(
        [Parameter(Mandatory=$true)][ValidateSet('user','org')][string]$Type="user", 
        [Parameter(Mandatory=$true)][string]$Project, 
        [switch]$Local
    )

    $fields = $Project.split("{/}")

    $User = $fields[0] 
    $Project = $fields[1]

    if($Local){
        python create_project.py $Type $User $Project $Local
    }else{
        python create_project.py $Type $User $Project
    }
}