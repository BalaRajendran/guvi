a=str(input("Enter a A string : "));
b=str(input("Enter a B string : "));
c=len(a);
d=len(b);
f=0;
#print (c)
if(c!=d):
    print("Imposible")
if (a[0]!=b[0]):
    #print ("1")
    f=f+1;
    if (a[1]!=b[1]):
        #print ("2")
        f=f+1;
    elif (a[1]==b[1]):
        if(c==int(3)):
            if(a[2]!=b[2]):
                f=f+1;
else:
    if (a[1]!=b[1]):
        #print ("3")
        f=f+1;
    elif (a[1]==b[1]):
        if(int(c)==int(3)):
            #print ("4")
            if(a[2]!=b[2]):
                f=f+1;
    
#print (f)
if(f==int(1)):
    print ("yes")
else:
    print ("no")
