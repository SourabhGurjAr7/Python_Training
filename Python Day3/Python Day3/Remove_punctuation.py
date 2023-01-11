def punctuation_removal(str):
  punc='''!@#$%^&*()_+=-{}0123456789[]:;"'?/<>,.'''
  new_str=""
  for i in str:
      if i not in punc:
          new_str=new_str+i
  print("Modified String:",new_str)
str=input("Enter string:")
punctuation_removal(str)