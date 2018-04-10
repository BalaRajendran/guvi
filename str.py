a=str(input())
c=0
b=[a[i:i+2] for i in range(0, len(a), 2)]
for i in range(0,len(b)-1,1):
    if b[i]!=b[i+1][::-1]:
        if len(b[i+1])==int(2):
            c=c+2
        else:
            c=c+1
print(c)
