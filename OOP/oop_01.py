class cal:
    def __init__(self, name):
        print(f'Welcome , {name}')
        return
    def pl(self,x,*y):
        return x+sum(y)
    def mu(self,x,*y):
        return x-y
class cal_pluse(cal):
    def power(self,x,*y):
        return x**sum(y)

name = input('Enter Your Name: ')
if name != 'admin':
    userFree = cal(name)
    pl = userFree.pl(2,7,3,4,423,2231)
    print(pl)
else:
    userPluse = cal_pluse(name)
    powe = userPluse.power(12,1212,12)
    print(powe)
