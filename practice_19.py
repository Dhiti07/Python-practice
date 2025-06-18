def linear_search(arr,target):
    size = len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
    return -1
my_list = [2,5,9,3,11,19]
target = int(input("what's the target"))
result = linear_search(my_list,target)
print(result)