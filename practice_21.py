def selection_sort(lst):
    size = len(lst)
    for i in range(size):
        min = lst[i]
        for j in range(i,size):
            if min > lst[j]:
                min = lst[j]
                lst[i],lst[j] = lst[j],lst[i]
    return lst
lst = []
n = int(input("enter the no. of elments in the array"))
for i in range(n):
    lst.append(int(input("enter the elements")))
print(selection_sort(lst))
