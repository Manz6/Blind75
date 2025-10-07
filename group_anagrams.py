#49. Group Anagrams
from collections import defaultdict
def group(nums):
    result=defaultdict(list)
    for s in nums:
        count=[0]*26
        for c in s:
            count[ord(c)-ord("a")] +=1
        result[tuple(count)].append(s)
    return result.values()

print(group(["act","pots","tops","cat","stop","hat"]))