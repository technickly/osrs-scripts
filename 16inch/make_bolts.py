import pyautogui as pg
import random
import time
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

for i in range(300):
    pg.moveTo(_00[0]+random.randint(-1,1),_00[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    time.sleep(.1+random.random()/2)
    pg.click()
    time.sleep(.1+random.random()/5)
    pg.click()
    pg.moveTo(_01[0]+random.randint(-1,1),_00[1]+random.randint(-1,1),.2+random.random()/2,pg.easeInQuad)
    time.sleep(.1+random.random()/2)
    pg.click()
    time.sleep(.1+random.random()/5)
    pg.click()
    time.sleep(.1+random.random()/5)
