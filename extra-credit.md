Extra Credit

1. The algorithmic complexity of my program is quadratic. This is due to the nested for loops in the main function. My program would not complete quickly when given hundreds of thousands of patterns and paths. I think there is a faster solution. I would try sorting the lists first using Python's built-in sorting function, which is only nlog(n) in complexity. That would help me avoid stepping through the Paths and Patterns so many times looking for matches.

2. I would explain how my program works to a non-technical person like this:

I made a computer program that can find all the matches between two different lists of data. It can tell us what the match is in one list for every entry in the other. It will also tell us if there is no match for that entry. 

Some of the entries in the list that we are looking for matches in have wildcards that can count as anything. This means that some entries might have more than one match because the wildcards. So if there is a tie when we are finding matches because of a wildcard, my program finds the match that has more wildcards towards the end of the entry, to break the tie.

