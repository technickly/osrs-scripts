import time
import random
import os
import sys

num_invs = int(sys.argv[1])
#CAMERA 40
#RUNELITE N ZOOMED OUT 765X550
#START AT DKP RING
_00 = 1530, 350; _01 = 1575, 350; _02 = 1620, 350; _03 = 1660, 350
_10 = 1530, 390; _11 = 1575, 390; _12 = 1620, 390; _13 = 1660, 390
_20 = 1530, 425; _21 = 1575, 425; _22 = 1620, 425; _23 = 1660, 425
_30 = 1530, 465; _31 = 1575, 465; _32 = 1620, 465; _33 = 1660, 465
_40 = 1530, 500; _41 = 1575, 500; _42 = 1620, 500; _43 = 1660, 500
_50 = 1530, 535; _51 = 1575, 535; _52 = 1620, 535; _53 = 1660, 535
_60 = 1530, 570; _61 = 1575, 570; _62 = 1620, 570; _63 = 1660, 570

RR = [  _12,_13,
        _20,_21,_22,_23,
        _30,_31,_32,_33 ]


karam_fish = [ 1286 , 280 ]
karam_to_ring = [ 1309 , 462 ]
chasm_tele_click = [ 1594 , 389 ]
confirm = [ 1189 , 395 ]

ring_to_bank = [ 1609 , 512 ]
# fish_barrel = [ 1604 , 294 ]

bank_to_ring = [ 917 , 205 ]


fish_tele_click = [ 1577 , 435 ]



import pyautogui

#
for i in range(num_invs):
    karam_inv =  RR[random.randint(0,len(RR)-1)]

    print(i)
    #From Fairy Ring on Karajama
    pyautogui.moveTo(karam_fish[0],karam_fish[1],.5+random.random()/2.5,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(random.randint(130,145))
    # os.system('say done fishing')

    #From fish to Ring
    pyautogui.moveTo(karam_to_ring[0],karam_to_ring[1],.5+random.random(),pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(4.5+random.random()/2)

    # pyautogui.moveTo(karam_to_ring[0],karam_to_ring[1],random.random()/2,pyautogui.easeInQuad)
    # pyautogui.click()
    # time.sleep(4+random.random()/5)

    # Choose Chasm

    pyautogui.moveTo(chasm_tele_click[0],chasm_tele_click[1],.4+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(2+random.random()/5)


    pyautogui.moveTo(confirm[0],confirm[1],.4+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(4.5+random.random()/5)




    pyautogui.moveTo(ring_to_bank[0],ring_to_bank[1],.2+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(10+random.random())


    pyautogui.moveTo(karam_inv[0],karam_inv[1],.3+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1.35+random.random()/10)

    print("Deposited")
    pyautogui.press('esc')
    time.sleep(.8+random.random()/10)
    pyautogui.moveTo(bank_to_ring[0],bank_to_ring[1],.2+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(10+random.random())


    # Choose Karajama

    pyautogui.moveTo(fish_tele_click[0],fish_tele_click[1],.25+random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1.5+random.random())


    pyautogui.moveTo(confirm[0],confirm[1],random.random()/2,pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(4.5+random.random()/5)



    # pyautogui.moveTo(d[0],d[1],random.random()/2,pyautogui.easeInQuad)
    # pyautogui.click()
    # time.sleep(.6)
    # pyautogui.moveTo(k[0],k[1],random.random()/2,pyautogui.easeInQuad)
    # pyautogui.click()
    # time.sleep(.6)
    # pyautogui.click()
    # time.sleep(.6)
    #
    # pyautogui.moveTo(teleport[0],teleport[1],random.random()/2,pyautogui.easeInQuad)
    # pyautogui.click()
    # time.sleep(4+random.randint(-1,1))
    #

#     #Done Fishing, To Zanaris
#     pyautogui.moveTo(fish_to_fairy_x,fish_to_fairy_y,random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     print("At Zanaris")
#     time.sleep(6)
#     #At Zanaris, Move halfway to bank
#     pyautogui.moveTo(ring_to_mid_x,ring_to_mid_y,random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     print("Halfway To Bank")
#     time.sleep(11)
#     #At Zanaris halfway, move to bank
#     pyautogui.moveTo(mid_to_bank_x,mid_to_bank_y,random.random(),pyautogui.easeInQuad)
#     pyautogui.click()
#     print("To the bank")
#     time.sleep(7)
#
#     #At bank tab deposit karawambam
#     pyautogui.moveTo(deposit_x,deposit_y,random.random(),pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(1.2)
#     print("Deposited")
#     pyautogui.press('esc')
#
#     #At bank, move halfway to ring
#     pyautogui.moveTo(bank_to_mid_x,bank_to_mid_y,random.random(),pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(11)
#
#     #Halfway to ring, move to ring
#     pyautogui.moveTo(mid_to_ring_x,mid_to_ring_y,random.random()/2,pyautogui.easeInQuad)
#     pyautogui.click()
#     time.sleep(8)
#






#
#
# move_to_fish()
# pyautogui.click()
# time.sleep(20)
# move_fish_to_fairy()
# pyautogui.click()
