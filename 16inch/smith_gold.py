#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys
#face south
invs = int(sys.argv[1])
run = str(sys.argv[2])
#ZOOM 900, 800x600 E UP
#start at bank with ice gloves bank open facing south

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


# ordon = [ 1169 , 268 ]
# deposit = [ 1252 , 188 ]
# bank = [ 1422 , 459 ]
click_run =     [ 1528 , 195 ]
deposit = [ 1576 , 352 ]
withdraw_gold = [ 1019 , 159 ]
equip = [ 1531 , 347 ]
smelt_ore = [ 1382 , 537 ]
pickup_bar = [ 1327 , 309 ]
bank = [ 1169 , 237 ]

# def smith(invs,run):
for i in tqdm(range(invs)):
    # for j in range(4):
        # t1 = time.time()
        # cook()
    pg.moveTo(deposit[0]+random.randint(-1,1),deposit[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.6+(random.random()))
    pg.moveTo(withdraw_gold[0]+random.randint(-1,1),withdraw_gold[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.6+(random.random()/2))
    pg.press('esc')
    time.sleep(.6 + random.random()/2)
    pg.moveTo(equip[0]+random.randint(-1,1),equip[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.6 + random.random()/2)

    pg.moveTo(smelt_ore[0]+random.randint(-1,1),smelt_ore[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    if run == 'run':
        time.sleep(10+(random.random()))
    else:
        time.sleep(18+(random.random()))
    pg.moveTo(equip[0]+random.randint(-1,1),equip[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    time.sleep(.6 + random.random()/2)

    pg.moveTo(pickup_bar[0]+random.randint(-1,1),pickup_bar[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()
    if run == 'run':
        time.sleep(3.5 + random.random()/2)
    else:
        time.sleep(6.5 + random.random()/2)

    pg.press('space')
    time.sleep(.6+(random.random()/2))


    pg.moveTo(bank[0]+random.randint(-1,1),bank[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    pg.click()

    if run == 'run':
        time.sleep(4+(random.random()))
    else:
        time.sleep(8+(random.random()))

# for i in range(1):
    # smith(5,'run')
    # # pg.moveTo(click_run[0]+random.randint(-1,1),click_run[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # # pg.click()
    # pg.moveTo(click_run[0]+random.randint(-1,1),click_run[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    # pg.click()
    #
    # time.sleep(.6+(random.random()/2))
    #
    #

    #
    # pg.press('esc')
    # time.sleep(.6+(random.random()/2))
    # time.sleep(1.2)
    # pg.press('z')
    # time.sleep(9)
    # pg.press('1')

#
# fire = [ 1299 , 241 ]
# raw =[ 1016 , 163 ]
# deposit = [ 1374 , 477 ]
# bank = [ 1176 , 372 ]
# def cook():
#     if random.randint(0,10) == 30:
#         print('pause')
#         time.sleep(5 + random.random())
#         pg.moveTo(w2[0]+random.randint(-2,2),w2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#         pg.click()
#         time.sleep(26.+(random.random()*3.5))
#         pg.moveTo(w1[0]+random.randint(-2,2),w1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#         pg.click()
#         time.sleep(26.+(random.random()*3.5))
#     else:
#         pg.moveTo(bank[0]+random.randint(-2,2),bank[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#         pg.click()
#         time.sleep(.9+(random.random()/10))
#         pg.moveTo(deposit[0]+random.randint(-2,2),deposit[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#         pg.click()
#         time.sleep(.8+(random.random()/2))
#         pg.moveTo(raw[0]+random.randint(-2,2),raw[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#         pg.click()
#         time.sleep(.8+(random.random()/2))
#         pg.press('esc')
#         time.sleep(.65)
#         pg.moveTo(fire[0]+random.randint(-2,2),fire[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#         pg.click()
#         time.sleep(.8+random.random()/2)
#         pg.press('space')
#         time.sleep((65/7)+random.random())
#
#
#
#
# for i in tqdm(range(invs)):
#     t1 = time.time()
#     cook()
#     # pg.moveTo(run_bank[0]+random.randint(-1,1),run_bank[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     # pg.click()
#     # time.sleep(10.+(random.random()))
#     # # time.
#     # pg.moveTo(deposit[0]+random.randint(-1,1),deposit[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     # pg.click()
#     # time.sleep(.5+random.random()/2)
#     # pg.press('esc')
#     # time.sleep(.65)
#     # pg.moveTo(run_tree[0]+random.randint(-1,1),run_tree[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
#     # pg.click()
#     # time.sleep(10+random.random())
#     #
#     #
#     #
#     #
#     #
#     #
#     #
#
#     print(i,time.time()-t1, pg.position())
