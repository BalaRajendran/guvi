print ("Count the number digits ");
a=int(input("Enter the Number to count : "));
s=0; 
while(a>0):
    l=a%10;
    #print (l)
    s=s+1;
    a=a//10;
print (s)
