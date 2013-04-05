def f(n):
	if n < 0:
		return "Can't do negative nth Fibonacci number."
	if n == 0:
		return 0
	if n == 1:
		return 1
	
	return f(n-1) + f(n-2)
	
"""
given n, produce the nth Fibonacci number:
1, 1, 2, 3, 5

5 = 3 + 2
3 = 2 + 1
2 = 1 + 1

f(5) = f(4) + f(3)
f(4) = f(3) + f(2)
f(3) = f(2) + f(1)
f(2) = f(1) + 1
f(1) = f(0) + 1
f(0) = 0

is there a way to print out results each time, instead of just final result? maybe using stack? --can't, would need a 2nd recursive function just for printing that would call this function to get the nth Fibonacci number
"""