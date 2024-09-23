a=input()
numN=''
numE=''
numS=''
numW=''
d=''
ans=''
for i in range(len(a)):
    if a[i]=="N":
        numN=numN+d
        d=''
    elif a[i]=="E":
        numE=numE+d
        d=''
    elif a[i]=="S":
        numS=numS+d
        d=''
    elif a[i]=="W":
        numW=numW+d
        d=''
    else:
        d=d+a[i]
numE,numS,numN,numW=int(numE),int(numS),int(numN),int(numW)
if numE>numW:
    c=str(numE-numW)
    ans=ans+c+"E"
elif numE<numW:
    c=str(numW-numE)
    ans=ans+c+"W"
if numS>numN:
    c=str(numS-numN)
    ans=ans+c+"S"
elif numS<numN:
    c=str(numN-numS)
    ans=ans+c+"N"
print(ans)
