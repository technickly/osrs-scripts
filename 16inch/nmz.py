#import warnings
#warnings.filterwarnings("ignore")
from tqdm import tqdm
import pyautogui as pg
import random
import time
import sys

mins = int(int(sys.argv[1]))
# mins_ = 100
time.sleep(1)
click_bank = pg.position()
# click_bank = [ 1287 , 445 ]

#ZOOM 900, 800x600 N UP


_00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
_10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
_20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
_30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
_40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
_50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
_60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

RR = [  _01,_02,_03,
        _10,_11,_12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33,
        _40,_41,_42,_43,
        _50,_51,_52,_53,
        _60,_61,_62,_63 ]

pray_flick = [ 1512 , 163 ]
rock = _00

# def rock():

def absorbtion():
    n1,n2 = random.randint(-1,1),random.randint(-1,1)
    r_num = random.randint(0,len(RR)-1)
    random_spot = RR[r_num]
    print('drinking')
    x,y = random_spot[0]+n1,random_spot[1]+n2
    pg.moveTo(x,y,.2+random.random()/2,pg.easeInQuad)
    pg.click()
    # time.sleep(1.2+random.random()/10)
    # pg.click()
    time.sleep(1.2+random.random()/10)

def flick_pray(mins_):
    for i in tqdm(range(mins_)):
        if i % 2 == 0:
            time.sleep(.6 + random.random()/10)
            absorbtion()
            # print('Drinking Absorbtion')
        pg.moveTo(pray_flick[0]+random.randint(-1,1),pray_flick[1]+random.randint(-1,1),.5+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(.6+random.random()/2)
        pg.click()
        time.sleep(random.randint(25,40))
        pg.moveTo(rock[0]+random.randint(-1,1),rock[1]+random.randint(-1,1),.5+random.random()/2,pg.easeInQuad)
        pg.click()
        time.sleep(random.random()/2)
        pg.click()

        # print('Flicked')
        # px,py =

flick_pray(mins)

# # move_to_sand = [ 1537 , 278 ]
# # click_bank = [ 1287 , 445 ]
# deposit_glass_item = [ 1569 , 353 ]
# bank_1 = [ 1016 , 160 ]
# # bank_2 = [ 1065 , 159 ]
# furnace = [ 941 , 421 ]
# # s_1 = [ 1298 , 345 ]
# # s_2 = [ 1320 , 370 ]
# # deposit = [ 986 , 485 ]
#
# def blow():
#     # for i in range(10):
#     #start at furnace
#     if random.randint(0,8) == 70:
#         print('pause')
#         time.sleep(3 + random.random())
#     pg.moveTo(click_bank[0]+random.randint(-2,2),click_bank[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.5+random.random()/10)
#
#     pg.moveTo(deposit_glass_item[0]+random.randint(-2,2),deposit_glass_item[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(1.2+random.random()/10)
#
#     pg.moveTo(bank_1[0]+random.randint(-2,2),bank_1[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(.65+random.random()/10)
#
#     # pg.moveTo(bank_2[0]+random.randint(-2,2),bank_2[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
#     # pg.click()
#     # time.sleep(.65+random.random()/10)
#
#     pg.press('esc')
#     time.sleep(.3)
#     pg.moveTo(_00[0]+random.randint(-2,2),_00[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(.8+random.random()/10)
#
#     pg.moveTo(_01[0]+random.randint(-2,2),_01[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
#     pg.click()
#     time.sleep(.8+random.random()/10)
#
#     pg.press('7')
#     time.sleep(49+random.random()/10)
#     #
#     # for j in range(10):
#     #     pg.moveTo(s_1[0]+random.randint(-2,2),s_1[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#     #     pg.click()
#     #     time.sleep(3.6+random.random()/10)
#     #     pg.moveTo(s_2[0]+random.randint(-2,2),s_2[1]+random.randint(-2,2),.2+random.random()/2,pg.easeInQuad)
#     #     pg.click()
#     #     time.sleep(3.6+random.random()/10)
#     # pg.moveTo(deposit[0]+random.randint(-2,2),deposit[1]+random.randint(-5,5),.2+random.random()/2,pg.easeInQuad)
#     # pg.click()
#     # time.sleep(5+random.random()/10)
#
#
# #
# # def move_through_inv(RR,shuffle,reverse,click):
# #     tween_delay = random.random()/7.5
# #     # IF WANT TO SHUFFLE
# #     if shuffle == True:
# #         coin_flip = random.randint(0,1)
# #         if coin_flip == 0:
# #             random.shuffle(RR)
# #     # IF WANT TO REVERSE
# #     if reverse == True:
# #         coin_flip = random.randint(0,1)
# #         if coin_flip == 0:
# #             RR.reverse()
# #
# #     for pos in RR:
# #         move_delay = random.random()/2
# #         pg.moveTo(pos[0]+random.randint(-2,2),pos[1]+random.randint(-2,2),tween_delay,pg.easeInQuad)
# #         if click == True:
# #             pg.click()
# #         time.sleep(move_delay)
#
# for i in tqdm(range(invs)):
#     t1 = time.time()
#     for k in range(9):
#         blow()
#     # if i % 3 == 0:
#     #     move_through_inv(RR[1:],shuffle=True,reverse=True,click=True)
#     # else:
#     #     chance = random.randint(0,1)
#     #     if chance == 0:
#     #         move_through_inv(RR[1:],shuffle=False,reverse=False,click=True)
#     #     else:
#     #         move_through_inv(RR[1:],shuffle=False,reverse=True,click=True)
#     # print(i,time.time()-t1, pg.position())
