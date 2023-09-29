def countingSort2(alist,exp10):
    
    order = [0] * len(alist)
    
    count=[0]*10
    
    for i in alist:
        ind = i//exp10
        count[ (ind)%10 ] +=1
        
    for i in range(1,10): 
        count[i] += count[i-1]     
    
    for i in range(len(alist)-1,-1,-1):
        ind = alist[i]//exp10
        order[  count[ (ind)%10 ] -1 ] = alist[i]
        count[ (ind)%10 ] -=1
        
    for i in range(len(alist)):
        alist[i]=order[i]
    
    
def RadixSort(alist):
    mx=max(alist)
    exp10=1
    while mx//exp10 >0:
        countingSort(alist,exp10)
        exp10 *=10

a=[22,33,44,1,2,3,5655,3,777,1000]
RadixSort(a)
print(a)