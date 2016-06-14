'''
Created on 19-Dec-2015

@author: Hemanth Kumar Tirupati
@ID    : cs13b027
'''

import os
from subprocess import call
import subprocess


#inDir = "../data/processed_data/";
inDir = "../data/raw_data/";
#inDir = "../data/map_raw_data/";
attackDir = "../data/attack_data/";
outDir = "../data/processed_dtw/";
webList = "../data/filtered.txt";

# start=-1
# base=0
#lastData=""
#first = [0,0]

#This processing function tries to give the complete detail i.e
#The below function just returns the entire sequence recorded.
# def process_dtw(inFilePath, outFilePath):
#     global start,first,lastData,base,attackDir,count
#     fo = open(outFilePath,"w")
#     start=-1
#     base=0
#     #lastData=""
#     first = [0,0]
#     count=1;
#     with open(inFilePath,"r") as f:
#         for data in f:
#             data = data.strip();
#             if not data:
#                 continue;
#             var = [int(i) for i in data.split()]
#             if start == -1:
#                 prev = var[1]
#                 start = 1
#             elif start ==1:
#                 if prev!=var[1]:
#                     start=2
#                     base = var[0]-1
#                     fo.write("0 "+str(prev)+"\n");
#                     #lastData+="1 "+str(var[1])+"\n";
#                     prev = var[1]
#                     first[0]=var[0]
#                     first[1]=var[1]
#             elif prev==var[1]:
#                 count = count+1;
# #                lastData+=str(var[0]-base)+" "+str(var[1])+"\n"
#             else:
#                 timeBase = first[0]-base;
#                 for i in range(count):
#                     fo.write(str(timeBase+i)+" "+str(first[1])+"\n");    
#                 #fo.write(lastData)
#                 #lastData=""
#                 #lastData+=str(var[0]-base)+" "+str(var[1])+"\n"
#                 count = 1;
#                 prev = var[1]
#                 first[0]=var[0]
#                 first[1]=var[1] 
#     
#     #lastData=""
#     
#     fo.write(str(first[0]-base)+" "+str(first[1]))
#     fo.close()

def process_dtw(inFilePath, outFilePath):
    fo = open(outFilePath,"w")
    #lastData=""
    prev = 0;
    with open(inFilePath,"r") as f:
        for data in f:
            data = data.strip();
            if not data:
                continue;
            var = [int(i) for i in data.split()]
            if prev != var[1]:
                fo.write(str(var[0])+" "+str(var[1])+"\n");
                prev = var[1];
    fo.close()

def processAll_dtw():
    #call(["sh", "processBasic_data.sh"])
    files = os.listdir(inDir);
    for fileName in files:
        process_dtw(inDir+fileName, outDir+fileName);
#process_dtw("../data/attack_data/8954", "../data/attack_data/processed_dtw8954");

processAll_dtw();