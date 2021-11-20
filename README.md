# Auto-login for Raspberry Pi

## Setup

### Clone
```bash
git clone https://github.com/suvambasak/autologin.git
```
```bash
cd autologin/
```

### Install dependencies
For first time only
```bash
sh dependencies.sh 
```

### Execution
```bash
source .venv/bin/activate
```
```bash
pip install -r requirements.txt 
```
```bash
python3 autologin.py
```
```bash
deactivate
```