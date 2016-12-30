def isPalindrome():
	flag = True 
	word = raw_input("Enter a word: ")
	for i in range(len(word)/2):
		if (word[i] != word[len(word)-1-i]):
			flag = False
		
	return flag
print isPalindrome()