from __future__ import print_function
import sys
import collections

inputFile = open(sys.argv[1])
outputFile = sys.argv[2]

def readIn(delimiter):
	numPaths = int(inputFile.readline())
	paths = []
	for n in range(0, numPaths):
		item = inputFile.readline().strip()
		#remove slashes from both ends, if they exist
		if item[0] == '/':
			item = item[1:]
		if item[len(item) - 1] == '/':
			item = item[:len(item) - 1]
		item = item.split(delimiter)
		paths.append(item)
	return paths

def breakTies(matchesList):
	matchLength = len(matchesList[0])
	index = -1;
	while -(index) <  matchLength:
		wildcardExists = False;
		for match in matchesList:
			if match[index] == "*":
				wildcardExists = True;
		if wildcardExists:
			for match in matchesList:
				if match[index] != '*':
					del matchesList[matchesList.index(match)]
		index = index - 1;

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
	if len(matchesList) > 1:
		breakTies(matchesList)

def main():
	patterns = readIn(',')
	paths = readIn('/')
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
			for item in matchesList:
				item = ','.join(item)
				f.write(item + '\n')
				print(item)

main()

