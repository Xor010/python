X = 10
try:
    z = 10/0
except Exception:
    print('no way')
else:
    print(z)
finally:
    print('this is finally message')

