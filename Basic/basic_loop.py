#loop
#   - while [until]
#   - for   [for every pice in unite ]
'''
WHILE
'''
x= 0
# - infinity loop
#while x <=10:
    #pass#print('this is infinite loop')
# - condition loop
while x <=10:
    print(x)
    x+=1
# - while loop in one line
while x <= 10 : print(x); x+=1

'''
FOR
'''
# - for basic
for l in 'python cool language':
    print(l)
# - for with range(start, stop, step) - range(start, stop) - range(start) 
for n in range(10):
    print(n)
'''
nested loop
'''
for x in range(1,4):
    for y in range(2,5):
        print(y, x)
'''
control loop
'''
# Stop [break]
for x in range(10):
    if x == 4:
        break
    print(f'this is break {x}')

# continue
for x in range(10):
    if x == 4:
        continue
    print(f'this is continue {x}')
        
