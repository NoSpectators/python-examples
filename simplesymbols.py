"""determine if a given string's letters are surrounded by
"+". It doesn't matter what else is in the string. """

def main():
    print simpleSymbols("+d+=3=+s+")
    print simpleSymbols("f++d+")
    print simpleSymbols("j+")
    print simpleSymbols("+j+k")
    print simpleSymbols("+d+")
    print simpleSymbols("+d===+a+")
    print simpleSymbols("b")
	
"""def simpleSymbols(str): 
	flag = False  
	for i in range(len(str)):
		if str[0].isalpha():  #check first element of string 
			return flag 
		elif str[len(str)-1].isalpha():  #check last element of string 
			return flag 
		elif str[i].isalpha():  #if there are non-alphanumeric symbols at end 
			if str[i-1] == "+" and str[i+1] == "+":
				flag = True 
	return flag""" 
	
#main()	  

def simpleSymbols(string): 
    if len(string) < 3:
        return "false"
    # code goes here 
    for i in range(len(string)-1):
        if string[0].isalpha():
            return "false"
        if string[-1].isalpha():
            return "false"
        if string[i].isalpha():
            if string[i-1]=="+" and string[i+1]=="+":
                return "true"
            return "false"
            
# keep this function call here  
#print simpleSymbols(raw_input())  

main()