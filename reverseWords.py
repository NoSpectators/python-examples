def main():
    f = open('fun.txt', 'rw')
    file_words = [] 
    for line in f:
        file_words.append(line)

    for i in range(len(file_words)-1, -1, -1):
        print file_words[i] 

  
     
main()
