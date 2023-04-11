def xv(names):
    res = [x for x in names]
    print(res)
    return

def xvv(names):
    res = [x for x in names if len(str(x)) > 3  ]
    print(res)
    return

def xvvv(names):
    res = [x if len(str(x)) > 3 else 0 for x in names ]
    print(res)
    return

xvvv([90,232,0])
xvv([1,23,24243])
xv([1,23,24243])

l = [1,2,3,'ahmed', 'nour']
d = [v if v == 3 or v == 'nour' else 'none' for v in l]
print(d)
l = [1,2,3,'ahmed', 'nour']
[print(v) if v == 3 or v == 'nour' else 'none' for v in l ]
#print('do' if not 1 else print('False'))
t= 50
print('ok') if t == 5 else print('o')
t = [x for x in range(5,101,5) ]
print(t)
tt = [x if x%2==0  else x for x in range(5,101,5)]
print(tt)