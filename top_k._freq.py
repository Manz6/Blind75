#347. Top K Frequent Elements 
def topk(nums,k):
    count={}
    freq=[[] for i in range(len(nums)+1)]
    for num in nums:
        count[num]=1+count.get(num,0)
    for num,cnt in count.items():
        freq[cnt].append(num)
    res=[]
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res

print(topk([1,3,2,2,3,4,5],2))