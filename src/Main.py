'''
Created on 15-Dec-2015

@author: Hemanth Kumar Tirupati
@ID    : cs13b027
'''

import subprocess
import sys
import threading
import time

from selenium import webdriver


ans = ""
browserDriver = "../lib/chromedriver"
threadLock = threading.Lock();
startLoad = 0

class browserThread (threading.Thread):
    def __init__(self, webpage):
        threading.Thread.__init__(self);
        self.webpage = webpage
        
    def run(self):
        while 1:
            threadLock.acquire()
            if startLoad == 1:
                threadLock.release()
                time.sleep(0.1)
                break;
            else:
                threadLock.release()
                time.sleep(0.5)
        driver.get(self.webpage)
        driver.quit()
        
class signatureThread (threading.Thread):
    def __init__(self, website, counter):
        threading.Thread.__init__(self);
        self.website = website
        self.counter = counter
        
    def run(self):
        fo = open("../data/" + self.website + str(self.counter), "w")
        pids = ""

        global startLoad
        with threadLock:
            startLoad=1
            
        while pids == "" or len(pids.splitlines())!=2:
            pids = subprocess.check_output("./scanChromeProcess.sh").rstrip()
        pid = pids.splitlines()[1]
        time = 1
        anon = ""

        print pid
        global ans
        while 1:
            anon = subprocess.check_output(["./anonMemory.sh", pid])
            if anon == "" or anon == "0":
                break;
            ans+=str(time) + " " + anon[:len(anon) - 2] + "\n";
            #fo.write(str(time) + " " + anon[:len(anon) - 2] + "\n")
            time = time+1;
        fo.write(ans)
        fo.close()
        
with open("../data/filtered.txt", "r") as f:
    for website in f:
        webpage = "http://" + website.rstrip()
        print webpage
        for counter in range(1, 6):
            print "counter:", counter
            driver = webdriver.Chrome(browserDriver);
            sthread = signatureThread(website.rstrip(), counter)
            bthread = browserThread(webpage)
            sthread.start()
            bthread.start()
            bthread.join()
            sthread.join()
            startLoad = 0
            ans=""
