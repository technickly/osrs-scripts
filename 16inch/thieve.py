import warnings

import pyautogui as pg
import random
import time
import sys
import os
from tqdm import tqdm
iter_ = int(sys.argv[1])
t1 = time.time()
x,y = pg.position()
#x = 1518
#y = 293


_02 = 1615, 300; _03 = 1655, 300
_10 = 1525, 340; _11 = 1570, 340; _12 = 1615, 340; _13 = 1655, 340
_20 = 1525, 380; _21 = 1570, 375; _22 = 1615, 375; _23 = 1655, 375
_30 = 1525, 410; _31 = 1570, 410; _32 = 1615, 410; _33 = 1655, 410
_40 = 1525, 445; _41 = 1570, 445; _42 = 1615, 445; _43 = 1655, 445
_50 = 1525, 480; _51 = 1570, 480; _52 = 1615, 480; _53 = 1655, 480
_60 = 1525, 515; _61 = 1570, 515; _62 = 1615, 515; _63 = 1655, 515

RR = [  _02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]
def thieve(iter_):
    pg.moveTo(x , y)
    pg.click()
    time.sleep(.3+ random.random()/10)
    pg.press('f1')
    for i in tqdm(range(iter_)):
        noise = random.randint(-1,1)
        time.sleep(.6+ random.random()/10)
        pg.click()
        if i % 10 == 0 and i != 0:
            pg.press('f1')
            time.sleep(.3 + random.random()/10)
            pg.click()
            time.sleep(.3 + random.random()/10)
            pg.press('f1')
    time.sleep(.2)
    pg.press('f1')
    #os.system('say done')

    #eat_pos = random.randint(0,len(RR))
    #for j in range(10):
    #    pg.moveTo(RR[eat_pos]+random.randint(-2,2),RR[eat_pos]+random.randint(-2,2),tween_delay,pg.easeInQuad)
    #    time.sleep(.1)
    #    pg.click()
    #    time.sleep(.5+random.random()/10)

thieve(iter_)
# def eat():

    #
    # for i in range(pos in RR:
    #         move_delay = random.random()/2
    #         pg.moveTo(pos[0]+random.randint(-2,2),pos[1]+random.randint(-2,2),tween_delay,pg.easeInQuad)
    #         if click == True:
    #             pg.click()
    #         time.sleep(move_delay)
    #
    #         # if chance == 0:
    #     move_through_inv(RR[2:],shuffle=True,reverse=False,click=True)
    #     print(i,time.time()-t1, pg.position())
