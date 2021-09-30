# Task 1: Generalised Fibonacci

# Write your code here:

p = 6
q = 4

fibo = [1, 1]

fibo.append(p * fibo[1] + q * fibo [0])
fibo.append(p * fibo[2] + q * fibo [1])

print(fibo)
