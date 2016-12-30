# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:40:20 2016

@author: John
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line



song1 = Song("i love my songs, yah yah yah")
print song1.lyrics
"""
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()"""
