s =[]
f=0
n=int(input());
for i in range(int(n)):
    s.append(int(input()))
for j in range (0,n,1):
    if(j==s[j]):
        f=1;
        print (s[j])
if(f!=1):
    print ("'-1'")
