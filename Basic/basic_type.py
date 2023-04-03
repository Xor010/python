# string
s_0 = 'A B C '
s_1 = "d e f "
s_2 = '''
        G 
          h 
            i
      '''
# or can use as comment
'''
    this is comment
'''
# print using format string
print(f'this is formate string {s_2}')
# print with concatenation
print(s_0+s_2)  
# repeat 3 times 
print(s_0 * 3)
# some methods for str [Search in google python string method]
print(s_0.upper()) # s_0.isupper --> return boolean
print(s_0.lower()) # s_0.islower --> return boolean
print(s_0.title()) # s_0.istitle --> return boolean
print(s_0.replace('A', 'D'))
print(s_0.split(' ')) #<-- return string as list

lisa = [1,2,3,4,11] #<-- Create list
tula = (1,2,45.30,7,44,6) #<-- Create tuple

'''
print items it's work with List and Tuple and Strings
'''
print(lisa[0]) #<-- print list items by INDEX
print(lisa[-1]) #<-- print list last items by INDEX
print(lisa[0:3]) #<-- print slice of list by INDEX
'''
add to List 
'''
print(lisa)
lisa.insert(0,34) #<-- add into First index of list 
lisa.append(333) #<-- add into last index of list
lisa[4] = 4000 #<-- change value by index
print(lisa)
'''
remove From List 
'''
lisa.pop() #<-- print & remove
lisa.remove(11) # <-- remove by value
del lisa[3]
print(lisa)
'''
sort list
'''
lisa.sort()
print(lisa)
lisa.sort(reverse=True)
print(lisa)
'''
Get min max and len for list tuple ans also str
'''
min(lisa)
print(max(tula))
print(len(s_2))

# convert tuple to list and modify the re-tuple  it T = tuple(x)
x = list(tula) #<-- make tuple as list 
x.append('add this str in the end')
T = tuple(x)
print(T)
'''
dictionary
{key:value, key:value}
'''
dic = {'A': 1, 'B':2}
dic.items() #<-- get all keys and values as list of tuples
dic.keys() #<-- print all keys
dic.values() #<- print all values
print(dic['A']) #<-- get value By Key

for key in dic: #<-- loop into dictionary and get all keys
    print(key)
for val in dic.values(): #<-- loop into dictionary and get all values
    print(val)
for key, val in dic.items(): #<-- loop into dictionary and get all values
    print(f'{key}, {val}')
