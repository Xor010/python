o  = [1,2,3,4,5]
x  = 1
xx = 2
'''Basic of def .. (Functions) in python'''
def def_name(para1 , para2, para3 ):
    pass
    pass
    pass
    return
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

# 4 - parameter value unknown value length
def def_name_4_1(para1, *para2):
    return (sum(para2) + para1) #<-- Keyword way call
# def unknown value length call way
print(def_name_4_1(1000, 3, 5, 60))
