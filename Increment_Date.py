# Vansh Gaikwad PRN 25070521088


# Increment Date

# Type Content here...
day = int(input())
month = int(input())
year = int(input())

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0)

if month in [1, 3, 5, 7, 8, 10, 12]:
	max_days = 31
elif month in [4, 6, 9, 11]:
	max_days = 30
elif month == 2:
	max_days = 29 if is_leap else 28
else:
	max_days = 0

if year <= 0 or month < 1 or month > 12 or day < 1 or day > max_days:
	print("Invalid Date")
else:
	day += 1
	if day > max_days:
		day = 1
		month += 1
		if month > 12:
			month = 1
			year += 1
	print(f"{day:02d}-{month:02d}-{year:04d}")
