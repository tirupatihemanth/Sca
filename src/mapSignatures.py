'''
Created on 15-Dec-2015

@author: Hemanth Kumar Tirupati
@ID    : cs13b027
'''

import subprocess
import threading
import time
from time import sleep

from selenium import webdriver
from process_jackard import processAll_jackard


ans = ""
#Path to chromedriver executable required by selenium to create an instance of Chrome browser
browserDriver = "../lib/chromedriver"
#Path to the url's for signature creation
urlFeed = "../data/mapUrls.txt"
nameFeed = "../data/mapNames.txt"
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
        fo = open("../data/map_raw_data/" + self.website + str(self.counter), "w")
        pids = ""

        global startLoad
        
        threadLock.acquire()
        startLoad = 1
        threadLock.release()
        global ans
        ans = ""
        
        while (not pids) or len(pids.splitlines())>=2 or int(pids.splitlines()[0])==basePid:
            if (not self.bthread.is_alive()) and startLoad == 0:
                print("Browser thread already exited... Signature Thread exiting..,");
                return;
            pids = subprocess.check_output("./scanChromeProcess.sh").rstrip()
        pid = pids.splitlines()[0]
        #print "signaturePid: "+pid;
        time = 1
        anon = ""
        #print pid
        statmObject = open("/proc/"+pid+"/statm", "r");
        while 1:
            try:
                anon = str(statmObject.readline());
            except(OSError, IOError) as e:
                #print "FileIOError";
                statmObject.close();
                break;
            
            #anon = subprocess.check_output(["./drsMemory.sh", pid])
            
            #print "anon str: "+ anon;
            # print "mem: "+anon+" "+str(len(anon))
            #print "anon: "+anon
            statmObject.flush();
            statmObject.seek(0);
            if not anon:
                continue;
            anon = anon.split()[5];
            if int(anon)<2048:
                continue;
            #print "anon: "+ anon;
            #statmObject.close();
            ans += str(time) + " " + anon + "\n";
            # fo.write(str(time) + " " + anon[:len(anon) - 2] + "\n")
            time = time + 1;
        #print "Total Time executed: "+ str(time);
        fo.write(ans)
        fo.close()


mapNamesObj = open(nameFeed, "r");
with open(urlFeed, "r") as f:
    global basePid;
    for website in f:
        placeName = str(mapNamesObj.readline());
        placeName = placeName.rstrip();
        website = website.rstrip();
        weburl = "https://" + website;
        print weburl
        for counter in range(1, 6):
            print "counter: ", counter
            driver = webdriver.Chrome(browserDriver);
            basePidStr = "";
            count=0;
            basePid=0;
            while not basePidStr and (count<10):
                basePidStr = subprocess.check_output("./scanChromeProcess.sh").rstrip()
                time.sleep(0.5);
                count= count+1;
            if basePidStr:
                basePid = int(basePidStr);
            print "basePid: "+str(basePid);
            bthread = browserThread(weburl)
            sthread = signatureThread(placeName, counter, bthread)
            #time.sleep(1);
            sthread.start()
            bthread.start()
            bthread.join()
            sthread.join()
            
mapNamesObj.close();
# processAll_dtw();
processAll_jackard();

