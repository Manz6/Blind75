def buystocks(arr):
    l=0
    r=1
    res=0
    while r<len(arr):
        if arr[l]<arr[r]:
            profit=arr[r]-arr[l]
            res=max(res,profit)
        else:
            l=r
        r+=1
    return res
print(buystocks([7,1,2,3,4,6,0,6]))