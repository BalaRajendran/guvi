a=int(input());
a1=a;
s=0;
while(a>0):
    l=a%10;
    s=(s*10)+l;
    a=a//10;
if(int(a1)==int(s)):
    print ("YES");
else:
    print ("NO");
