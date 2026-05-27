# Parv Pahuja - 25070521089

# Count Vowels In String

s = input()

count = 0
vowels = "aeiouAEIOU"

for ch in s:
	if ch in vowels:
		count += 1

print(count)