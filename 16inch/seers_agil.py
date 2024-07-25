import time
import pyautogui as pg
import sys
import random
import os
from tqdm import tqdm

t1 = time.time()

def run_laps(laps_):
    # laps_ = 9
    wall_1 = [ 1308 , 309 ]
    gap_1 = [ 1251 , 355 ]
    rope_1 = [ 1281 , 393 ]
    gap_2 = [ 1303 , 388 ]
    # [ 1320 , 365 ]
    gap_3 = [ 1251 , 382 ]
    # [ 1253 , 360 ]
    edge_final = [ 1304 , 377 ]
    run_to_tile = [ 1415 , 296 ]
    noise = 0
    move_noise = .1


    for i in tqdm(range(laps_)):
        run_loop = time.time()
        noise = random.randint(-1,1)
        noise = 0
        move_noise = random.randint(1,2)/10

    #FROM TILE MARKER TO WALL
        pg.moveTo(wall_1[0]+noise,wall_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(4+random.random()/10.)

        # os.system('say a')
    #JUMP FIRST GAP
        time.sleep(4+random.random()/10.)
        pg.moveTo(gap_1[0]+noise,gap_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say b')


    #CROSS ROPE
        time.sleep(6.5+random.random()/10.)
        pg.moveTo(rope_1[0]+noise,rope_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say c')

    #JUMP SECOND GAP
        time.sleep(10+random.random()/10.)
        pg.moveTo(gap_2[0]+noise,gap_2[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say d')

    #JUMP THIRD GAP
        time.sleep(6.5+random.random()/10.)
        pg.moveTo(gap_3[0]+noise,gap_3[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say e')

    #JUMP EDGE
        time.sleep(6+random.random()/10.)
        pg.moveTo(edge_final[0]+noise,edge_final[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say f')

    #RUN TO START TO FINISH
        time.sleep(4+random.random()/10.)
        pg.moveTo(run_to_tile[0]+noise,run_to_tile[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(10+random.random()/10.)
        # os.system('say g')
        print('Run Loop: ',((time.time()-run_loop)))

def pickup_marks():
        print('marks')
        # laps_ = 9
        wall_1 = [ 1327 , 270 ]
        m0 = [ 1302 , 328 ]
        gap_1 = [ 1271 , 341 ]
        m1 = [ 1290 , 346 ]
        m2 = [ 1297 , 342 ]
        rope_1 = [ 1339 , 365 ]
        m3 = [ 1327 , 335 ]
        gap_2 = [ 1311 , 373 ]
        gap_3 = [ 1245 , 360 ]
        m4 = [ 1277 , 365 ]
        edge_final = [ 1324 , 378 ]
        run_to_tile = [ 1456 , 255 ]
        noise = 1
        move_noise = .1

        # t1 = time.time()

    # for i in tqdm(range(laps_)):
        mark_loop = time.time()
        noise = random.random()/5
        move_noise = random.randint(1,2)/10

    #FROM TILE MARKER TO WALL
        pg.moveTo(wall_1[0]+noise,wall_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # time.sleep(6+random.random()/10.)
    #TO M0
        time.sleep(7+random.random()/10.)
        pg.moveTo(m0[0]+noise,m0[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()

    #JUMP FIRST GAP FROM M0
        time.sleep(2+random.random()/10.)
        pg.moveTo(gap_1[0]+noise,gap_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()

        # os.system('say b')
    #FROM GAP1 TO M1
        time.sleep(6+random.random()/10.)
        pg.moveTo(m1[0]+noise,m1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
    #FROM M1 TO M2
        time.sleep(3+random.random()/10.)
        pg.moveTo(m2[0]+noise,m2[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()

    #FROM M2 CROSS ROPE
        time.sleep(3.5+random.random()/10.)
        pg.moveTo(rope_1[0]+noise,rope_1[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say c')

    # FROM ROPE TO M3
        time.sleep(8+random.random()/10.)
        pg.moveTo(m3[0]+noise,m3[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
    #FROM M3 JUMP SECOND GAP
        time.sleep(5+random.random()/10.)
        pg.moveTo(gap_2[0]+noise,gap_2[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say d')

    #JUMP THIRD GAP
        time.sleep(8+random.random()/10.)
        pg.moveTo(gap_3[0]+noise,gap_3[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say e')

    #FROM GAP JUMP M4
        time.sleep(6+random.random()/10.)
        pg.moveTo(m4[0]+noise,m4[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say d')

    #JUMP EDGE
        time.sleep(3+random.random()/10.)
        pg.moveTo(edge_final[0]+noise,edge_final[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        # os.system('say f')

    #RUN TO START TO FINISH
        time.sleep(4+random.random()/10.)
        pg.moveTo(run_to_tile[0]+noise,run_to_tile[1]+noise,.5+move_noise,pg.easeInQuad)
        pg.click()
        time.sleep(10+random.random()/10.)
        # os.system('say g')
        print('Pick up Loop: ',((time.time()-mark_loop)))

for j in range(20):
    loop = time.time()
    laps_ = random.randint(8,9)
    print("Laps: ",laps_)
    run_laps(laps_)
    print("Picking up marks")
    pickup_marks()
    print('Iter Loop: ',((time.time()-loop)/60))
print('Finished in: ',(time.time()-t1)/60)
os.system('say finished')
