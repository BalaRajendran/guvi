a=int(input());
b=int(input());
count=0;
for i in range(a,b+1,1):
    fact=0;
    for j in range(1,b+1,1):
        if(i%j==0):
            fact=fact+1;
    if(fact==2):
        #print (i)
        count=count+1;
print (count)
