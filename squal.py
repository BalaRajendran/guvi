a=int(input())
b=[]
for i in range(0,a,1):
    b.append(int(input()))
c=int(input())
#print (b)
t=0
s=0
#for i in range (a-1):
    #print (i)
for i in range (a-1):
    if(b[i]==b[i+1]):
        s=b[i]+b[i+1]
    if(s==c):
        print("yes")
        t=1;
if(t!=1):
    print("no")
