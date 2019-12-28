import threading
import random
import os
import time
import msvcrt


tree = list(open('tree.txt').read().rstrip())

print(''.join(tree))
yellow = []
blue = []
green = []
red = []

def colored_dot(color):
    if color == 'red':
        return f'\033[91m◙\033[0m'
    if color == 'green':
        return f'\033[92m◙\033[0m'
    if color == 'yellow':
        return f'\033[93m◙\033[0m'
    if color == 'blue':
        return f'\033[94m◙\033[0m'
    pass


def lights(color,index):
    off = True
    while True:
        for idx in index:
            tree[idx] = colored_dot(color) if off else '◙'
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        off = not off
        time.sleep(random.uniform(0.5,1.5))

    pass

for i,c in enumerate(tree):
    if c == 'Y':
        yellow.append(i)
        tree[i] = '◙'
    if c == 'B':
        blue.append(i)
        tree[i] = '◙'
    if c == 'G':
        green.append(i)
        tree[i] = '◙'
    if c == 'R':
        red.append(i)
        tree[i] = '◙'

print(''.join(tree))

ty = threading.Thread(target=lights,args=('yellow',yellow))
tb = threading.Thread(target=lights,args=('blue',blue))
tg = threading.Thread(target=lights,args=('green',green))
tr = threading.Thread(target=lights,args=('red',red))

for t in [ty,tr,tb,tg]:
    t.start()