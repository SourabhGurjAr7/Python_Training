str=input("Enter string:")
def reverse_word_Order(str):
  str1=str.split()[::-1]
  res=' '.join(str1)
  print(res)
def count_characters(str):
    c=0
    for i in str:
        if i!=" ":
         c=c+1
    print("Characters present in string:",c)
reverse_word_Order(str)
count_characters(str)