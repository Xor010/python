story1 = '0987654321'
l0 = [story1[i] for i in range(len(story1)-1, -1 ,-1)]
print(''.join(l0))


story2 = ['i','wanna','eat','but','not','Fish']
l1 = [i if i !='not' else '' for i in story2 ]
print(' '.join(l1))
l1 = [i for i in story2 if i !='not'  ]
print(' '.join(l1))


yy = [story1[i] for i in range(len(story1))]
yy.reverse()
print(''.join(yy))

print(''.join(list(reversed(story1))))


def count_list(lst):
    c = [ len(str(i)) for i in lst ]
    return c 
print(count_list([1212,'ds',22222,222222,2222222]))





