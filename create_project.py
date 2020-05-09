import sys
import os
from github import Github

Type = str(sys.argv[1])
UserName = str(sys.argv[2])
ProjectFolder = str(sys.argv[3])
path = os.environ.get("mp")  # add projects dirctory to the env vars
token = os.environ.get("gt")  # add github token to the env vars
_dir = path + "/" + ProjectFolder

Flag = False
if len(sys.argv) == 5:
    Flag = bool(sys.argv[4])

g = Github(token)


def orgRepo():
    org = g.get_organization(UserName)
    try:
        org.get_repo(ProjectFolder)
    except:
        repo = org.create_repo(ProjectFolder)
        print(repo)
    else:
        print(f"Repo {UserName}/{ProjectFolder} already exists cloning")


def userRepo():
    user = g.get_user()
    user.login
    try:
        user.get_repo(ProjectFolder)
    except:
        repo = user.create_repo(ProjectFolder)
        print(repo)
    else:
        print(f"Repo {UserName}/{ProjectFolder} already exists cloning")


def cloneRepo():
    os.chdir(path)
    Clone = os.system(f"git clone git@github.com:{UserName}/{ProjectFolder}.git")
    print(Clone)
    os.chdir(_dir)
    commands = [
        f"@echo # {ProjectFolder}>> README.md",
        "git add .",
        'git commit -m "Initial commit"',
        "git push -u origin master",
    ]

    for c in commands:
        os.system(c)

    print(f"{UserName}/{ProjectFolder} cloned")

    return os.system("code .")


if Flag:
    try:
        os.mkdir(_dir)
        os.chdir(_dir)
        os.system("git init")
        os.system(f'echo "# {ProjectFolder}" > README.md')
        os.system("git add README.md")
        os.system('git commit -m "first commit"')

        print(f"{ProjectFolder} created locally")
        os.system("code .")

    except:
        print("create <project_name> -Local")

else:
    if Type == "org":
        orgRepo()
        cloneRepo()

    elif Type == "user":
        userRepo()
        cloneRepo()
    else:
        print("Command: create -Type <user/org> -Project <userorg>/<ProjectFolder>")
