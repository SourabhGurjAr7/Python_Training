#371 370 407
n=int(input("Enter the number to check:"))
sum=0
temp=n
while(n>0):
    rem=n%10
    sum=sum+rem**3
    n=n//10 # 19//2=9
if(temp==sum):
    print(temp,"is a Armstrong number")
else:
    print(temp,"is not a Armstrong number")