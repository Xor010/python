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
print(s_2 * 3)
# some methods for str [Search in google python string method]
print(s_0.upper()) # s_0.isupper --> return boolean
print(s_0.lower()) # s_0.islower --> return boolean
print(s_0.title()) # s_0.istitle --> return boolean
print(s_0.replace('A', 'D'))
print(s_0.split(' '))
