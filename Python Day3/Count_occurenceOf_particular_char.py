str,occ=input("Enter String:"),input("enter character whose occurence to check: ")
def occurence(str):
 count=0
 for i in str:
     if(i==occ):
         count+=1
 print(count,"times ")
occurence(str)
