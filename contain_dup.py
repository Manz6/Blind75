#217. Contains Duplicate
def has_dup(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
print(has_dup([1,2,2,3]))