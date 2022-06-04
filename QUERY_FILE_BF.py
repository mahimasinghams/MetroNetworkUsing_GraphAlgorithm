import sys
from random import randint
out = sys.stdout
with open('./graph_5.txt', 'w') as f:
	sys.stdout = f
	N = 50
	print(N, int(N * (N - 1)))
	for i in range(1, N + 1):  
		for j in range(i + 1, N + 1):
			print(i, j, randint(-10, 100), randint(-10, 100))
			print(j, i, randint(-10, 100), randint(-10, 100))
	Q = N
	qry = set()
	while len(qry) < Q:
		u = randint(1, N)
		v = randint(1, N)
		if u != v:
			qry.add((u, v))
	print(Q)
	for i in qry:
		print(i[0], i[1])
	sys.stdout = out