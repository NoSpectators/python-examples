def main():
    print letterChanges('hello*3')
    print letterChanges("fun times!")
	
def letterChanges(str):
    newstring = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in str:
        if ord('a') <= ord(letter) and ord(letter) < ord('z'):        
            ch_str = ord(letter) + 1
            if ch_str in map(ord, vowels):
                newstring += chr(ch_str - 32)
            else:
                newstring += chr(ch_str)
        elif letter == 'z':
            newstring += 'A'
        else:
            newstring += letter
    return newstring
main()