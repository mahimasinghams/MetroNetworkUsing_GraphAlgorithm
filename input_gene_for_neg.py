from random import randint
N = 5
print(N, int(N * (N - 1)))
for i in range(1, N + 1):
	for j in range(i + 1, N + 1):
		print(i, j, randint(-9,4), randint(-9,4))
		print(j, i, randint(-9,4), randint(-9,4))