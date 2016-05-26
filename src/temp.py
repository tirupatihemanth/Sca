# import time
# 
# import threading
# 
# 
# var=5;
# threadLock = threading.Lock()
# class myClass(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self);
#     def run(self):
#         global var
#         threadLock.acquire()
#         var=1;
#         threadLock.release()
# 
# class secClass(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self);
#     def run(self):
#         global var
#         threadLock.acquire()
#         print "var: ", var
#         threadLock.release()
#         
# ob1 = myClass();
# ob2 = secClass();
# 
# ob1.start();
# time.sleep(1)
# ob2.start()

with open('../data/filtered.txt', 'r') as f:
    for website in f:
        print("%s" % website.rstrip());