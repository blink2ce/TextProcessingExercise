from __future__ import print_function
import sys

inputFile = open(sys.argv[1])
outputFile = sys.argv[2]

def readPatterns():
	numPatterns = int(inputFile.readline())
	patterns = []
	for n in range(0, numPatterns):
		patterns.append(inputFile.readline().strip().split(','))
	return patterns

def readPaths():
	numPaths = int(inputFile.readline())
	paths = []
	for n in range(0, numPaths):
		item = inputFile.readline().strip()
		#remove slashes from both ends, if they exist
		if not item[0].isalnum():
			item = item[1:]
		if not item[len(item) - 1].isalnum():
			item = item[:len(item) - 1]
		item = item.split('/')
		paths.append(item)
	return paths

def findBestMatch(matchesList):
	#first remove matches that have more wildcards than any other.
	countWildcards = []
	for pattern in matchesList:
		count = 0
		for item in pattern:
			if item == "*":
				count = count + 1
		countWildcards.append(count)
	mostWildcards = max(countWildcards)
	minWildcards = min(countWildcards)
	while len(matchesList) > 1  and mostWildcards != minWildcards:
	 	#delete the item where mostWildcards is found and delete 
	 	#the corresponding count in countWildcards.
	 	index = countWildcards.index(mostWildcards)
	 	del countWildcards[index]
	 	del matchesList[index]
	 	#Recalculate mostWildcards and minWildcards.
	 	mostWildcards = max(countWildcards)
	 	minWildcards = min(countWildcards)


def main():
	patterns = readPatterns()
	paths = readPaths()
	with open(outputFile, 'w') as f:
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
			if len(matchesList) > 1:
				findBestMatch(matchesList)
			if len(matchesList) == 0:
				matchesList.append(["NO MATCH"])
			#print matchesList
			for item in matchesList:
				item = ','.join(item)
				f.write(item + '\n')
				print(item)

main()

