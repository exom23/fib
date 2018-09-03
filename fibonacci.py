startNumber = int(raw_input("Enter the first number: "))
endNumber = int(raw_input("Enter the last number: "))
def fib(n):
	if n < 2:
			return n
	return fib(n-1) + fib(n-2) #2 the 1
print map(fib, range(startNumber, endNumber))