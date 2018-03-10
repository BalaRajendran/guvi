a=str(input("Enter a string : "));
I=1;
V=5;
X=10;
b=len(a)
o=0;
for i in range (b):
    #print (a[i]);
    if (a[i]=='I'):
        o=o+1;
    elif (a[i]=='V'):
        o=o+5;
    else:
        o=o+10;
print (o)
