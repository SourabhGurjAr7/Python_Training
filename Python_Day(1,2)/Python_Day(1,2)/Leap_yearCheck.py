#1992 1988 1996 2012 2016 2024
'''
COnditions for leap year:
1.)The year is multiple of 400.
2.)The year is multiple of 4 and not multiple of 100.
'''
yr=int(input("Enter year: "))
if((yr%400==0) or (yr%4==0) and (yr%100!=0)):
    print(yr,"is a leap year")
else:
    print(yr,"is not a leap year")
