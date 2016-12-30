# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:44:47 2016

@author: John
"""

"""f = open("story.txt", 'r')
story_string = f.read()

def clean_text(text_string):
    cleaned_string = text_string.replace(".","") #most important
    cleaned_string = cleaned_string.replace(",","")
    cleaned_string = cleaned_string.replace(";","")
    cleaned_string = cleaned_string.replace("'","")
    cleaned_string = cleaned_string.replace(";","")
    cleaned_string = cleaned_string.replace("\n","")
    return cleaned_string

cleaned_story = clean_text(story_string)
print cleaned_story"""

f = open("story.txt", 'r')
story_string = f.read()
clean_chars = [",", ".", "'", ";", "\n"]

# Previous code for clean_text().
def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for char in special_characters:
        cleaned_string = cleaned_string.replace(char, "")    
    return(cleaned_string.lower())

def tokenize(text_string, special_characters):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return story_tokens
    
tokenized_story = tokenize(story_string, clean_chars)
print tokenized_story
#cleaned_story = clean_text(story_string, clean_chars)
#print cleaned_story