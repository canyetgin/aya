
from time import sleep
import sys

import time



for i in range(50):
    time.sleep(0.1)
    print(("[%d"%i+"%]")+("["+('#'*i)),end= ((50-i)*' ')+"] \r")
    if(i==49):
     time.sleep(0.1)
     print(("[OK!]"),end=(51)*' '+" \r")
    