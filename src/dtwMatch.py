'''
Created on Dec 18, 2015

@author: Hemanth Kumar T
@ID: cs13b027
'''


import os
import sys
import threading


ITER=5
#Remember that max value of ITER CAN be 9 else change the implementation in dtwThread
#target = sys.argv[1]

dataDir = "../data/processed_data/"
files = os.listdir(dataDir)

def readSignature(fileName):
    signature = [0];
    with open(fileName,'r') as f:
        for data in f:
            #print "data: " + data + " :hello"
            var = data.rstrip().split()
            signature.append(int(var[1]))
    return signature;

#targetSignature = readSignature(target)
matchDict = {}
debugDict={}
minValue = sys.maxsize;
minWebsite = "";
threadLock = threading.Lock();

class dtwThread(threading.Thread):
    def __init__(self, fileName):
        threading.Thread.__init__(self);
        self.fileName = fileName.rstrip();
    
    def createDTWArray(self, m, n):
        dtwArray = [];
        dtwArray.append([sys.maxsize]*(n+1))
        for i in range(0,m):
            var = [0]*(n+1);
            var[0]=sys.maxsize;
            dtwArray.append(var);
        dtwArray[0][0]=0
        return dtwArray;

    def run(self):
        global minValue
        global minWebsite
        global matchDict
        dbSignature = readSignature(dataDir+self.fileName)
        m = len(dbSignature)
        n = len(targetSignature)
        #print "m: ", m
        #print "n: ", n
        dtwArray = self.createDTWArray(m-1, n-1);
        #print "reached dtw"
        for i in range(1, m):
            for j in range(1, n):
                cost = abs(dbSignature[i]-targetSignature[j])
                dtwArray[i][j] = cost + min(dtwArray[i-1][j], dtwArray[i][j-1], dtwArray[i-1][j-1])
        website = self.fileName[:len(self.fileName)-1];
        #print "finished dtw"
        with threadLock:
            print "website "+website
            if website in matchDict:
                if len(matchDict[website])==ITER-1:
                    matchDict[website].append(dtwArray[m-1][n-1]);
                    avg = sum(matchDict[website])/float(ITER);
                    if avg<minValue:
                        minValue = avg;
                        minWebsite = website;
                else:
                    matchDict[website].append(dtwArray[m-1][n-1]);
            else:
                matchDict[website] = [dtwArray[m-1][n-1]];
            if website in debugDict:
                debugDict[website].append(dtwArray[m-1][n-1])
            else:
                debugDict[website] = [dtwArray[m-1][n-1]]

def scan(targetFile):
    global target, targetSignature, matchDict,minValue, minWebsite,debugDict
    minWebsite = ""
    minValue = sys.maxsize
    matchDict = {}
    debugDict = {}
    target = targetFile;
    targetSignature = readSignature(target)
    threadList = []
    for f in files:
        dtwthread = dtwThread(f)
        dtwthread.start()
        threadList.append(dtwthread)
        
    for thread in threadList:
        thread.join()
    print targetFile, minWebsite, minValue
    print debugDict
