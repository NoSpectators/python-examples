def reverse(a_str):
    print "Got an argument:", a_str
    #base case
    if len(a_str) == 1:
        print "Base Case!"
        return a_str
    #recursive step
    else:
	new_str = reverse(a_str[1:]) + a_str[0]
  	print "Reassembling %s and %s into %s" %(a_str[1:], a_str[0], new_str)
  	return new_str

the_str = raw_input("What string: ")
print()
result_str = reverse(the_str)
print "The reverse of %s is %s" %(the_str, result_str)
