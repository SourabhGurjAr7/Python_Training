lst=list(map(str,input("Enter list values:").split()))
print("Original list:",lst)
def duplicate(lst):
 dup,uni=[],[]
 for i in lst:
     if(lst.count(i)>1 and i not in dup):
         dup.append(i)
     elif( i not in dup):
         uni.append(i)
 print("List with duplicate elements:",dup,"\n")
 if(len(dup)==0):
     print("No Duplicate Elements are present..! \n")
 print("List with Unique elements: ",uni)
duplicate(lst)
