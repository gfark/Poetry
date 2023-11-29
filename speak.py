"""
Author: Greta Farkas

Course: CSCI 3725
Prof. Harmon
------------
This file allows us to to speak the words in the poems and 
print them clearly on the page for the viewer
"""
import os 
from turtle import *


class SpeakWords:

    """
    This class prvodies the functionality for the program to spring out its words
    and speak them to the consol. It also shows the given poems to the consol
    
    
    """

    def __init__(self, poem=None):
        """
        Innitalizes the class SpeakWords

        Parameters:

            poem (optional) -- none if not inputted
        """
        self.poem = poem
        


    def speak(self, poem: str):
        """
        This function speaks the words that are presented on the screen

        Parameters:
            poem: str
                - poem to speak and display
        """
        t = Turtle()
        result = poem.splitlines()
        t.hideturtle()
        t.write(poem, align="center", font=("Cooper Black", 25, "italic"))
        for line in result:
            os.system("say " + line)
            
        t.clear()


  
