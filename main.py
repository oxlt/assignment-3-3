validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

MIN_YEAR = int (MIN_YEAR) 
MIN_MONTH = int (MIN_MONTH)
MAX_MONTH = int (MAX_MONTH)
MIN_DAY = int (MIN_DAY)
MAX_DAY = int (MAX_DAY)

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if int(year) <= MIN_YEAR:
  validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH:
  validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: 
  validDate = False
 
if validDate == True:
  print(month, "/", day, "/", year, "is a valid date. ")
else: 
  print(month, "/", day, "/", year, "is an invalid date")