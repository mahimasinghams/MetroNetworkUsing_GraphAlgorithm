from random import randint
N = 7
print(N, int(N * (N - 1) / 2))
for i in range(1, N + 1):
	for j in range(i + 1, N + 1):
		print(i, j, randint(1, 10), randint(1, 10))