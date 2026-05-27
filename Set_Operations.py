# Vansh Gaikwad PRN 25070521088


# Set Operations

Set_A = set(map(int, input("Set A: ").split()))

Set_B = set(map(int, input("Set B: ").split()))

union_set = Set_A | Set_B
intersection_set = Set_A & Set_B
difference_set = Set_A - Set_B

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)

