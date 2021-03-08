import numpy as np
import random
def test(L,R,B):
    num = 2*L - 2
    i = 10000
    while (i):
        numbers = 1
        t = 1
        km = 0
        kn = 0
        actions = ''
        for i in np.arange(num):
            flag = random.choice([True, False])  # right  down
            if flag and km < (L - 1) and kn < (L - 1):
                actions = actions + 'R'
                numbers += t
                km = km + 1
            elif not flag and km < (L - 1) and kn < (L - 1):
                actions = actions + 'D'
                t = t + 1
                numbers += t
                kn = kn + 1

            elif km >= (L - 1):
                actions = actions + 'D'
                t = t + 1
                numbers += t
                kn = kn + 1

            elif kn >= (L - 1):
                actions = actions + 'R'
                numbers += t
                km = km + 1

        i=i-1










test(5,12,13)

