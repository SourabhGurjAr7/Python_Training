def fact(n):
    if(n==0 or n==1):
       return 1
    else:
       return n*fact(n-1)
term=int(input("Enter the number whose factorial is to find:  "))
print("Factorial of {0} is {1}".format(term,fact(term)))