o  = [1,2,3,4,5]
x  = 1
xx = 2
print (f' x  {x}')
'''Basic of def .. (Functions) in python'''
def def_name(para1 , para2, para3):
    global x 
    x = 100
    print(x)
    pass
    pass
    pass
    return para1 + para2
'''
parameter in python have 4 type
'''
# 1 - Require.  
def def_name_1(para1, para2):
    pass
    pass
    return
# require way --> def_name(para1, para2)

# 2 - Keyword  : change passion
def def_name_2(para1, para2):
    pass
    pass
    return
# Keyword way --> def_name(para2 = value , para1 = value)
# 3 - default 
def def_name_3(para1 = 1, para2 = 2 ):
    pass
    pass
    return
#default way --> in this way if you not add any value parameter will have the default value

# 4.0 - parameter value unknown value length
def def_name_4_0(para1, *para2): # <-- tow para
    return (sum(para2) + para1) #<-- Keyword way call
# def unknown value length call way
print(def_name_4_0(1000, 3, 5, 60))
# 4.1 - parameter value unknown value length
def def_name_4_1(*para2): #<-- one para
    return (sum(para2)) #<-- Keyword way call
# def unknown value length call way
print(def_name_4_1(1000, 3, 5, 60))

# global var

print(def_name(100,50,7))
print (f' x from function {x}')