def ee(L):
    add_list = []
    for i in range(len(L)):
        ls = L[i][i]
        add_list.append(ls)
    return add_list


L = [[1, 2], [3, 4]]
ee(L)
print(ee(L))