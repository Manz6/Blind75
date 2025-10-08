#271. Encode and Decode Strings

def encode(arr):
    res=""
    for s in arr:
        res+=str(len(s))+"#"+s
    return res
def decode(s):
    res=[]
    i=0
    while i<len(s):
        j=i
        while s[j]!="#":
            j+=1
        length=int(s[i:j])
        res.append(s[j+1:j+1+length])
        i=j+1+length
    return res

print(encode(["manasa","nanama"]))
print(decode("6#manasa3#ama"))