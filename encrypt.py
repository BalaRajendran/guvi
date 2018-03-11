a=str(input());
b=str(input());
l=len(a);
e=0
f=0
c = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0,l,1):
    #print ("1-",i)
    for j in range(0,26,1):
        #print (c[j],"  ",j)
        if(str(a[i])==str(c[j])):
            #print (c[j],"=",j)
            e=e+(j+1);
        if(str(b[i])==str(c[j])):
             #print (c[j],"=",j)
             f=f+(j+1);
    #   print(e+f)
    k=e+f;
    e=0
    f=0
    if(k>26):
        k=k-26;
    print(c[k-1], end='')
    
