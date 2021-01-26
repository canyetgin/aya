
from time import sleep
import sys
import time
for i in range(100):
    time.sleep(0.1)
    print(("[%d"%i+"%]")+("["+('#'*i)),end= ((99-i)*' ')+"] \r")
    if(i==99):
     time.sleep(0.1)
     print(("[OK!]"),end=(100)*' '+" \r")
    