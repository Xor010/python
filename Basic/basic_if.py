x   = 1
xx  = 2
xxx = 3
l   = [1,2,3,'this is list']
'''
use [any - all - in - not] with if
'''

if any([x == 1, xx == 3 ]):
    print('yes any of them TRUE')
if all([x== 1 ,xx ==2]):
    print('yes all of them TRUE')
if 'this is list' in l:
    print('TRUE')
if '4' not in l:
    print('TRUE')
'''
use elif with else
'''
if x == 3:
    print(3)
elif xx == 1:
    print(1)
else:
    print('this is else')