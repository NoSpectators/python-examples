"""def isPalindrome(string):
    new = string.replace(" ", "")
    #print new
    backwards = ""
    for i in range(len(new)-1,-1,-1):
        backwards += new[i]
    #print backwards
    return new == backwards
    
print isPalindrome("dont nod") """



#this version ignores etra puncuation
def isPalindrome(string):
    new = ""
    for i in string:
        if i.isalpha():
            new += i.lower()
    #print new
    backwards = ""
    for i in range(len(new)-1,-1,-1):
        backwards += new[i]
    #print backwards
    #print "backwards =",backwards
    #print "new = ", new
    if new == backwards:
        return "true"
    return "false"
    
print isPalindrome("Noel - sees Leon")  