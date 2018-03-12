a=int(input())
b=list()
c=0
for i in range (0,a,1):
    c=int(input())
    b.append(int(c))
#print (b)
for i in range(0,a,1):
    for j in range(0,a,1):
        if(b[i]>b[j]):
            t=b[i];
            b[i]=b[j]
            b[j]=t;
for i in range (0,a,1):
    print(b[i])
