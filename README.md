# Project Initialization Automation

Create a repo and project folder, then open up Visual Studio Code in the correct directory.

## Setup

```powershell
git clone "https://github.com/totaldebug/ProjectInitializerAutomation.git"
cd ProjectInitializerAutomation
pip install -r requirements.txt
```

### Environment Variables

Right-click Computer, choose Properties or in Windows Control Panel, choose System.

Choose Advanced system settings.

On the Advanced tab, click Environment Variables.

Cick New to create a new environment variable.

```shell
create env vars :
> projects directory as - "mp"
> Github tocken as      - "gt"
> Add the path to the ProjectInitializerAutomation to PATH
```

### Usage

Create Repo and local folder:

```powershell
create -Type <org/user> -Project <GitHub-User>/<project_name>
```

Create local folder and init git:

```powershell
create -Type <org/user> -Project <GitHub-User>/<project_name> -Local
```
