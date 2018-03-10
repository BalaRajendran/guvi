a=str(input("Enter a A string : "));
b=str(input("Enter a B string : "));
c=len(a);
d=len(b);
i=0;
if (c!=d):
    print("no");
elif(c==int(3)):
    if(a[i]==a[i+1]==a[i+2]):
        if (b[i]==b[i+1]==b[i+2]):
            print("yes")
        else:
            print("no");
    elif(a[i]==a[i+1]!=a[i+2]):
        if (b[i]==b[i+1]!=b[i+2]):
            print ("yes")
        else:
            print("no");
    elif (a[i]!=a[i+1]==a[i+2]):
        if (b[i]!=b[i+1]==b[i+2]):
            print ("yes")
        else:
            print("no");
    elif (a[i]!=a[i+1]!=a[i+2]):
        if (b[i]!=b[i+1]!=b[i+2]):
            print ("yes")
        else:
            print("no");
elif(c==int(2)):
    if (a[i]==a[i+1]):
        if (b[i]==b[i+1]):
            print ("yes")
        else:
            print("no");
    elif (a[i]!=a[i+1]):
        if (b[i]!=b[i+1]):
            print ("yes")
        else:
            print("no");
else:
    print("unexpected");
