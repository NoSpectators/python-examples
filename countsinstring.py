"""myString = "We want to get the counts for each letter in this sentence"
counts = {}

for letter in myString:
    counts[letter] = counts.get(letter, 0) + 1
print counts

sortedKeys = sorted(counts.keys(), key = lambda x: counts[x])
for k in sortedKeys:
    print k, "-->", counts[k]"""

#build a dictionary of letter counts, easy to follow, doesn't count spaces
counts = {}
str = "john is great"
for i in str:
    if i != " ":
        if i in counts:
            counts[i] +=1
        else:
            counts[i] = 1

#build a dictionary of letter counts with a comprehension, doesn't count spaces
str = "john is great"
for i in str:
    letterlist = [i for i in str if i != " "]
    stats = {x:letterlist.count(x) for x in letterlist}
print counts
print stats

#build a dictionary of words the easy way
counts2 = {}
str = "john is great"
for i in str.split():
    if i != " ":
        if i in counts2:
            counts2[i] +=1
        else:
            counts2[i] = 1
print counts2

#build a dictionary of words using comprehension
str = "john is great"
wordlist = [x for x in str.split()]
counts3 = {x:wordlist.count(x) for x in wordlist}
print counts3
