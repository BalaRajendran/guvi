print ("Find the largest number amoung three numbers");
num=list()
arry=int(3);
a=1;
for i in range(int(arry)):
   print ('Num :',a);
   a+=1;
   n=input();
   num.append(int(n))
if (num[0]>num[1] and num[0]>num[2]):
        print (num[0]);
elif  (num[1]>num[0] and num[1]>num[2]):
        print (num[1]);
else:
    print(num[2]);
    
