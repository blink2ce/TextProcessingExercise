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

# #For each path, check each pattern for a match.
# for path in paths:
# 	matchesList = []
# 	for pattern in patterns:
# 		#if the lengths aren't the same, we know it's not a match
# 		if len(pattern) == len(path):
# 			patternMatches = True
# 			#step through the pattern, check that every item matches the corresponding item in the pattern
# 			#for index in range(0, len(path)):
# 			#	if not path[index] == pattern[index]:
# 			#		patternMatches = False
# 			if patternMatches:
# 				matchesList.append(pattern)
# 	print matchesList

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
	if len(matchesList) == 0:
		matchesList.append("NO MATCH")
	print matchesList

def findBestMatch(matchesList[]):
	

