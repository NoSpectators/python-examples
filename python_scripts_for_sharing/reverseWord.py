"""ask user to input a word, then return the reversed string of that input"""

def main():
    word1 = raw_input('type a string: ')
    reverseWord(word1)
	
def reverseWord(str):
    string = ""
    for i in range(len(str)-1,-1,-1):
		string += str[i]
    print 'reversed =',string
		
main()

#alternate way to write same program
"""
def reverseWord(str):
    string = ""
    for i in range(len(str)-1,-1,-1):
		string += str[i]
    print 'reversed =',string
	
if __name__ == "__main__":
    word1 = raw_input('type a string: ')
    reverseWord(word1)"""