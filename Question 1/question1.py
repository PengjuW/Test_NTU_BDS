import random

import numpy as  np

def get_Actions(m,n,summedNumbers):
    # matrix = np.ones((m,n)).T*np.arange(1,m+1)
    # matrix = matrix.T
    num = m + n-2

    actions = ''
    while(True):
        numbers = 1
        t = 1
        km = 0
        kn = 0
        actions = ''
        for i in np.arange(num):
            flag = random.choice([True, False])   #right  down
            if flag and km <(m-1) and kn<(n-1):
                actions  = actions+'R'
                numbers += t
                km = km+1
            elif not flag and km <(m-1) and kn<(n-1):
                actions = actions+'D'
                t = t + 1
                numbers += t
                kn= kn+1

            elif km>=(m-1):
                actions = actions + 'D'
                t = t + 1
                numbers += t
                kn = kn + 1

            elif kn>=(n-1):
                actions = actions + 'R'
                numbers += t
                km = km + 1
        if numbers==summedNumbers:
            return actions
            break
fop = open('output_question_1.txt','ab')
actions = get_Actions(9,9,65) # 65, 72, 90, 110.
fop.write(actions+'\n')
actions= get_Actions(9,9,72)
fop.write(actions+'\n')
actions = get_Actions(9,9,90)
fop.write(actions+'\n')
actions = get_Actions(9,9,110)
fop.write(actions+'\n')

#
actions = get_Actions(90000,100000,87127231192)
fop.write(actions+'\n')
actions = get_Actions(90000, 100000, 5994891682)
fop.write(actions+'\n')