#238 Product of Array Except Self
def product(arr):
    n=len(arr)
    res=[0]*n
    pre=[0]*n
    suf=[0]*n
    pre[0]=suf[n-1]=1
    for i in range(1,n):
        pre[i]=arr[i-1]*pre[i-1]
    for i in range(n-2,-1,-1):
        suf[i]=arr[i+1]*suf[i+1]
    for i in range(n):
        res[i]=pre[i]*suf[i]
    return res
print(product([1,2,3,4]))


def product_opt(arr):
    res=[1]*(len(arr))
    prefix=1
    for i in range(len(arr)):
        res[i]=prefix
        prefix*=arr[i]
    postfix=1
    for i in range(len(arr)-1,-1,-1):
        res[i]*=postfix
        postfix*=arr[i]
    return res
print(product_opt([1,2,3,4]))