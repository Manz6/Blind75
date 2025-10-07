#1. Two Sum
def twosum(nums,target):
    prevmap={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in prevmap:
            return[prevmap[diff],i]
        prevmap[n]=i
    return
print(twosum([1,2,3,4,5],4))