def mergeSort(arr,low,high):
    if((high-low+1)>1):
        mid=int((low+high)/2)
        mergeSort(arr,low,mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)
        #return arr
        
def merge(arr,low,mid,high):
    temp1=[]
    temp2=[]
    len1=mid-low+1
    len2=high-mid
    
    for i in range(low,mid+1):
        temp1.append(arr[i])
    for j in range(mid+1,high+1):
        temp2.append(arr[j])
    t1=0
    t2=0
    a_low=low
    while(t1!=len1 and t2!=len2):
        if(temp1[t1]<temp2[t2]):
            arr[a_low]=temp1[t1]
            t1=t1+1
            a_low=a_low+1
        else:
            arr[a_low]=temp2[t2]
            t2=t2+1
            a_low=a_low+1
    while(t1!=len1):
        arr[a_low]=temp1[t1]
        t1=t1+1
        a_low=a_low+1
    
    while(t2!=len2):
        arr[a_low]=temp2[t2]
        t2=t2+1
        a_low=a_low+1
        #print(arr)
    #return arr
        
    
arr=[2,1,51,6,3,8,0]
n=7
mergeSort(arr,0,n-1)
print(arr)
    
