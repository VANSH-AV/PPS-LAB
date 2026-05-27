# Write your code here......
import Fibbonacci_Sequence_using_Module
n = int(input())

if n > 0:
	fib_series = Fibbonacci_Sequence_using_Module.generate_fibonacci_sequence(n)
	print(' '.join(map(str, fib_series)))
else:
	print("Please enter a positive integer")