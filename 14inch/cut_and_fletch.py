#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

#ZOOM 100, 800x600 E UP


_00 = 1230, 280; _01 = 1275, 280; _02 = 1320, 280; _03 = 1365, 280
_10 = 1230, 315; _11 = 1275, 315; _12 = 1320, 315; _13 = 1365, 315
_20 = 1230, 350; _21 = 1275, 350; _22 = 1320, 350; _23 = 1365, 350
_30 = 1230, 385; _31 = 1275, 385; _32 = 1320, 385; _33 = 1365, 385
_40 = 1230, 420; _41 = 1275, 420; _42 = 1320, 420; _43 = 1365, 420
_50 = 1230, 455; _51 = 1275, 455; _52 = 1320, 455; _53 = 1365, 455
_60 = 1230, 490; _61 = 1275, 490; _62 = 1320, 490; _63 = 1365, 490

RR = [  _00,_01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]

knife = _01
w1 =[ 1184 , 367 ]
# [~/osrs-scripts/14inch]$ python3 get_position.py
w2 =[ 1066 , 197 ]
# nnife = RR[0]
# run_tree = [ 1378 , 136 ]
def cut():
    if random.randint(0,20) == 2:
        print('REVERSE')
        time.sleep(3 + random.random())
        for j in range(3):
            pg.moveTo(w2[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
            pg.click()
            time.sleep(13.+(random.random()*3.5))
            pg.moveTo(w1[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
            pg.click()
            time.sleep(13.+(random.random()*3.5))

        # for j in range(2):
        #     pg.moveTo(w2[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        #     pg.click()
        #     time.sleep(26.+(random.random()*3.5))
        #     pg.moveTo(w1[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        #     pg.click()
        #     time.sleep(26.+(random.random()*3.5))
    else:
        for j in range(2):
            pg.moveTo(w1[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
            pg.click()
            time.sleep(13.+(random.random()*3.5))
            pg.moveTo(w2[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
            pg.click()
            time.sleep(13.+(random.random()*3.5))

def fletch():
    log = RR[random.randint(2,3)]

    pg.moveTo(RR[1][0]+random.randint(-2,2),RR[1][1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.65+(random.random()/2))
    pg.moveTo(log[0]+random.randint(-2,2),log[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.6+random.random()/2)
    pg.press('space')
    time.sleep(.6+random.random()/2)
    pg.press('space')


    time.sleep(45.65+(random.random()))

for i in tqdm(range(invs)):
    t1 = time.time()
    cut()
    fletch()
    # pg.moveTo(run_bank[0]+random.randint(-1,1),run_bank[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(10.+(random.random()))
    # # time.
    # pg.moveTo(deposit[0]+random.randint(-1,1),deposit[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(.5+random.random()/2)
    # pg.press('esc')
    # time.sleep(.65)
    # pg.moveTo(run_tree[0]+random.randint(-1,1),run_tree[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    # time.sleep(10+random.random())
    #
    #






    print(i,time.time()-t1, pg.position())
