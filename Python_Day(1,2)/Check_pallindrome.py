#121,232,595
'''
n=int(input("Enter the number to check:"))
rev=0
temp=n
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print(temp,"is a pallindrome number...")
else:
    print(temp,"is not a pallindrome...")
'''
