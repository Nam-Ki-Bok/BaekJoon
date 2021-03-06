from math import factorial


def cal(n, r):

	return factorial(n) // (factorial(n - r) * factorial(r))


answer = 0
weight = int(input())
n = weight
r = 0

while n >= r:
	answer += cal(n, r)
	n -= 1
	r += 1

print(answer % 10007)