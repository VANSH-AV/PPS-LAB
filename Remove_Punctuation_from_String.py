# Vansh Gaikwad PRN 25070521088


# Remove Punctuation From String

s = input()

result = ""

for ch in s:
	if ch.isalnum() or ch == " ":
		result += ch

print(result)
