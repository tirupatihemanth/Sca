'''
Created on 04-Jan-2016

@author: Hemanth Kumar Tirupati
@ID    : cs13b027
@about: This file is about creating Memory Signatures for various web pages
'''

from selenium import webdriver
import subprocess
import threading
import time


ans = ""
browserDriver = "../lib/chromedriver"
threadLock = threading.Lock();
startLoad = 0

class browserThread (threading.Thread):
    def __init__(self, webpage):
        threading.Thread.__init__(self);
        self.webpage = webpage
        
    def run(self):
        global startLoad
        while 1:
            threadLock.acquire()
            if startLoad == 1:
                print "startLoad", startLoad
                threadLock.release()
                time.sleep(0.1)
                break;
            else:
                print "startLoad", startLoad
                threadLock.release()
                time.sleep(0.5)
        driver.get(self.webpage)
        driver.quit()
        threadLock.acquire()
        startLoad=0
        threadLock.release()
        
class signatureThread (threading.Thread):
    def __init__(self, website, counter, bthread):
        threading.Thread.__init__(self);
        self.website = website
        self.counter = counter
        self.bthread = bthread
        
    def run(self):
        fo = open("../data/webMd/raw_data/" + self.website + str(self.counter), "w")
        pids = ""

        global startLoad
        threadLock.acquire()
        startLoad = 1
        threadLock.release()
        print startLoad
        while pids == "" or len(pids.splitlines()) != 2:
            if (not self.bthread.is_alive()) and startLoad==0:
                return;
            pids = subprocess.check_output("./scanChromeProcess.sh").rstrip()
        pid = pids.splitlines()[1]
        time = 1
        anon = ""

        print pid
        global ans
        ans=""
        while 1:
            anon = subprocess.check_output(["./anonMemory.sh", pid])
            #print "anon", anon
            if anon == "" or anon == "0":
                break;
            ans += str(time) + " " + anon[:len(anon) - 2] + "\n";
            # fo.write(str(time) + " " + anon[:len(anon) - 2] + "\n")
            time = time + 1;
        fo.write(ans)
        fo.close()
        
namesObject = open("../data/webMd/webMdCommonNames.txt", "r");

with open("../data/webMd/webMdCommon.txt", "r") as f:
    for website in f:
        webpage = "http://" + website.rstrip()
        pageName = namesObject.readline().strip()
        print webpage
        for counter in range(1, 6):
            print "counter:", counter
            driver = webdriver.Chrome(browserDriver);
            bthread = browserThread(webpage)
            sthread = signatureThread(pageName, counter, bthread)
            sthread.start() 
            bthread.start()
            bthread.join()
            sthread.join()
