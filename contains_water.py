#11. Container With Most Water
def contains(arr):
    res=0
    l=0
    r=len(arr)-1
    while l<r:
        area=(r-l)*(min(arr[l],arr[r]))
        res=max(res,area)
        if arr[l]<arr[r]:
            l+=1
        else:
            r-=1
    return res
print(contains([1,7,2,5,4,7,3,6]))