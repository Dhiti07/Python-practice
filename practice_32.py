# Tower of Hanoi

def tower_of_hannoi(n,source,destination,auxillary):
    if(n==0):
        return
    if(n==1):
        print(source,'-->',destination)
        return
    tower_of_hannoi(n-1,source,auxillary,destination)
    print(source,'-->',destination)
    tower_of_hannoi(n-1,auxillary,destination,source)
    #n = int(input("Enter the value of n"))
    n = 3
    tower_of_hannoi(n,'source','destination','auxillary')