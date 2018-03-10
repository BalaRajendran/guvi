b=str(input("Enter a A string : "));
a=list(b)
c1=len(b);
i=0;
if(c1==2):
    c=a[i];
    a[i]=a[i+1];
    a[i+1]=c;
elif(c1==4):
    c=a[i];
    a[i]=a[i+1];
    a[i+1]=c;
    a[i+2]=c;
    a[i+2]=a[i+3];
    a[i+3]=c;
if(c1%2==0):
    str1 = ''.join(map(str, a))
    print (str1)
else:
    print ("Impossible")
    
