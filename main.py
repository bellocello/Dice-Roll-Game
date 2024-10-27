from os import system
system('clear')
import random

def diceroll():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    z = random.randint(1, 6)
    # create a dictionary with each key (the number on the dice) mapping to a tuple of strings that each make up a row of the dice
    diceface = {1:('-' * 11, '|         |', '|    o    |', '|         |', '-' * 11), 2:('-' * 11, '|    o    |', '|         |', '|    o    |', '-' * 11), 3:('-' * 11, '|    o    |', '|    o    |', '|    o    |', '-' * 11), 4:('-' * 11, '|  o   o  |', '|         |', '|  o   o  |', '-' * 11), 5:('-' * 11, '|  o   o  |', '|    o    |', '|  o   o  |', '-' * 11), 6:('-' * 11, '|  o   o  |', '|  o   o  |', '|  o   o  |', '-' * 11)}
    print(diceface[x][0], diceface[y][0], diceface[z][0])
    print(diceface[x][1], diceface[y][1], diceface[z][1])
    print(diceface[x][2], diceface[y][2], diceface[z][2])
    print(diceface[x][3], diceface[y][3], diceface[z][3])
    print(diceface[x][4], diceface[y][4], diceface[z][4])
    return x, y, z

ans = input('Welcome to the Roll 3 Dice Game!!! \nRoll the Dice? (Y/N) ')
run = 1
you = 0
comp = 0
while ans.upper() == 'Y':
    print("Let's roll your dice!!!")
    user = diceroll()
    print("\nIt's AI's turn to roll the dice!!!")
    ai = diceroll()
    print(f'YOU ({user[0]+user[1]+user[2]}) {user[0]},{user[1]},{user[2]} - {ai[0]},{ai[1]},{ai[2]} ({ai[0]+ai[1]+ai[2]}) AI')
    if user[0]+user[1]+user[2] > ai[0]+ai[1]+ai[2]:
        you += 1
        print('\nYou win!!!')
    elif user[0]+user[1]+user[2] < ai[0]+ai[1]+ai[2]:
        comp += 1
        print('\nAI wins...')
    else:
        print('\nDraw?!!')
    # fix win ratio in case of draw on first run
    if (you == 0 & comp == 0):
        winRatio = 0
    else:
        winRatio = you/(you+comp)
    print(f'GRAND TOTAL AFTER THE RUN #{run}: YOU {you} - {comp} AI (Win Ratio: {winRatio:.3f})')
    ans = input('Roll the Dice? (Y/N) ')
    run += 1
print('See ya!!!')