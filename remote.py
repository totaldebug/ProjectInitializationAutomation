import sys
import os
from github import Github

Type = str(sys.argv[1])
UserName = str(sys.argv[2])
ProjectFolder = str(sys.argv[3])
path = os.environ.get('mp')         # add projects dirctory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
_dir = path + '/' + ProjectFolder

def CloneRepo():
    os.chdir(path)
    Clone = os.system(f'git clone git@github.com:{UserName}/{ProjectFolder}.git')
    print(Clone)
    os.chdir(_dir)
    commands = [f'@echo # {ProjectFolder}>> README.md',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']

    for c in commands:
        os.system(c)
        
    print(f'{UserName}/{ProjectFolder} cloned')

    return os.system('code .')

        

g = Github(token)

if Type == 'org':
    org = g.get_organization(UserName)
    try:
        check_repo = org.get_repo(ProjectFolder)
    except:
        repo = org.create_repo(ProjectFolder)
        print(repo)
    else:
        print(f'Repo {UserName}/{ProjectFolder} already exists cloning')
    CloneRepo()

elif Type == 'user':
    user = g.get_user()
    login = user.login
    check_repo = user.get_repo(ProjectFolder)
    try:
        check_repo = user.get_repo(ProjectFolder)
    except:
        repo = user.create_repo(ProjectFolder)
        print(repo)
    else:
        print(f'Repo {UserName}/{ProjectFolder} already exists cloning')
    CloneRepo()

else:
    print("Command: create -Type <user/org> -Project <userorg>/<ProjectFolder>")
