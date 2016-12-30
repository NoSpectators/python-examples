"""return the boolean value of whether or not the string 'cat' 
is in the string the same number of times as 'dog' """

def main():
    
    array = [cat_dog('catdog'), cat_dog('catcat'), cat_dog('1cat1cadodog')]
    print_results(array)

def print_results(arr):
    for i in arr:
		print i

def cat_dog(str):
    dog = 0 #initialize two counting variables to 0 
    cat = 0
    for i in range(len(str)-2): #remember you want to end -2 because three letter words
		if 'cat' in str[i:i+3]: #if not -2, you get out of index error 
			cat += 1 
		if 'dog' in str[i:i+3]:
			dog += 1
    return dog == cat

main()
 

