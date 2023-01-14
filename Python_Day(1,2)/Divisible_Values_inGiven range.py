low=int(input("Enter lower range: "))
high=int(input("Enter range range: "))
num=int(input("Enter number to check for divisibility:"))
print("Numbers divisible by {0} in between {1} and {2}:".format(num,low,high))
for i in range(low,high):
    if(i%num==0):
        print(i,end=" ")