def heapify(arr,n,i):
    largeele=i
    l=2*i
    r=2*i+1
    if(l<n and arr[l]>arr[largeele]):
        #swap
        largeele=l
    if(r<n and arr[r]>arr[largeele]):
        largeele=r
    if(largeele!=i):
        #swap
        temp=arr[i]
        arr[i]=arr[largeele]
        arr[largeele]=temp
        heapify(arr,n,largeele)


def heapsort(arr,n):

    for i in range(n-1,-1,-1):
        heapify(arr,n,i)
    #last=n-1
    for k in range(n-1,0,-1):
        #swap
        temp=arr[0]
        arr[0]=arr[k]
        arr[k]=temp
        heapify(arr,k,0)

arr=[4,7,-1,3,1,3,57,98,8,0]
heapsort(arr,10)
print(arr)
            









