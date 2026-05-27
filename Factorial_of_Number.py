# Parv Pahuja -  25070521089

# Factorial Of A Number

#Write your code here
#Accept integer
n = int(input())

#Initialize factorial result
factorial = 1

# Calculate factorial using a loop
for i in range(1, n + 1):
	factorial *= i

#print the result
print(factorial)