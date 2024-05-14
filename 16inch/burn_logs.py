#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

#ZOOM 30, 800x600 E UP


_00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
_10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
_20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
_30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
_40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
_50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
_60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

RR = [  _00,_01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]

def burn():

    # for inv in range(i)
    tind = RR[0]
    for num,log in enumerate(RR[1:]):
        # if num < 10:
        t = 4*.7 + random.random()
        # else:
        #     t = 4*.6 + random.random()/5.

        pg.moveTo(tind[0]+random.randint(-2,2),tind[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        pg.moveTo(log[0]+random.randint(-2,2),log[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(t)
        # pg.click()

        # time.sleep(26.+(random.random()*3.5))
burn()
        # print(j)
# w1 = [ 1279 , 362 ]
# w2 = [ 1303 , 347 ]
# run_bank = [ 1222 , 591 ]
# deposit = [ 1369 , 480 ]
# run_tree = [ 1364 , 176 ]
# def cut():
#     if random.randint(0,5) == 3:
#         print('pause')
#         time.sleep(22 + random.random())
#         for j in range(2):
#             pg.moveTo(w2[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#             pg.click()
#             time.sleep(26.+(random.random()*3.5))
#             pg.moveTo(w1[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#             pg.click()
#             time.sleep(26.+(random.random()*3.5))
#     else:
#         for j in range(2):
#             pg.moveTo(w1[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#             pg.click()
#             time.sleep(26.+(random.random()*3.5))
#             pg.moveTo(w2[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#             pg.click()
#             time.sleep(26.+(random.random()*3.5))
#
#
#
# for i in tqdm(range(invs)):
#     t1 = time.time()
#     cut()
#     pg.moveTo(run_bank[0]+random.randint(-1,1),run_bank[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(11.+(random.random()))
#     # time.
#     pg.moveTo(deposit[0]+random.randint(-1,1),deposit[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(.5+random.random()/2)
#     pg.press('esc')
#     time.sleep(.65)
#     pg.moveTo(run_tree[0]+random.randint(-1,1),run_tree[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(11+random.random())
#
#
#
#
#
#
#
#
#     print(i,time.time()-t1, pg.position())
