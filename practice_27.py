#checking if the list is sorted or not using recursion
def checksorted(l1):
    if(len(l1)==0 or len(l1)==1):
        return True
    if(l1[0]< l1[1]): # we did the checking 1st becasue why to continuosly do recrsion if the 1st element is not sorted
        return checksorted(l1[1:]) # we have to check for the 1st element as well thats why we are performing slicing
    else:
        return False

print(checksorted([20,5,7,9,10]))