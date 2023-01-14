name=list(input("Enter names: ").split())
roll=list(input("Enter roll no: ").split())
dict1=dict(zip(roll,name))
print(dict1)

def ab_present(i):
    for i in dict1:
      if(n in dict1[i]):
          print(n,"Yes present...!",i)
          break
    else:
      print("not")
   #     for x in dict1:
      #      print(x,"is present and roll number is",dict[x])
    #else:
     #   print("Absent")
n=input("Enter name: ")
ab_present(n)
