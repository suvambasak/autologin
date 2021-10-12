# Auto-login for Raspberry Pi

## Setup

### Clone
```bash
$ git clone https://github.com/suvambasak/autologin.git
$ cd autologin/
```

### Install dependencies
For first time only
```bash
$ sh dependencies.sh 
```

### Execution
```bash
$ source .venv/bin/activate
$ pip install -r requirements.txt 
$ python3 autologin.py

$ deactivate
```