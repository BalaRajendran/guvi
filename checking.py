a=int(input())
b=[]
c=[]
for i in range (a):
    b.append(int(input()))
for i in b:
    if i not in c:
        c.append(i)
print(len(c))
