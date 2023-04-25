x   = 1
xx  = 2
xxx = 3
xv  = 5000
Rty = 'test'

if x == 1 and xxx == 4:
    print(False)
    if xx == 2:
        print(True)
        if xxx==3:
            print(0)
elif xv  == 5:
    print('xv == ', xv)
else :
    print('this is else')

#def
'''
* defualt
    def function(x = 't', y=1)
* Keyowrd
    function(x='j')
* def function(var, *lag)

'''
var = 'r'
lag = [1,2,3,4,5,6]
def func(var , *lag):
    print(var)
    for v in lag:
        print (v)
func(var, lag)
print('😅')

