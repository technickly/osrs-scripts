import time
import pyautogui as pg
import sys
import random
import os
from tqdm import tqdm

t1 = time.time()
#camera 900
def run_lap():
    # laps_ = 9
    ladder_1 = [ 1407 , 396 ]
    rope_1 = [ 1324 , 447 ]
    rope_2 = [ 1284 , 379 ]
    ladder_2 = [ 1285 , 382 ]
    edge_1 = [ 1273 , 379 ]
    rope_3 = [ 1274 , 357 ]
    zipeline = [ 1324 , 343 ]
    move_noise = .1


    run_loop = time.time()
    n1 = random.randint(-1,1)
    n2 = random.randint(-1,1)
    move_noise = random.randint(1,2)/10

    pg.moveTo(ladder_1[0]+n2,ladder_1[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(4+random.random()/10.)

    pg.moveTo(rope_1[0]+n2,rope_1[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(20.5+random.random()/10.)

    pg.moveTo(ladder_2[0]+n1,ladder_2[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(2.5+random.random()/10.)


    pg.moveTo(edge_1[0]+n2,edge_1[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(6+random.random()/10.)

    pg.moveTo(rope_3[0]+n1,rope_3[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(20.5+random.random()/10.)


    pg.moveTo(zipeline[0]+n2,zipeline[1]+n1,.5+move_noise,pg.easeInQuad)
    pg.click()
    time.sleep(10+random.random()/10.)


    print('Run Loop: ',((time.time()-run_loop)))


for j in range(20):
    loop = time.time()
    run_lap()
    print('Iter Loop: ',((time.time()-loop)/60))
print('Finished in: ',(time.time()-t1)/60)
os.system('say finished')
