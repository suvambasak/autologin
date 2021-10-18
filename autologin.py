from selenium import webdriver
from pyvirtualdisplay import Display
import json
import logging

# Reading configuration file.
conf = json.loads(open('conf.json').read())
logging.warning('Reading configuration file...')

# Creating virtual display.
display = Display(visible=0, size=(1024, 768))
display.start()
logging.warning('Creating virtual display...')

opts = webdriver.ChromeOptions()
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-setuid-sandbox')

# Web driver.
browser = webdriver.Chrome(options=opts)
logging.warning('Configuring webdriver...')

# URL
browser.get(conf['url'])
logging.warning('URL: '+conf['url'])

# username
username_textbox = browser.find_element_by_id("username")
username_textbox.send_keys(conf['username'])
logging.warning('Setting username...')

# password
password_textbox = browser.find_element_by_id("password")
password_textbox.send_keys(conf['password'])
logging.warning('Setting password...')

# Click sign in button.
link = browser.find_element_by_link_text('Sign in')
logging.warning('Signing in...')
link.click()

# Close display.
display.stop()
logging.warning('Complete.')