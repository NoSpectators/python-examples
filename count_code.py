def main():
    
    array = [count_code('aaacodebbb'),count_code('codexxcode'), 
             count_code('cozexxcope')]
    print_results(array)

def print_results(arr):
    for i in arr:
        if i == 1:
	    print 'string appeared 1 time'
 	else:
	    print 'string appeared',i,'times'

def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
	    count += 1
    return count
 
main()
