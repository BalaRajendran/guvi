s =[]
n=int(input());
for i in range(int(n)):
    s.append(int(input()))
#print (s)
for i in range (0,n,1):
    for j in range (i+1,n,1):
        if(s[i]<s[j]):
            t=s[i]
            s[i]=s[j]
            s[j]=t
#print (s)

for k in range(n):
    try:
        if(s[k]!=s[k+1]):
            print (s[k], end='')
    except:
        print (s[k])
        
