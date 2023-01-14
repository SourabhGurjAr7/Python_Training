class Calculation:
    def add(self,n1,n2):
        sum1=n1+n2
        return sum1
    def multi(self,n1,n2):
        multi=n1*n2
        return multi
class cal(Calculation):
    def display(self):
        print("------Calculated values are:------ \n")
n1=float(input("Enter 1st number: "))
n2=float(input("Enter 2nd Number: "))
c1=cal()
c1.display()
print("Addition of {0} and {1} is {2}".format(n1,n2,c1.add(n1,n2)))
print("Multiplication of {0} and {1} is {2}".format(n1,n2,c1.multi(n1,n2)))
