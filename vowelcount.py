"""given any string, return the number of vowels """

def main():
	print vowel_count("john")
	print vowel_count("biscuit")
	print vowel_count("for")
	print vowel_count("fOr")

def vowel_count(str):
	count = 0
	vowels = 'aeiou'
	for i in str:
		if i.lower() in vowels:
			count+=1
	return count

"""	
#alternate way printing counts next to letters 
def vowel_count(str):
	vowels = 'aeiou'
	for v in vowels:
		print v, str.lower().count(v)"""
		
"""
def vowel_count(str):
	counts = {i:0 for i in 'aeiouAEIOU'}
	for char in str:
		if char in counts:
			counts[char] += 1
 
	for k,v in counts.items():
		print(k, v)"""

main()