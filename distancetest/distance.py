def levenshtein_distance(s1, s2):
	m = len(s1) + 1
	n = len(s2) + 1
	costs = [[0]*n for x in range(m)]

	for i in range(m):
		costs[i][0] = i
		
	for i in range(n):
		costs[0][i] = i

	for j in range(1, n):
		for i in range(1, m):
			cost = 0 if s1[i-1] == s2[j-1] else 1
			costs[i][j] = min(costs[i-1][j] + 1,
			                  costs[i][j-1] + 1,
			                  costs[i-1][j-1] + cost)
	return costs[m-1][n-1]
