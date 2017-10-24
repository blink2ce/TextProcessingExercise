from __future__ import print_function
import sys

def readIn(delimiter):
	numPhrases = int(sys.stdin.readline())
	phrases = []
	for n in range(0, numPhrases):
		item = sys.stdin.readline().strip()
		#remove slashes from both ends, if they exist
		if item[0] == '/':
			item = item[1:]
		if item[len(item) - 1] == '/':
			item = item[:len(item) - 1]
		item = item.split(delimiter)
		phrases.append(item)
	return phrases

def breakTies(matchesList):
	matchLength = len(matchesList[0])
	#Start at the end of the match and work backwards
	index = -1;
	#Stop after we look at all of the items in the match
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
	#Make list that records the number of wildcards in each match.
	countWildcards = []
	for pattern in matchesList:
		count = 0
		for item in pattern:
			if item == "*":
				count = count + 1
		countWildcards.append(count)
	mostWildcards = max(countWildcards)
	minWildcards = min(countWildcards)
	#Delete the matches that have more wildcards than any other.
	while len(matchesList) > 1  and mostWildcards != minWildcards:
	 	index = countWildcards.index(mostWildcards)
	 	del countWildcards[index]
	 	del matchesList[index]
	 	#recalculate max and min
	 	mostWildcards = max(countWildcards)
	 	minWildcards = min(countWildcards)
	if len(matchesList) > 1:
		breakTies(matchesList)

def printResult(result):
	for matchesList in result:
		for match in matchesList:
			match = ','.join(match)
			print(match)

def main():
	patterns = readIn(',')
	paths = readIn('/')
	result = []
	#Find patterns that match each path
	for path in paths:
		matchesList = []
		for pattern in patterns:
			if len(pattern) == len(path):
				#Check that each value in the pattern matches for path
				patternMatches = True;
				for index in range(0, len(path)):
					if pattern[index] != '*':
						if path[index] != pattern[index]:
							patternMatches = False;
				if patternMatches:
					matchesList.append(pattern)
		if len(matchesList) > 1:
			findBestMatch(matchesList)
		if len(matchesList) == 0:
			matchesList.append(["NO MATCH"])
		result.append(matchesList)
	printResult(result)	


main()

