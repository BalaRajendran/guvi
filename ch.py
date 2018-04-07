a=int(input())
b=int(input())
c=[]
d=[]
l=0
for i in range(a):
    c.append(int(input()))
for i in range(b):
    d.append(int(input()))
for i in c:
    if i in d:
        l=l+1
if l==len(d):
    print("YES")
else:
    print("NO")
