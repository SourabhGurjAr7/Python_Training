def Cal_LCM(n1,n2):
    for i in range(1,(n1*n2)+1):
        if(i%n1==0 and i%n2==0):
            print("LCM of {0} and {1} is {2}".format(n1,n2,i))
            break
n1,n2=int(input("Enter 1st numbers: ")),int(input("Enter 2nd Number:"))
Cal_LCM(n1,n2)