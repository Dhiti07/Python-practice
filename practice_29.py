def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  
        quicksort(arr, low, pi - 1)     
        quicksort(arr, pi + 1, high)    
def partition(arr, low, high):
    pivot = arr[low]  
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] 
        else:
            break
    arr[low], arr[j] = arr[j], arr[low] 
    return j
