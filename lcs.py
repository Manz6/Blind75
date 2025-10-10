#128. Longest Consecutive Sequence
def lcs(arr):
    s=set(arr)
    longest=0
    for n in s:
        if (n-1) not in s:
            length=0
            while (n+length) in s:
                length+=1
            longest=max(longest,length)
    return longest
print(lcs([1,2,3,100,4,200]))