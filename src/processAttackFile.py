'''
Created on 19-Dec-2015

@author: Hemanth Kumar Tirupati
@ID    : cs13b027
'''

start=-1
base=0
lastData=""
first = [0,0]
attackDir = "../data/attack_data/";

def processAttackFile(pidString):
    global start,first,lastData,base,attackDir
    fo = open(attackDir+"processed_"+pidString,"w")
    start=-1
    base=0
    lastData=""
    first = [0,0]
    with open(attackDir+pidString,"r") as f:
        global first
        for data in f:
            var = [int(i) for i in data.split()]
            if start == -1:
                prev = var[1]
                start = 1
            elif start ==1:
                if prev!=var[1]:
                    start=2
                    base = var[0]-1
                    fo.write("0 "+str(prev)+"\n");
                    lastData+="1 "+str(var[1])+"\n";
                    prev = var[1]
                    first[0]=var[0]
                    first[1]=var[1]
            elif prev==var[1]:
                lastData+=str(var[0]-base)+" "+str(var[1])+"\n"
            else:
                fo.write(lastData)
                lastData=""
                lastData+=str(var[0]-base)+" "+str(var[1])+"\n"
                prev = var[1]
                first[0]=var[0]
                first[1]=var[1] 
    
    lastData=""
    fo.write(str(first[0]-base)+" "+str(first[1]))
    fo.close()