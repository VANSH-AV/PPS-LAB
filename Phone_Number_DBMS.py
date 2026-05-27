# Parv Pahuja - 25070521089

# Phone Number Data Base Management System

def main():
	n = int(input().strip())
	database = {}

	for _ in range(n):
		line = input().strip().split()
		if not line:
			continue

		command = line[0]

		if command == "ADD":
			name = line[1]
			phone = line[2]
			database[name] = phone
		elif command == "REMOVE":
			name = line[1]
			if name in database:
				del database[name]
		elif command == "DISPLAY":
			if not database:
				print("No contacts")
			else:
				for name in sorted(database.keys()):
					print(f"{name}: {database[name]}")

if __name__ == "__main__":
	main()
