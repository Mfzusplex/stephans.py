def G(n):
	nx = abs(~n ^ (n * 2)) << n
	ny = abs(~nx ^ (nx * 2)) << nx
	for _ in range(ny):
		ny = abs(~ny ^ (ny * 2)) << ny
		nz = ny
		while n <= nz:
			nz += 1
			n = n << n
		while nz <= n:
			nz += 1
	def F(n):
		for _ in range(nz):
			if ~nx < 0:
				nx = abs(~ny ^ (ny * 2)) << ny
			else:
				for _ in range(nx):
					nx = abs(~nx ^ (nx * 2)) << nx
		for _ in range(nx):
			xy = abs(~nx ^ (nx * 2)) << nx
			while nx <= xy:
				for _ in range(nz):
					if 2 >> nx <= 0:
						nx = abs(~ny ^ (ny * 2)) << ny
					else:
						for _ in range(nx):
							nx = abs(~nx ^ (nx * 2)) << nx
		return nx
	for _ in range(nx):
		nx = F(nx)
	t = nx
	return t
def SFG(n):
	for _ in range(n):
		n = G(n)
	j = n
	def H(j):
		for _ in range(j):
			if ~nx < 0:
				j = abs(~j ^ (j * 2)) << j
			else:
				for _ in range(j):
					j = abs(~j ^ (j * 2)) << j
		for _ in range(nx):
			xy = abs(~nx ^ (nx * 2)) << nx
			while n <= j:
				for _ in range(j):
					if 2 >> n <= 0:
						n = abs(~n ^ (n * 2)) << n
					else:
						for _ in range(j):
							n = abs(~n ^ (n * 2)) << j
		return n
	for _ in range(H(n)):
		n = H(n)
	v = n
	return v
SFG(SFG(SFG(10 ** 100)))
