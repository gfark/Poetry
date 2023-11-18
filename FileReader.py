"""
Team: FantasticFour (Diego, Richard, Greta, Will)
Course: CSCI 3725
Prof. Harmon
------------
This class serves to create a fileReader object which is capable
of retrieving the recipe name from the given relative path, and 
a list of all the ingredients needed to create that recipe. This 
class is also capable of creating a dictionary with the recipe name
as the key, and a list of the ingredients as the value.

Dependencies: glob
"""
import glob as gl
import numpy as np
from writePoems import WritePoems

class FileReader:
    """
    This class serves to provide functionality to read txt files from a given folder
    and create a dictionary from the parsed data. Such data consists words from poems and a
    count of what words follow them and how many times they occur
    ...
    Attributes:
    -----------
    subfolder_name : str
        folder containing all the txt files to be parsed
    
        self.word_dictionary : dict 
            a word dictionary with the word that follows and the frequency of it

    """

    def __init__(self, subfolder_name : str) -> None:
        """
        This initializer serves to create the subfolder_name 
        attribute. This subfolder folder contains all the txt 
        files to be parsed
        ...
        Parameters:
        -----------
        subfolder_name : str
            folder containing all the txt files to be parsed
        """
        self.subfolder_name = subfolder_name
        #self.open_and_read_file()
        self.word_dictionary = dict()
       


    def open_and_read_file(self):
        """
        this function serves to open all the txt files within a given directory
        and creates a dictionary with the recipe name as the key, and a list
        of ingredients (quantity/name) as the value.
        ...
        Parameters:
        ----------
        None
        
        Returns:
        --------
        None
        """
        
        poems = []
        for file in gl.glob( self.subfolder_name + "/*.txt"):

            individual_line = []
         
            content = open(file, "r")
            # iterate through each line of txt file and retrieves a poem line
            for text in content:
            
                #splits the poem lines into a list based on spaces
                individual_line = text.split()

                #adds a line break at the end of each line
                individual_line.append("\n")

                #call to add the words in the line to the word dictionary
                self.add_line_to_dictionary(individual_line)


                
    
    def add_line_to_dictionary(self, line : list) -> None:
        """Adds the individual words of a line of a poem as a key to a dictionary
        and the word that follows and its occurance as the value
        
        Parameters:
        line: list
            - a line in a poem broken up by individual words and put into a list 
        
        Return:
            None
        """

        #keeps track of list index in order to access the word that follows it
        index = 0

        for word in line:

            #checks if word exist in the word dict
            if(self.dict_has_word(word)):

                freq_dict = self.word_dictionary.get(word.lower())

                #if before the the last index in the list, updates the current words frequency dict of the words that follow it
                if(index < len(line)-1):
                    next_word = line[index + 1]
                    updated_freq = self.add_next_word(next_word, freq_dict)
                    self.word_dictionary[word.lower()] = updated_freq 
                
            #if the word is not in the word dict
            else:
                
                #adds the word to the word dict with the following word and the frequency as a dict as its value
                if (index< len(line) - 1):
                    self.word_dictionary[word.lower()] = {line[index + 1] : 1}

            
            #increments index afte the loop is finished
            index += 1


        
    def add_next_word(self, word : str, freq: dict):

        #checks to make sure the frequency dict is not NoneType
        if(isinstance(freq, dict)):
            
            #gets number value
            num = freq.get(word.lower())

            #if it does not exist, frequency is one
            if (num == None):
                freq[word.lower()] = 1
            
            #updates frequency if the word exist 
            else:
                freq[word.lower()] = num + 1
          
        
        return freq


    
    def dict_has_word(self, word: str):
        """Checks to see if the word dictionary contains the word as hand"""

        if (self.word_dictionary.get(word.lower()) == None):
            return False
        else:
            return True
        
    def generate_poem(self):

        print(self.word_dictionary)
         
    

        #print(generate_poem.same_first_letter("The", self.word_dictionary))

    def get_word_dictionary(self):
        return self.word_dictionary
        


        
def main():

    inspiring_set_name = input("What is the name of the folder containing the poems: ")
    type_of_poem = input("What type of poem? R for rhyming or A for alliteration: ")

    if type_of_poem.upper() == "A":

        letter = input("What letter would you like alliterate: ")
        suffix = None

    elif type_of_poem.upper() == "R":

        suffix = input("What suffix would you like to rhyme?")
        letter= None

    else:

        print("Error incorrect entry, please restart.")
    
    number_of_poems = input("How many poems would you like the generate: ")

    reader = FileReader(inspiring_set_name)
    reader.open_and_read_file()
    word_dict = reader.get_word_dictionary()

    generate_poem = WritePoems(word_dict, letter, suffix, type_of_poem)

    all_poems = generate_poem.create_poem(int(number_of_poems))

    print(all_poems)
    file = open("poems/output.txt", "w")
    file.write(all_poems)
    

if __name__ == "__main__":
    main()