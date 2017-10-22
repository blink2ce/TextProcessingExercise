#Open file
tf = 'input-file.txt'
f = open(tf)

#Read patterns into the program
numPatterns = int(f.readline())
patterns = []
for n in range(0, numPatterns):
	patterns.append(f.readline().strip().split(','))
#print(patterns)

#Read paths into the program
numPaths = int(f.readline())
paths = []
for n in range(0, numPaths):
	item = f.readline().strip()
	if not item[0].isalnum():
		item = item[1:]
	if not item[len(item) - 1].isalnum():
		item = item[:len(item) - 1]
	item = item.split('/')
	paths.append(item)
#print(paths)

def findBestMatch(matchesList):
	#first remove matches that have more wildcards than any other.
	countWildcards = []
	#Make a list that has the count of asterisks of each match.
	for pattern in matchesList:
		count = 0
		for item in pattern:
			if item == "*":
				count = count + 1
		countWildcards.append(count)
	#remove matches that have more asterisks than another.
	mostWildcards = max(countWildcards)
	minWildcards = min(countWildcards)
	while len(matchesList) > 1  and mostWildcards not == minWildcards:
		#delete the item where mostWildcards is found and delete 
		#he corresponding count in countWildcards.

		#Recalculate mostWildcards and minWildcards.



	print countWildcards

for path in paths:
	matchesList = []
	for pattern in patterns:
		if len(pattern) == len(path):
			patternMatches = True;
			for index in range(0, len(path)):
				if not pattern[index] == '*':
					if not path[index] == pattern[index]:
						patternMatches = False;
			if patternMatches:
				matchesList.append(pattern)
	findBestMatch(matchesList)
	if len(matchesList) == 0:
		matchesList.append("NO MATCH")
	print matchesList


