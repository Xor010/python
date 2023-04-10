numlist = [1,2,44,67,4,7,7,2345,23553,67]
numtuple= (12,234,234,34222,3467,66,87,65)
string  = 'This Is String '
'''
print - Add - remove - create from range
'''
# - print [All]
print(string[1])
print(string[:3])
print(numlist[3:6])
print(numtuple[-1])
print('''
            this is print
        ''')
print('this is concatenate '+ string)
print(f'print using format string :- {string}')
print(f'multiply string :-  {string * 3} ')

# - Add [list]
numlist.append(2424) # take value
numlist.insert(0,2000000) # take Index, value
numlist[2] = 20000000 # same as insert
print(numlist)

# - remove [list]
numlist.remove(20000000) # take vale
numlist.pop(0) # take index
del numlist[0] # take index

# - sorting [list]
numlist.sort()
numlist.reverse()
numlist.sort(reverse=True)

# - helpful method
string.upper()
string.lower()
string.title()
string.replace('e','3')
string.split(' ') # <-- return string as list
print(min(numtuple))
print(max(numlist))
print(len(string))
print(abs(-44))
print(round(12.123,1))
print(any([True,False,False,True]))
print(all((True,True,False,True)))
x = zip((1, 22, 3), [4, 5, 6])
print(list(x))
v = enumerate(['a', 'b', 'c'],3)
print(list(v))
sorted((6,2,6,9,1,5,0))
xb = reversed([2,7, 9, 1, 5])
print(list(xb))
# reduce , filter , map

# - create list from range
print(list(range(100)))
print(list(range(90 , 100)))
print(list(range(60,100,5)))

# - convert from tuple to list for modify tuple
xlist = list(numtuple)
print(numtuple)
xlist.append(1212112)
xtuple = tuple(xlist)
print(xtuple)
# - convert from list to str
lop = ['i', 'love', 'god']
print(' '.join(lop))
'''
dictionary
d = {key1: 'value1', key2:'value2'}
'''
dicx = {'ahmed' : 90, 'mohamed': 100, 9000:'mahmoud'}
print(dicx.keys())
print(dicx.values())
print(dicx.items())
for k in dicx: #<-- for will print only keys like [for k in dicx.keys()]
    print(k)
# ---- GET KEYS WITH VALUES
for k,v in dicx.items():
    print(k,v)
