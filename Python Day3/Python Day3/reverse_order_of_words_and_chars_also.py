str=input("Enter string: ")
def reverse_order_and_characters(str):
  str1=str[::-1].split()
  res=' '.join(str1)
  print(res)
reverse_order_and_characters(str)
