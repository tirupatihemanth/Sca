'''
Created on 04-Feb-2016

@author: hemanth
'''
import os
from subprocess import call


#inDir = "../data/processed_data/";
inDir = "../data/raw_data/";
attackDir = "../data/attack_data/";
outDir = "../data/processed_jackard/";
webList = "../data/filtered.txt";

#This function is to process the data obtained from the attack process and place it into processed_jackard folder

def process_jackard(inFilePath, outFilePath):
    processSig_jackard(inFilePath, outFilePath);

#DEPRECATED VERSION OF THE FUNCTION
# def process_jackard(inFilePath, outFilePath):
#     start=-1
#     sig = {}
#     keyList = []
#     with open(inFilePath,"r") as f:
#         var = [0,0];
#         for data in f:
#             var = [int(i) for i in data.split()]
#             if start == -1:
#                 prev = var[1]
#                 start = 1
#                 sig[var[1]] = 1;
#                 keyList.append(var[1]);
#             elif start ==1:
#                 if prev!=var[1]:
#                     start=2
#                     sig[var[1]]=1;
#                     keyList.append(var[1]);
#             else:
#                 if var[1] in sig:
#                     sig[var[1]] = sig[var[1]]+1;
#                 else:
#                     sig[var[1]] = 1;
#                     keyList.append(var[1])
#                          
#         if sig[var[1]]>1:
#             sig[var[1]] = 1;
#     outFile = open(outFilePath, 'w');
#     for key in keyList:
#         outFile.write(str(key) + " " + str(sig[key]) + "\n");
#     outFile.close()

#To build initial signature database from the initial raw data
#TODO: Change the way processing is done
#Finished Doing the above job. Now this function is Depracated
# def processSig_jackard(inFilePath, outFilePath):
#     with open(inFilePath) as f:
#         sig = {};
#         keyList = [];
#         for data in f:
#             var = int(data.split()[1])
#             if var not in sig:
#                 sig[var] = 1;
#                 keyList.append(var);
#             else:
#                 sig[var] = sig[var]+1;
#     outFile = open(outFilePath,"w");
#     for key in keyList:
#         outFile.write(str(key)+" "+str(sig[key])+"\n");
#     outFile.close();

def processSig_jackard(inFilePath, outFilePath):
    with open(inFilePath) as f:
        sig = {};
        prevKey = 0;
        keyList = [];
        for data in f:
            var = int(data.split()[1]);
            if var!=prevKey:
                prevKey = var;
                if var not in keyList:
                    sig[var]=1;
                    keyList.append(var);
                else:
                    sig[var] = sig[var]+1;
    outFile = open(outFilePath, "w");
    for key in keyList:
        outFile.write(str(key)+" "+str(sig[key])+"\n");
    outFile.close();
                
def processAll_jackard():
    #call(["sh", "processBasic_data.sh"])
    files = os.listdir(inDir);
    for fileName in files:
        processSig_jackard(inDir+fileName, outDir+fileName)
