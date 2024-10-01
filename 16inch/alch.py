import warnings
warnings.filterwarnings("ignore")

import pyautogui as pg
import random
import time
import sys
num_ = int(sys.argv[1])*2
t1 = time.time()
x,y = pg.position()
#pg.moveTo(1661 , 378
#)
# x,y = [ 1657 , 885 ]
for i in range(num_):
    noise = random.randint(-1,1)
    flip = random.randint(0,10)
    if flip == 2:
        pg.moveTo(x+noise , y+noise)

    time.sleep(1.4 + random.random()/5)
    pg.click()
