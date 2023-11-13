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
    recipes : list
        list containing all parsed data from the txt files.
        [Recipe obj, Recipe obj, ...]
    number_of_recipes : int
        keeps count of the number of recipes in the first generation
        to be referenced for later generations.
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
            # iterate through each line of txt file and retreive recipe name, and amount
            for text in content:
                individual_line = text.split()
                individual_line.append("\n")
                self.add_line_to_dictionary(individual_line)


            
            print(self.word_dictionary)
                
    
    def add_line_to_dictionary(self, line : list) -> None:
        """Adds the individual words of a line of a poem as a key to a dictionary
        and the word that follows and its occurance as the value"""

        index = 0

        for word in line:

            if(self.dict_has_word(word)):
                freq_dict = self.word_dictionary.get(word.lower())
                if(index < len(line)-1):
                    next_word = line[index + 1]
                    updated_freq = self.add_next_word(next_word, freq_dict)
                    self.word_dictionary[word.lower()] = updated_freq 
                
                

            else:

                
                if (index< len(line) - 1):
                    self.word_dictionary[word.lower()] = {line[index + 1] : 1}

            freq = self.word_dictionary.get(word.lower())
            
          
            index += 1



        
    def add_to_word_dict(self, word):
        """adds a new word to the word dictionary"""

        self.word_dictionary[word.lower()] = {}

        
    def add_next_word(self, word : str, freq: dict):



        if(isinstance(freq, dict)):
            
            num = freq.get(word.lower())

            if (num == None):
                freq[word.lower()] = 1
            else:
                freq[word.lower()] = num + 1
          
        
        return freq



    
    
    def dict_has_word(self, word: str):
        """Checks to see if the word dictionary contains the word as hand"""

        if (self.word_dictionary.get(word.lower()) == None):
            return False
        else:
            return True



        
def main():

    inspiring_set_name = input("What is the name of the folder containing the poems: ")

    reader = FileReader(inspiring_set_name)
    reader.open_and_read_file()
    

if __name__ == "__main__":
    main()