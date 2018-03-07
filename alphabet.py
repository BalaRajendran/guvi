print ("Code weather a number or alphabet");
a=input("Enter a letter to check weather a number or alphabet : ");
if (str(a)>='a' and str(a)<='z') or (str(a)>='A' and str(a)=='Z'):
    print ("Alphabet");
else:
    print ("No");
