import sys
import time
from implementation import create, display, solve

for i in range(10):
    begin = time.time()
    x = create('puzzles/%d.txt' %i)
    display(x)
    y = solve(x)

    if y:
        print()
        display(y)
    print()
    print('Time = ', time.time()-begin)
    print('**********************************')
    print()
