#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

invs = int(sys.argv[1])

#ZOOM 900, 800x600 N UP


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


iron_spot_1 = [ 943 , 349 ]
iron_spot_2 = [ 1030 , 256 ]
iron_spot_3 = [ 1113 , 341 ]

def mine():
    if random.randint(0,12) == 5:
        print('middle->right->left')
        # time.sleep(2.4 + random.random())
        # pg.moveTo(iron_spot_2[0]+random.randint(-2,2),iron_spot_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        # pg.click()
        # time.sleep(1.8+random.random()/10)
        # pg.moveTo(iron_spot_3[0]+random.randint(-2,2),iron_spot_3[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        # pg.click()
        # time.sleep(1.8+random.random()/10)
        # pg.moveTo(iron_spot_1[0]+random.randint(-2,2),iron_spot_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        # pg.click()
        # time.sleep(1.8+random.random()/10)
        time.sleep(12+random.random())
    else:
        # print('left->middle->right')
        pg.moveTo(iron_spot_1[0]+random.randint(-2,2),iron_spot_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(2.4+random.random()/10)
        pg.moveTo(iron_spot_2[0]+random.randint(-2,2),iron_spot_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(2.4+random.random()/10)
        pg.moveTo(iron_spot_3[0]+random.randint(-2,2),iron_spot_3[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(2.4+random.random()/10)



def move_through_inv(RR,shuffle,reverse,click):
    tween_delay = random.random()/7.5
    # IF WANT TO SHUFFLE
    if shuffle == True:
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            random.shuffle(RR)
    # IF WANT TO REVERSE
    if reverse == True:
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            RR.reverse()

    for pos in RR:
        move_delay = random.random()/2
        pg.moveTo(pos[0]+random.randint(-2,2),pos[1]+random.randint(-2,2),tween_delay,pg.easeInQuad)
        if click == True:
            pg.click()
        time.sleep(move_delay)

for i in tqdm(range(invs)):
    t1 = time.time()
    for k in range(9):
        mine()
    if i % 3 == 0:
        move_through_inv(RR[1:],shuffle=True,reverse=True,click=True)
    else:
        chance = random.randint(0,1)
        if chance == 0:
            move_through_inv(RR[1:],shuffle=False,reverse=False,click=True)
        else:
            move_through_inv(RR[1:],shuffle=False,reverse=True,click=True)
    print(i,time.time()-t1, pg.position())
