# Parv Pahuja - 25070521089

# Remove Punctuation From String

s = input()

result = ""

for ch in s:
	if ch.isalnum() or ch == " ":
		result += ch

print(result)