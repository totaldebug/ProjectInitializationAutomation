# Project Initialization Automation

## pre-setup

Right-click Computer, choose Properties or in Windows Control Panel, choose System.

Choose Advanced system settings.

On the Advanced tab, click Environment Variables.

Cick New to create a new environment variable.

```shell
create env vars :
> projects directory as - "mp"
> Github tocken as      - "gt"
```

## Setup

```bash
git clone "https://github.com/totaldebug/ProjectInitializerAutomation.git"
cd ProjectInitializerAutomation
pip install -r requirements.txt

path:
"projectInitializerAutomation" add the folder directory to path
```

### Usage

```bash
Command to run the program type

'create <GitHub-User>/<project_name>'
'create <GitHub-User>/<project_name> l' - just locally
```