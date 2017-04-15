import sys

# Cost weights are (deletion, insertion, substitution)
def levenshtein_distance(s1, s2, cost_weights=(1,1,1)):
	s1 = s1.lower()
	s2 = s2.lower()
	m = len(s1) + 1
	n = len(s2) + 1
	costs = [[0]*n for x in range(m)]

	for i in range(m):
		costs[i][0] = i
		
	for i in range(n):
		costs[0][i] = i

	for j in range(1, n):
		for i in range(1, m):
			sub_cost = 0 if s1[i-1] == s2[j-1] else cost_weights[2] #subcost
			costs[i][j] = min(costs[i-1][j] + cost_weights[0], #del cost
			                  costs[i][j-1] + cost_weights[1], #ins cost
			                  costs[i-1][j-1] + sub_cost)
	return costs[m-1][n-1]

class Distances:
	def __init__(self, fn="wordlist.txt"):
		self.knownwords = []
		with open(fn) as wordlist:
			for line in wordlist.readlines():
				self.knownwords.append(line[:-1])
	
	def closest_levenshtein(self, word):
		best_dist = (float('inf'), "")
		for known in self.knownwords:
			dist = (levenshtein_distance(word, known), known)
			if dist[0] < best_dist[0]:
				best_dist = dist

		return best_dist[1]
