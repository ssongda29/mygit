import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

UP = 0
SIDE = 1
DOWN = 2
HIDE = 3
HEIGHT = HIDE + 12

# 배경 초기화 함수
def white_back():
    # 기본 배경
    # 윗부분
    up = ['-' for i in range(26)] # ['-', '-', '-',..., '-', '-']

    # 옆부분
    side_p = []
    for i in range(26):
        side_p.append('|') if i== 0 or i ==25 else side_p.append(' ') 

    # side_p = ['|', ' ', ' ', ..., ' ', ' ', '|']

    side = []
    for j in range(HEIGHT):
        side.append(side_p[:])

    # side = ['|', ' ', ' ', ..., ' ', ' ', '|'] *26

    # 아래부분
    down = ['-' for i in range(26)] # ['-', '-', '-',..., '-', '-']


    return [up,side,down]


# 배경 그리기 함수
def draw_back_ground(ground):
    print(''.join(ground[UP]))
    for i in range(3,len(ground[SIDE])):
        print(''.join(ground[SIDE][i]))
    print(''.join(ground[DOWN]))


# I 블록 
def block_I(ground):
    ground[SIDE][i][11:15] = '■■■■'


# O 블록
def block_O(ground):
    ground[SIDE][i-1][12:14] = '■■'
    ground[SIDE][i][12:14]   = '■■'

# T 블록
def block_T(ground):
    ground[SIDE][i-2][11:14] = '■■■'
    ground[SIDE][i-1][12]     = '■'
    ground[SIDE][i][12]       = '■'

# L 블록
def block_L(ground):
    ground[SIDE][i-2][11]    = '■'
    ground[SIDE][i-1][11]    = '■'
    ground[SIDE][i][11:14]   = '■■■'

# J 블록
def block_J(ground):
    ground[SIDE][i-2][13]    =   '■'
    ground[SIDE][i-1][13]    =   '■'
    ground[SIDE][i][11:14]   = '■■■'

# Z 블록
def block_Z(ground):
    ground[SIDE][i-1][12:14] ='■■'
    ground[SIDE][i][13:15]   = '■■'

# S 블록
def block_S(ground):
    ground[SIDE][i-1][13:15] =  '■■'
    ground[SIDE][i][12:14]    ='■■'








# 배경 초기화
back_ground = white_back()


# 배경 출력
draw_back_ground(back_ground)



block = [block_I,block_O, block_T,block_L,block_J,block_S,block_Z]
current_block = block[random.randint(0,len(block))]
current_block = block_S
current_back_ground = back_ground

i = HIDE
while True :
    current_back_ground = white_back()
    current_block(current_back_ground)
    clear_screen()
    draw_back_ground(current_back_ground)
    time.sleep(1)
    i += 1
    if i == HEIGHT:break