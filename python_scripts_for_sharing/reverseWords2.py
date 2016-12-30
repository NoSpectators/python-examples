def main():
    f = open('fun.txt', 'rw')
    file_words = [] 
    for line in f:
        file_words.append(line)
    reverse(file_words)

def reverse(arr):
    for i in range(len(arr)-1, -1, -1):
        print arr[i] 
     
main()
