 # Vansh Gaikwad PRN 25070521088


# Sum Of Digits Using Recursion

def sum_of_digits_recursive(n):
	if n < 10:
		return n
	else:
		return (n % 10) + sum_of_digits_recursive( n // 10)



# Write your code here
number = int(input())
result = sum_of_digits_recursive(number)	
print(result)

	
