def count_list(lst):
    c = []
    for l in lst:
        c.append(len(str(l)))
    return c
print(count_list([1212,1212,22222,222222,2222222]))