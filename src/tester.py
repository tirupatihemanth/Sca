'''
Created on 19-Jan-2016

@author: hemanth
'''

import subprocess
import time
from yaml import scan

from selenium import webdriver

# anon = subprocess.check_output(["./drsMemory.sh", "13444"]);
# print not anon

chrome = '../lib/chromedriver'
driver = webdriver.Chrome(chrome)
print "getready"
print subprocess.check_output("./scanChromeProcess.sh");
print subprocess.check_output(["ps", "-aux"])
time.sleep(15);
driver.get("https://www.google.com")
#time.sleep(5)
print subprocess.check_output(["ps", "-aux"])
print subprocess.check_output("./scanChromeProcess.sh");
time.sleep(5);
driver.quit();
