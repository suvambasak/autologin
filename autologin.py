from selenium import webdriver
from pyvirtualdisplay import Display
import json

# Reading configuration file.
conf = json.loads(open('conf.json').read())

# Creating virtual display.
display = Display(visible=0, size=(1024, 768))
display.start()
opts = webdriver.ChromeOptions()
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-setuid-sandbox')

# Web driver.
browser = webdriver.Chrome(options=opts)

# URL
browser.get(conf['url'])

# username
username_textbox = browser.find_element_by_id("username")
username_textbox.send_keys(conf['username'])

# password
password_textbox = browser.find_element_by_id("password")
password_textbox.send_keys(conf['password'])

# Click sign in button.
link = browser.find_element_by_link_text('Sign in')
link.click()

# Close display.
display.stop()