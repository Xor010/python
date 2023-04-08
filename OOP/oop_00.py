class users():
    def __init__(self ,name):
        print(f'Welcome {name}')
    def color(self ,x):
        co = ['red','yellow']
        return co[x]
class admins(users):
    def control(self,xd):
        x = f'you can control {xd}'
        return x
ahmed = users('ahmed')
print(ahmed.color(1))
amin = admins('ahmos')
print (amin.control('am'))

o= str
print (o.lower('coool'))

bv = list()
bv.append(1)
print(bv)

