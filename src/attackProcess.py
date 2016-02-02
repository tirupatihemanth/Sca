'''
Created on Dec 18, 2015

@author: Hemanth Kumar T
@ID: cs13b027
'''

import subprocess
import threading
import time
from dtwMatch import scan
from processAttackFile import processAttackFile

#These processes have already started even before starting our attack process
#Let's wait to see what new tabs he opens
#We can do nothing for now about all those websites that he has already opened

pidString = subprocess.check_output("./scanChromeProcess.sh").rstrip()
prevPids = pidString.splitlines()


class spyThread(threading.Thread):
    def __init__(self, pid):
        threading.Thread.__init__(self);
        self.pid = pid;
        
    def run(self):
        fileName = "../data/attack_data/"+self.pid; 
        fo = open(fileName,'w');
        ans="";
        #for now timeout is 5 seconds i.e we are giving at most 5 seconds for the page to load
        #May be in the future we can adjust this timeout duration based on the bandwidth
        timeout = time.time()+5;
        counter=1
        
        while 1:
            anon = subprocess.check_output(["./anonMemory.sh", self.pid])
            if anon == "" or anon == "0" or time.time()>=timeout:
                break;
            ans+=str(counter) + " "+anon[:len(anon)-2]+"\n";
            counter+=1;
            
        fo.write(ans)
        fo.close()
        processAttackFile(self.pid)
        scan("../data/attack_data/processed_"+self.pid)
        
while 1:
    pidString = subprocess.check_output("./scanChromeProcess.sh").rstrip()
    curPids = pidString.splitlines()
    #print "prevPids: "
    #print prevPids
    #print "curPids:"
    #print curPids
    for pid in curPids:
        if pid not in prevPids:
            spythread = spyThread(pid);
            spythread.start()

    prevPids = [pid for pid in prevPids if pid in curPids]
    
    for pid in curPids:
        if pid not in prevPids:
            prevPids.append(pid)
        
