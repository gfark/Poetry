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


class WritePoems:
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

    def __init__(self, word_dictionary : dict(), start_letter: str):
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
        
        self.word_dictionary = word_dictionary
        self.start_letter = start_letter
        

    
    def start_word_exist(self, start_word) -> str:

        """
        This function checks to see if the user inputted start word exist, if it does not
        it choose a word from the knowledge base that starts with the first letter

        Parameters:
        start_word: str
            inputted word to start the string
        """

        sw = self.word_dictionary.get(start_word)

        if (isinstance(sw, dict)):
            self.start_word = start_word
            return start_word
        else:
            new_start = self.same_first_letter(start_word, self.word_dictionary)
            self.start_word = new_start
            return new_start

        

    def same_first_letter(self, letter, word_dict: dict) -> str:
        """
        This function obtains the words that starts with the same letter of the 1st word of the 
        poem. These then become the next options for the next word in the poem.

        """

    

        same_letter_list = []

        number_of_words = 0
        for key in word_dict:
            if key[0] == letter.lower():
                number_of_words += 1
                same_letter_list.append(key)

        print(number_of_words)
        index = np.random.randint(number_of_words)
        
        return same_letter_list[index]
    
    

    def generate_alliteration_poem(self, word_dict: dict, number_of_words: int) -> str:

        poem = ""
        starting_word = self.same_first_letter(self.start_letter, self.word_dictionary)
        poem += starting_word

        word_count = 0

        current_word = starting_word

        while (word_count <= number_of_words):

            print("next word: " + current_word + "\n")
            print("\n" + str(self.word_dictionary.get(current_word)))
            if (isinstance(word_dict.get(current_word), dict)):
                next_word = self.get_next_word(current_word, "alliteration")
            else:
                next_word = self.same_first_letter(self.start_letter, self.word_dictionary)

            poem += " " + next_word

            current_word = next_word
            word_count += 1
            
        return poem

    
    def get_next_word(self, current_word: str, poem_type: str) -> str:

        following_words = self.word_dictionary.get(current_word)
        
        same_start = []
        all_words = []
        for key in following_words:
            pairing = [key, following_words.get(key)]
            if (current_word != "\n" and key[0] == current_word[0]):
                same_start.append(pairing)
                
            if (current_word != "\n"):
                all_words.append(pairing)

            elif(current_word == "\n"):
                
                return self.same_first_letter(self.start_letter, self.word_dictionary)
        
        if(len(same_start) > 1):
            return self.choose_word(same_start)
       
        else:
            return self.choose_word(all_words)


    def choose_word(self, word_list: list) -> str:

        #ADD PROBABILITY MATRIX

        length = len(word_list) 
        print(length)
        if (length > 1):
            index = np.random.randint(length)

        elif (length == 1):
            pairings = word_list[0]
            return pairings[0]
        else:
            return self.same_first_letter(self.start_letter, self.word_dictionary)

        choose_pairing = word_list[index]
        chosen_word = choose_pairing[0]
        return chosen_word
    


    
    def create_poem(self, number_of_poems) -> str:

        full_string = ""

        poem_count = 1
        while( poem_count <= number_of_poems ):

            full_string += "\nPOEM " + str(poem_count)+ ": \n"

            poem = self.generate_alliteration_poem(self.word_dictionary, 50)

            full_string += poem + "\n"

            poem_count += 1


            
        return full_string
            



                                                                                                                                




            
            


