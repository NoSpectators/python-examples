def main():
    print 'hello john!'
    str1 = 'abc hi ho'
    str2 = 'ABChi hi'
    str3 = 'hihi'
    str4 = 'hi hi he'
    array = [count_hi(str1), count_hi(str2), count_hi(str3),count_hi(str4)]
    array_print(array)
    print 'this is a change'

def array_print(array):
    for i in array:
        if (i == 1):
            print 'there is 1 \'hi\' in the string'
        else:
            print 'there are', i, 'hi\'s in the string'


def count_hi(string):
    count = 0
    for i in range(len(string)-1):
        if (string[i:i+2] == 'hi'):
    	    count += 1
    return count

main()
