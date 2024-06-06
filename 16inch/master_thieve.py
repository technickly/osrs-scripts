#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time

#INV MAPPER
#CLIENT 765x550
#KEEP SIDE OPEN, TOP RIGHT
#45 Horizontal
#40 vertical
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


#Skip Inventory spots
# skips = [0,13,14,15,16]

# RR_skip = []
#
# for pos,value in enumerate(RR):
#     if pos not in skips:
#         RR_skip.append(value)
# RR = RR_skip
def get_start():
    start = pg.position()
    print(start)
    return start
def pickpocket(start):
    for i in tqdm(range(60)):
        tween_delay = random.random()/5
        # tween_delay2 = random.random()/5
        # tween_delay3 = random.random()/5
        # move_delay = random.random()/2.
        coin_flip = random.randint(0,1)
        if coin_flip == 0:
            noise = 0
        else:
            noise = random.randint(-1,1)
        pg.moveTo(start[0]+noise,start[1]+noise,tween_delay,pg.easeInQuad)
        pg.click()
        time.sleep(.9+random.random()/10)


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
        move_delay = .4+random.random()/10
        pg.moveTo(pos[0]+random.randint(-2,2),pos[1]+random.randint(-2,2),tween_delay,pg.easeInQuad)
        if click == True:
            pg.click()
            pg.click()

        time.sleep(move_delay)


start = get_start()
t1 = time.time()
for i in tqdm(range(140)):
    t2 = time.time()
    pickpocket(start)
##DEFINE THIS HERE
    move_through_inv(RR[6:],shuffle=False,reverse=False,click=True)
    print('Total Time %s'%(time.time()-t1))
    print('Inventory Time %s'%(time.time()-t2))
