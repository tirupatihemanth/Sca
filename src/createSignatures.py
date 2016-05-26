'''
Created on 15-Dec-2015

@author: Hemanth Kumar Tirupati
@ID    : cs13b027
'''

import subprocess
import threading
import time

from selenium import webdriver
from process_jackard import processAll_jackard


ans = ""
#Path to chromedriver executable required by selenium to create an instance of Chrome browser
browserDriver = "../lib/chromedriver"
#Path to the url's for signature creation
urlFeed = "../data/filtered.txt"
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
                #giving signature thread an edge and letting it loop over pids
                time.sleep(0.1)
                break;
            else:
                print "startLoad", startLoad
                threadLock.release()
                #not being greedy to acquire the lock
                time.sleep(0.1)
        driver.get(self.webpage)
        driver.quit()
        threadLock.acquire()
        startLoad = 0
        threadLock.release()
    
class signatureThread (threading.Thread):
    def __init__(self, website, counter, bthread):
        threading.Thread.__init__(self);
        self.website = website
        self.counter = counter
        self.bthread = bthread
        
    def run(self):
        fo = open("../data/raw_data/" + self.website + str(self.counter), "w")
        pids = ""

        global startLoad
        
        threadLock.acquire()
        startLoad = 1
        threadLock.release()
        
        while not pids:
            if (not self.bthread.is_alive()) and startLoad == 0:
                print("Browser thread already exited... Signature Thread exiting..,");
                return;
            pids = subprocess.check_output("./scanChromeProcess.sh").rstrip()
        pid = pids.splitlines()[0]
        time = 1
        anon = ""
        print pid
        global ans
        ans = ""
        while 1:
            anon = subprocess.check_output(["./drsMemory.sh", pid])
            # print "mem: "+anon+" "+str(len(anon))
            #print "anon: "+anon
            if anon == "" or anon == "0" or len(anon) <= 2 or len(anon) > 10:
                break;
            ans += str(time) + " " + anon[:len(anon) - 2] + "\n";
            # fo.write(str(time) + " " + anon[:len(anon) - 2] + "\n")
            time = time + 1;
        fo.write(ans)
        fo.close()


with open(urlFeed, "r") as f:
    for website in f:
        website = website.rstrip();
        weburl = "http://" + website;
        print weburl
        for counter in range(1, 6):
            print "counter: ", counter
            driver = webdriver.Chrome(browserDriver);
            bthread = browserThread(weburl)
            sthread = signatureThread(website, counter, bthread)
            sthread.start()
            bthread.start()
            bthread.join()
            sthread.join()
            

# processAll_dtw();
processAll_jackard();

