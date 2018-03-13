n=int(input())
a=[]
b=[]
c=[]
k=0
for i in range (n):
    a.append(int(input()))    
for j in range (n):
        b.append(int(input()))
for i in range (n):
        for j in range(n):
                if(a[i]==b[j]):
                        k=k+1;
                        c.append(a[i])
c=list(set(c))
for i in c:
        print (i)
                        
