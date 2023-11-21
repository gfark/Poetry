"""
This file allows us to to speak the words in the poems 
"""
import os 
from turtle import *


class SpeakWords:

    """
    This class prvodies the functionality for the program to spring out its words
    and speak them to the consol.
    
    
    """

    def __init__(self, poem=None):
        self.poem = poem
        


    def speak(self, poem: str):
        t = Turtle()
        result = poem.splitlines()
        t.hideturtle()
        t.write(poem, align="center", font=("Cooper Black", 25, "italic"))
        for line in result:
            os.system("say " + line)
            
        t.clear()


  
