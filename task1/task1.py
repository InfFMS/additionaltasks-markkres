a=int(input())
b=int(input())
if b<a:
    b,a=a,b
if b%2==0:
    b-=1
if a%2==0:
    a-=1
print(int((b-a)/2))
