def binary_search(arr,target):
    size = len(arr)
    start = 0
    end = size - 1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return -1
arr = []
n = int(input("enter the no. of elments in the array"))
for i in range(n):
    arr.append(int(input("enter the elements")))
target = int(input("enter the element to be searched"))
print(binary_search(arr,target))