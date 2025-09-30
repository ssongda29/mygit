import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

UP = 0
SIDE = 1
DOWN = 2

# 배경 초기화 함수
def white_back():
    # 기본 배경
    # 윗부분
    up = ['-' for i in range(26)] # ['-', '-', '-',..., '-', '-']
    print(f'up : {up}')

    # 옆부분
    side_p = []
    for i in range(26):
        side_p.append('|') if i== 0 or i ==25 else side_p.append(' ') 

    # side_p = ['|', ' ', ' ', ..., ' ', ' ', '|']

    side = []
    for j in range(12):
        side.append(side_p[:])

    # side = ['|', ' ', ' ', ..., ' ', ' ', '|'] *26

    # 아래부분
    down = ['-' for i in range(26)] # ['-', '-', '-',..., '-', '-']


    return [up,side,down]


# 배경 그리기 함수
def draw_back_ground(back_ground):
    print(''.join(back_ground[0]))
    for i in range(len(back_ground[1])):
        print(''.join(back_ground[1][i]))
    print(''.join(back_ground[2]))


# 배경 초기화
back_ground = white_back()


# 배경 출력
draw_back_ground(back_ground)


# I 블록 
block_i= ['■' for i in range(4)]



current_block = block_i
current_back_ground = back_ground

i=0
while True :
    back_ground = white_back()
    current_back_ground=back_ground[SIDE][i][11:15] = '****'
    clear_screen()
    draw_back_ground(back_ground)
    time.sleep(1)
    i+=1
    if i==12:break