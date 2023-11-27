import multiprocessing
import os
import time
from datetime import datetime  ## get most accurate time
from random import random  ## returns a random float between 0 and 1

def wait_print_time(): #wait a random fraction of a second, print the current time, and exit
    ran = random()
    time.sleep(ran)
    #print current time
    print("Process %s says: The time is %s after waiting %s secs." % (os.getpid(), datetime.now(), ran)) 
    
if __name__ == "__main__":
    print("Starting the main program at time %s" % datetime.now())
    for n in range(3):
        p = multiprocessing.Process(target=wait_print_time)
        p.start()