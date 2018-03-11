t=1;
m=0;
s = list()
n=int(input());
for i in range(int(n)):
    s1 = input()
    s.append(str(s1))
l=100000;
for k in range(1,n):
    l1=len(s[k])
    if(l1<l): 
        l=l1
#print (l)
for i in range(0,l-1,1):
    c=s[0][i];
    for j in range(1,n,1):
        #print (i)
        if((s[j][i]==c) and (t==1)):
            #print (c)
            t=1;
        else:
            t=0;
    if t==1:
        m=m+1;
        print(c, end='')
    elif m==0:
        m=m+1;
        print("No Prefix Found")
