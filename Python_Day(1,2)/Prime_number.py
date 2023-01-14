num=int(input("Enter the number:"))
if(num==1):
    print(num,"is not a Prime number.")
elif(num==0):
    print(num,"is neither prime nor composite.")
else:
 for i in range(2,num):
     if(num%i==0):
         print(num,"is not a Prime number")
         break
 else:
     print(num,"is a Prime Number")