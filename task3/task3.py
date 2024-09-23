m=int(input())
count=1
d=2
while d**2<=m:
    if m%(d**2)==0:
        count=d*d
    d+=1
print(count)
