#347. Top K Frequent Elements 
def topk(nums,k):
    count={}
    for num in nums:
        count[num]=1+count.get(num,0)
    arr=[]
    for num,cnt in count.items():
        