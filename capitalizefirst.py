"""capitalize the first letter of each word in a given string,
assuming there are only alphanumeric characters and spaces in the string"""

def main():
    print capitalizeFirst('hello world')
    print capitalizeFirst('i ran there')
	
"""def capitalizeFirst(str):
	string = ""
	new = str.split(" ") #split the string by spaces into a python list 
	for i in range(len(new)):
		string += new[i][:1].upper()  #append to empty string capitalized first letter 
		if (i+1) != len(new):   #add other letters to string and spaces 
			string += new[i][1:] + "-" 
		else:
			string += new[i][1:]  #for last letter, just add letter, not space too 
	return string """
    

#main()



def capitalizeFirst(str):
	string = ""
	new = str.split(" ")
	for i in range(len(new)):
         string += new[i][:1].upper()
         if (i+1) != len(new):
             string += new[i][1:] + " "
         else:
             string += new[i][1:]
            
	return string 
 
 
 
 
 
 
 
 
main()