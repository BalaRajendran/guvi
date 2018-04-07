a=int(input())
b=[]
f=[]
j=[]
r=0
for i in range(a):
    b.append(int(input()))
try:
    for i in b:
        if i==0:
            r=1+r
        elif i>=0:
            f.append(i)
        elif i<0:
            j.append(i)
    f.sort()
    sorted(j)
except:
    print()
if r!=2:
    print(j[0])
    print(f[0])
else:
    print("0\n0")
