# Vansh Gaikwad PRN 25070521088


# Multiplication Of Two Square Matrices

n = int(input("dimension: "))

print("first matrix:")
A = []
for i in range(n):
	A.append(list(map(int, input().split())))

print("second matrix:")
B = []
for i in range(n):
	B.append(list(map(int, input().split())))

C = [[0]*n for _ in range(n)]

for i in range(n):
	for j in range(n):
		for k in range(n):
			C[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix:")
for i in range(n):
	print(" ".join(map(str, C[i])))
