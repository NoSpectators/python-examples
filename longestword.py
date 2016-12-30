"""given a string, return the longest word of that string .
assume that alphanumeric characters form words in this case """

def main():
    print longestWord("fun&!! time")
    print longestWord("I love dogs")
    print longestWord("I like pumpernickel doohickeys jo&&&&&&&&&&")
	
def longestWord(str):
    new_word = ""
    for i in str:
	    if i.isalpha() or i == " ": #check if each character in string is either alphanumeric or a space 
		    new_word += i   
    return longestTest(new_word)  #call longestTest, passing new_word into it 
	
def longestTest(str):   #at this point, the str is the same but only with alphanumeric and spaces
    test = str.split(" ") #use split method to append each series of alphanumerics into a python list 
    #print test 
    word  = test[0]    #use first word in list as a test 
    for i in test:
	    if len(i) > len(word):
		    word = i
    return word  #return largest word 
	
main()