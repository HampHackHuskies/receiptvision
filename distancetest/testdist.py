#!/bin/python

import distance

receipt = ['sahara bread', 'sb garbnzo beans', 'sb canola oil', 'jfc sesame seed', 'cucumbers', 'ex lrg tomatoes']
knowledge = distance.Distances()

closests = []
for item in receipt:
	closests.append((item, knowledge.closest_levenshtein(item)))

print(*closests, sep='\n')
