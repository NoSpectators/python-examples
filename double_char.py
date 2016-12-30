def main():
    str = 'The'
    str2 = 'AAbb'
    str3 = 'Hi-There'  
    print double_char(str)
    print double_char(str2)
    print double_char(str3)

def double_char(string):
    new = ''
    for i in string:
        new += 2*i
    return new

main()
