n=int(input("Enter the number:"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem**3
    n=n//10

print("Sum of cubes of digits of given number is",sum)