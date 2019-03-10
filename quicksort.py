def quicksort(arr,low,high):
    if((high-low)<=0):
        return
    if((high-low)==1):
        if(arr[low]>arr[high]):
            temp=arr[low]
            arr[low]=arr[high]
            arr[high]=temp
            return
        
    pivot=partition(arr,low,high)
    quicksort(arr,low,pivot-1)
    quicksort(arr,pivot+1,high)
def partition(arr,low,high):
    pindex=high
    findex=low
    lindex=high-1
    while(findex<lindex):
        if(arr[findex]>arr[pindex] and arr[lindex]<arr[pindex]):
            #swap
            temp=arr[findex]
            arr[findex]=arr[lindex]
            arr[lindex]=temp
            findex +=1
            lindex -=1
        elif(arr[findex]>arr[pindex]):
            lindex -=1
        elif(arr[lindex]<arr[pindex]):
            findex +=1
        elif(arr[findex]<arr[pindex] and arr[lindex]>arr[pindex]):
            findex +=1
            lindex -=1
       
       
    if(arr[findex]>arr[pindex]):
        temp=arr[pindex]
        arr[pindex]=arr[findex]
        arr[findex]=temp
        return findex
    else:
        temp=arr[findex+1]
        arr[findex+1]=arr[pindex]
        arr[pindex]=temp
        return findex+1
arr=[1,3,0,5,2,8,7]
quicksort(arr,0,6)
print(arr)

        
        
            
            
    
