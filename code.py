a=int(input())
b=[]
c=[]
f=0
for i in range (a):
    b.append(int(input()))
for i in b:
    if i not in c:
        c.append(i)
        f=1
if(f==0):
    print("unique")
else:
    print(c[0])
