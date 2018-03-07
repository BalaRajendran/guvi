num=list()
n=int(input("Enter the number array :"));
n1=int(input("Enter the number to count the array: "));
print("Enter the element");
a=int(0);
for i in range (n):
    k=input();
    num.append(k);
for j in range (n1):
    a+=int(num[j]);
    print(a);
print (a);
#print (num);

