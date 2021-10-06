# Auto-login for Raspberry Pi

## Setup

### Install dependencies
Install `chromium-chromedriver`, `xvfb`
```bash
$ sudo apt install chromium-chromedriver xvfb
```

### Execution
```bash
$ git clone https://github.com/suvambasak/autologin.git
$ cd autologin/
$ source .venv/bin/activate
$ python3 autologin.py
$ deactivate
```