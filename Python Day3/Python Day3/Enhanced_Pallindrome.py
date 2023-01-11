inp=input("Enter value: ").lower()
def Check_pallindrome(inp):
   rev=inp[::-1].lower()
   if(rev==inp):
     print(inp,"is a pallindrome...!")
   else:
     print(inp,"is not a pallindrome...!")
Check_pallindrome(inp)