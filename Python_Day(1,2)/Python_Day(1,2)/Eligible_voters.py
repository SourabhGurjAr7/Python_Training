name=input("Enter the Name:")
age=int(input("Enter the Age:"))
if age<=0:
    print("Invalid Age.Please enter valid age")
elif(age<18):
    print("{0} is not eligible Voter.".format(name))
else:
    print("{0} is eligible Voter".format(name))

