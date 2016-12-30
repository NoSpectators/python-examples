# version code d345910f07ae
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

u = [1,2,3]
v = [4,5,6]
def list_dot(u,v):
    return sum([u[i]*v[i] for i in range(len(u))])
print 'dot product =',list_dot(u,v)
print ""


from random import randint
#Task 1 
def randomize(a,b):
    return randint(a,b)
    
print randomize(2,5)


movie_review_list = ["See it!", "A gem!", "Ideological claptrap!"]
def movie_review(name):    
    return name + " review: " + movie_review_list[randint(0,2)]
    
print movie_review("Superman")


mystring = "Look at me ! Look at me ! Look at me NOW ! It is fun to have fun but you have \
            to know how ."
mystring2 = ["Look at me !", "Look at me !", "Look at me NOW !", "It is fun to have fun but you have \
            to know how ."]
def word_count(string):
    my_string = string.lower().split() 
    my_dict2= {}
    my_dict = {}
    for item in my_string:           
            
        if item in my_dict:
            my_dict[item] += 1
            my_dict2[item] = len(item)
            
        else:
            my_dict[item] = 1
            my_dict2[item] = len(item)
            
    max_length = max(zip(my_dict2.values(), my_dict2.keys()))
    ranked_count = sorted(zip(my_dict.values(), my_dict.keys()))
    ranked_length = sorted(zip(my_dict2.values(), my_dict2.keys()))
    minimum_key = min(my_dict, key=lambda k: my_dict[k])  
    maximum_key = max(my_dict, key=lambda k: my_dict[k])  
    min_value = my_dict[min(my_dict, key=lambda k: my_dict[k])]
    max_value = my_dict[max(my_dict, key=lambda k: my_dict[k])]

    print 'word count-->',my_dict
    print ''
    print 'word length-->',my_dict2
    print ''
    print 'number of items in string =',len(my_string)
    print ''
    print 'word with longest letters is',max_length
    print ''
    print 'sorted words by count is', ranked_count
    print ''
    print 'sorted words by length is',ranked_length
    print ''
    print 'key corresponding to min value in my_dict is', minimum_key
    print ''
    print 'key corresponding to max value in my_dict is', maximum_key
    print ''
    print 'minimum value corresponding to my_dict is', min_value
    print ''
    print 'maximum value corresponding to my_dict is', max_value

print ''

def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    D = {}
    for i, substr in enumerate(strlist):
      for word in substr.split():
        if word not in D:
          D[word] = {i}
        else:
          D[word].add(i)
    return D
print makeInverseIndex(['hello world','hello','hello cat','hellolot of cats'])
print ''
## 2: (Task 2) Make Inverse Index
def makeInverseIndex2(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.
    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    index={}
    for i in range(len(strlist)):
        lst=strlist[i].split()
        for j in lst:
            if(j in index.keys()):
                index[j]= index[j]|{i}
            else:
                index[j]={i}
    return index

print makeInverseIndex2(['hello world','hello','hello cat','hellolot of cats']) 

## 3: (Task 3) Or Search
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.
    
    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    pass



## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    pass

