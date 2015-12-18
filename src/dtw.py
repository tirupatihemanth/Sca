import os
import sys
import threading

ITER=5
#Remember that max value of ITER CAN be 9 else change the implementation in dtwThread
target = sys.argv[1]

dataDir = "../data/processed_data/"
files = os.listdir(dataDir)

def readSignature(fileName):
    signature = [];
    with open(target,'r') as f:
        for data in f:
            var = data.split()
            signature.append(int(var[1]))
    return signature;

targetSignature = readSignature(target)
matchDict = {}
minValue = sys.maxint;
minWebsite = "";

class dtwThread(threading.Thread):
    def __init__(self, fileName, iter):
        threading.Thread.__init__(self);
        self.fileName = fileName;
        self.iter = iter;
    
    def createDTWArray(self, m, n):
        dtwArray = [];
        dtwArray.append([sys.maxint]*(n+1))
        for i in range(0,m):
            var = [0]*(n+1);
            var[0]=sys.maxint;
            dtwArray.append(var);
        return dtwArray;

    def run(self):
        m = len(dbSignature)
        n = len(targetSignature)
        dbSignature = readSignature(self.fileName)
        dtwArray = createDTWArray(m, n);
        for i in range(1, m+1):
            for j in range(1, n+1):
                cost = abs(dbSignature[i]-targetSignature[j])
                dtwArray[i][j] = cost + min(dtwArray[i-1][j], dtwArray[i][j-1], dtwArray[i-1][j-1])
        website = self.fileName[:len(self.fileName)-1];
        if website in matchDict:
            if len(matchDict[website])==ITER-1:
                matchDict[website].append(dtwArray[m][n]);
                avg = sum(matchDict[website])/float(len(matchDict[website]));
                if(avg<minValue)
                    minValue = avg;
                    minWebsite = website;
            else:
                matchDict[website].append(dtwArray[m][n]);
        else:
            matchDict[website] = [dtwArray[m][n]];

for f in files:
    for iter in range(1,ITER+1):
        dtwthread = dtwThread(f,iter)
        dtwthread.start()

    with open(dataDir+sign,'r') as f:
        dbSignature = []
        for data in f:
            var = data.split()
            var[0] = int(var[0])
            var[1] = int(var[1])
            dbSignature.append(var)
        
