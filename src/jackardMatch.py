'''
Created on 04-Feb-2016

@author: hemanth
'''


import os
import sys
import threading


ITER=5
#Remember that max value of ITER CAN be 9 else change the implementation in dtwThread
#target = sys.argv[1]

dataDir = "../data/processed_jackard/"
files = os.listdir(dataDir)

def readSignature(fileName):
    signature = {};
    with open(fileName,'r') as f:
        for data in f:
            #print "data: " + data + " :hello"
            var = [int(i) for i in data.rstrip().split()]
            signature[var[0]] = var[1];
    return signature;

#targetSignature = readSignature(target)
matchDict = {}
debugDict={}
minValue = sys.maxsize;
minWebsite = "";
target = "";
targetSignature="";
threadLock = threading.Lock();

class jackardThread(threading.Thread):
    def __init__(self, fileName):
        threading.Thread.__init__(self);
        self.fileName = fileName.rstrip();
    

    def run(self):
        global minValue
        global minWebsite
        global matchDict
        dbSignature = readSignature(dataDir+self.fileName)
        #Remember that these signatures have a zero prepended which makes the job a little bit easier in dtw arlgorithm
        intersect = {};
        union = {};
        for key, val in targetSignature.items():
            if key in dbSignature:
                intersect[key] = min(val, dbSignature[key])
                union[key] = max(val,dbSignature[key])
        intersectSum=0;
        unionSum=0;
        for key, val in intersect.items():
            intersectSum+=val;
        for key, val in union.items():
            unionSum+=val;
        jackardIdx1 = -1.0;
        jackardIdx2 = -1.0;
        
        if len(union)!=0:
            jackardIdx1 = (float)(len(intersect)/(1.0*len(union)));
            jackardIdx2 = (float)(intersectSum/unionSum);
        else:
            print "DIVIDE BY ZERO IN JACKARD INDEX\n"
        website = self.fileName[:len(self.fileName)-1]; 
        #print "finished dtw"
        with threadLock:
            print( 'website %s %.5f %.5f\n' %(website , jackardIdx1, jackardIdx2));
            print unionSum, intersectSum, len(union), len(intersect);
#             if website in debugDict:
#                 debugDict[website].append(dtwArray[m-1][n-1])
#             else:gmail
#                 debugDict[website] = [dtwArray[m-1][n-1]]

def scan_jackard(targetFile):
    global target, targetSignature, matchDict,minValue, minWebsite, debugDict
    minWebsite = ""
    minValue = sys.maxsize
    matchDict = {}
    debugDict = {}
    target = targetFile;
    targetSignature = readSignature(target)
    threadList = []
    print files;
    for f in files:
        jackardthread = jackardThread(f)
        jackardthread.start()
        threadList.append(jackardthread)
        
    for thread in threadList:
        thread.join()
#     print targetFile, minWebsite, minValue
#     print debugDict