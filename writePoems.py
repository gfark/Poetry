"""
Author: Greta Farkas
Course: CSCI 3725
Prof. Harmon
------------
This class generates poems. There are options for an alliteration poem
and a rhyming poem. It uses the SpeakWords class to out put its poems.
It uses the frequencies off following words and a probablitity matrix 
to produce the following words.

Dependencies: glob
"""
import glob as gl
import numpy as np
from speak import SpeakWords


class WritePoems:
    """
    This class serves to provide functionality generate the next 
    word in the poem based on the current word given. It searches
    the word dictionary for the best matches, as well as construct
    poetry.
    ...
    Attributes:
    -----------
    

        word_dictionary : dict 
            a word dictionary with the word that follows and the frequency of it

        start_letter : str
            used for alliteration poem, the letter to be repeated

        suffix : str
            used for rhyming poem, the suffix to be rhymed with

        type_of_poem: str
            A for alliteration, R for rhyming

    """

    def __init__(self, word_dictionary : dict(), start_letter: str, suffix: str, type_of_poem: str):
        """
        This initializer serves to create variables for the attributes of this class.
        ...
        Parameters:
        -----------
        word_dictionary : dict 
            a word dictionary with the word that follows and the frequency of it

        start_letter : str
            used for alliteration poem, the letter to be repeated

        suffix : str
            used for rhyming poem, the suffix to be rhymed with

        type_of_poem: str
            A for alliteration, R for rhymin
        
        """
        
        self.word_dictionary = word_dictionary
        self.start_letter = start_letter
        self.current_freq_matrix = "high"
        self.suffix  = suffix
        self.type_of_poem = type_of_poem
        

    
    def get_start_word(self, start_word) -> str:

        """
        This function checks to see if the user inputted start word exist, if it does not
        it choose a word from the knowledge base that starts with the first letter

        Parameters:
        start_word: str
            inputted word to start the string

        Returns: 
            str: a new word 
        """

        sw = self.word_dictionary.get(start_word)

        #makes sure there is a value for the dictionary key
        if (isinstance(sw, dict)):
            self.start_word = start_word
            return start_word
        else:
            #
            new_start = self.same_first_letter(start_word, self.word_dictionary)
            self.start_word = new_start
            return new_start

        

    def same_first_letter(self, letter, word_dict: dict) -> str:
        """
        This function obtains the words that starts with the same letter of the 1st word of the 
        poem. These then become the next options for the next word in the poem.

        Parameters:
            letter: str
                specifced start letter
            word_dict: dict
                a word dictionary to get the words from

        Return:
            a word with the same letter

        """

        same_letter_list = []

        number_of_words = 0
        for key in word_dict:
            #if the word starts with the same letter, it addes it to the same letter list
            if key[0] == letter.lower():
                number_of_words += 1
                same_letter_list.append(key)

        

        #choose a word at random from the list
        index = np.random.randint(number_of_words)
        
        return same_letter_list[index]
    
    

    def generate_alliteration_poem(self, word_dict: dict, number_of_words: int) -> str:
        """
        This function generates a new poem using helper functions in the WritePoems class
        
        Parameters:
            word_dict : dict
                a dictionary of words with the words that follow them and the frequency 
                that they follow

            number_words : int
                number of words in a poem
            
        Return:
            a generate poem in a str
        """

        poem = ""

        #gets the starting word
        starting_word = self.same_first_letter(self.start_letter, self.word_dictionary)
        poem += starting_word

        word_count = 0

        #starting word set a the current word
        current_word = starting_word
        words_per_line = 0

        while (word_count <= number_of_words):


            #checks if the currrent word has a value in the dictionary
            if (isinstance(word_dict.get(current_word), dict)):

                #gets the following word based of the words that follow it
                next_word = self.get_next_word(current_word, "alliteration")

            else:

                #if theres no value picks another letter with the same word
                next_word = self.same_first_letter(self.start_letter, self.word_dictionary)

            if not (next_word == "\n"):
                
                if (words_per_line == 7):
                    poem += "\n" + next_word
                    words_per_line = 1

                else:
                    poem += " " + next_word
                    words_per_line += 1
    
                
            #adds word to poem wit
            

            #sets the current word to the new word
            current_word = next_word
            word_count += 1
            
        return poem

    
    def get_next_word(self, current_word: str, poem_type: str) -> str:
        """
        The function gets the next word to be added to the poem based on the poem type
        and the current word.

        Parameters:
            current_word: str
                current word in the poem -- most recently added
            
            poem_type : str
                type of poem, alliteration or rhyme

        Return:
            next word to be added to the poem
        """

        #gets the current word, frequency word dictionarty from the big word dictionary
        following_words = self.word_dictionary.get(current_word)
        
        #words that have the same letters
        same_start = []

        #all words
        all_words = []

        for key in following_words:

            #adds the word and the frequency to a new list
            pairing = [key, following_words.get(key)]

            #checks if the word is not next line, there is no key and if the letters start with the same letter
            if (current_word != "\n" and key[0] == current_word[0]):
                same_start.append(pairing)
                
            #letters do not start with the same letter
            if (current_word != "\n"):
                all_words.append(pairing)

            #word is a next line
            elif(current_word == "\n"):
                
                return self.same_first_letter(self.start_letter, self.word_dictionary)
        
        #if there is only one value in the same start
        if(len(same_start) > 1):
            return self.choose_word(same_start, "A")
       
       #if there are not words with the same start chooses based on frequency
        else:
            return self.choose_word(all_words, "A")


    def choose_word(self, word_list: list, type_of_poem: str, ignore_word_list=False, next_word="") -> str:
        """
        This function chooses the a word based on the frequency 

        Parameters:
            word_list: list
                list of words

        Return:
            chosen_word: str
                word to be added to the poem
        """

        length = len(word_list) 
       

        if(ignore_word_list == True):
            return next_word

        #if there is more than one word in the list
        if (length > 1):

            #determines what type of word frequency to use
            freq = self.choose_frequency()
            

            #sorts words in the list by their frequency
            word_list = self.sort_freq(word_list, freq)
           
            #choose a word at random from the sorted frequency list
            new_length = len(word_list)
          
            index = np.random.randint(new_length)


        #if theres only one word in the list, returns that word
        elif (length == 1):

            

            pairings = word_list[0]
            
            return pairings[0]
        
        #for alliteration poem
        elif (type_of_poem == "A"):
            return self.same_first_letter(self.start_letter, self.word_dictionary)
        
        elif (type_of_poem == "R"):
            return self.find_rhyme(word_list)
        #for a rhyming poem
    

        choose_pairing = word_list[index]
        chosen_word = choose_pairing[0]
        return chosen_word
    

    def choose_frequency(self):
       """
       This function uses a probablitiy transition matrix to determine if the next
       word should be a word that follows the word frequently, or infrequently
       """

       transition_matrix = { 
            "high": {"high": 0.3, "mid": 0.5, "low": 0.2},
		    "mid": {"high": 0.7, "mid": 0.2, "low": 0.1},
		    "low": {"high": 0.4, "mid": 0.3, "low": 0.3},}
       
       freq = list(transition_matrix.keys())

       temp = np.random.choice (freq,p= [transition_matrix[self.current_freq_matrix][f] for f in freq])

        #returns type of frequency, high, mid, or lo
       return temp
       

    def sort_freq(self, word_list: list , freq: str):
        """
        This function sorts a given word list based on their frequencies

        Paramenters:
            word_list: list
                list of words and their corresponding frequencies
            
            freq: str
                type of frequency to return: low, mid, or high
        
        Return:
            a list of the corresponding frequencies

        """
        #initializes lists
        highest_freq = []
        lowest_freq = []
        middle_freq = []
        max = 0
        min = 1
        
        #words that used to be the max and now are not
        needs_placement = []


        for word in word_list:

            #checks coordinate for frequency
            if word[1] > max:
                max = word[1]

                #relocates old high frequency words
                for i in highest_freq:
                    needs_placement.append(i)

                highest_freq = [word]

            #adds word to max list
            if word[1] == max:

                highest_freq.append(word)

            #adds word to min list
            if word[1] == min:
                if min <= max:
                    min = word[1]

                lowest_freq.append(word)

            if (word[1] < max and word[1] > min) :
                middle_freq.append(word)
        

        if (len(needs_placement) > 0):

            for i in needs_placement:
                
                if i[1] > min:
                    middle_freq.append(i)
                    
                if i[1] == min:
                    lowest_freq.append(i)


        if (freq == "high" and len(highest_freq) > 0):
            return highest_freq
        elif (freq == "mid" and len(middle_freq) > 0):
            return middle_freq
        elif(freq == "low" and len(lowest_freq) > 0):
            return lowest_freq
        else:
            return highest_freq
            

    def remove_punctuation(self, word : str) -> str:
        """
        a function that removes punctation to get a word alone

        Parameters:
            word: str
                word to strip 
            
        Return:
            word stripped
        """

        #list of unwanted punctuation
        punc = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        stripped_word = ""
        
        for letter in word:
            
            if letter not in punc:
                stripped_word += letter

        
        return stripped_word
        

    def generate_rhyming_poem(self, word_dict: dict, number_of_words: int, suffix: str) -> str:
        """
        generates a rhyming poem 
        """
        #keeps track of rhyming pattern
        start_word = "the"
        rhyme = 0
        word_count = 0

        poem = " "
        poem += start_word

        #adds starts word
        current_word = start_word

        #initiates next word
        next_word = ""

        while(word_count <= number_of_words):

            
            if (isinstance(word_dict.get(current_word), dict)):
                #rhyme on the 3rd or 6th word
                if rhyme == 3 or rhyme == 6:

                    next_word = self.get_next_word_rhyme(current_word, True)
                    
                    
                
                #reset rhyme count
                elif rhyme == 7:
                    rhyme = 0
                    next_word = self.get_next_word_rhyme(current_word, False)
                   

                else:
            
                    next_word = self.get_next_word_rhyme(current_word, False)
                
            else:
                next_word = self.find_rhyme(word_dict, False)

           
            if (isinstance(next_word, list)):
                new_next = next_word[0]
                next_word = new_next
            poem += " " + next_word

            current_word = next_word
            rhyme += 1
            word_count += 1
        
        return poem



    def get_next_word_rhyme(self, current_word: str, rhyme: bool) -> str:
        """
        Finds the next word for a rhyming poem 

        Parameters:

        current_word : str 
            current word in poem
        
        rhyme: bool 
            True if the suffix should rhyme, False if the suffix shouldn't rhyme

        Return:
            str -- new word
        """

        #gets the current word, frequency word dictionarty from the big word dictionary
        following_words = self.word_dictionary.get(current_word)
        new_word_list =[]
        rhyming_word_list = []

        for key in following_words:
             
             #createsa a word pairing
             pairing = [key, following_words.get(key)]
             
             if(current_word != "\n"):
                  
                  new_word_list.append(pairing)

                  if (rhyme):
                    stripped_word = self.remove_punctuation(pairing[0])
                    does_rhymes = self.does_rhyme(stripped_word)

                    if (does_rhymes):
                        rhyming_word_list.append(pairing)

             elif(current_word == "\n"):
                  
                  ##if rhyme and if not rhyme
                  ###get word from the dictionary function
                  return self.find_rhyme(self.word_dictionary, False)
                  

        if (rhyme):
             
             if(len(rhyming_word_list) > 1):
                  return self.choose_word(rhyming_word_list, "R")
             
             if(len(rhyming_word_list) == 1):
                  return rhyming_word_list[0]
             else:
                  ###get rhymes from the entire word dictionary in another function
                  return self.find_rhyme(self.word_dictionary, True)
        else:
             
             return self.choose_word(new_word_list, "R") 
            
        
    
    def does_rhyme(self, word: str) -> bool:
        """
        Recieves a rhyming word from the frequency list and checks to see
        if the suffix rhymes with the word at hand
        """

        word_length = len(word)

        suffix_length = len(self.suffix)

        index = word_length - suffix_length 
                

        if word[index:] == self.suffix:

            return True
        else:
            return False

        
    def find_rhyme(self, word_dict: dict, rhyme: bool) -> str:
        """
        Finds a word that rhymes with the suffix from the word dictionary

        Parameters:
            word_dict : dict 
                word dictionary
            
            rhyme: bool
                True if the word should rhyme, False if not
        
        """
        rhyme_list = []
        all_words = []
        

        number_of_rhyme_words = 0
        number_of_words = 0

        for key in word_dict:
            #if the word starts with the same letter, it addes it to the same letter list
            if key[len(key) - len(self.suffix):] == self.suffix.lower():
                number_of_rhyme_words += 1
                rhyme_list.append(key)
            
            all_words.append(key)
            number_of_words += 1
                


        #choose a word at random from the list
        if(rhyme):
            index = np.random.randint(number_of_rhyme_words)
            return rhyme_list[index]
        else:
            index = np.random.randint(number_of_words)
            return all_words[index]
 
    def evaluate_alliteration(self, poem: str, letter: str):
        """
        evaluates an alliteration poem based on the amount of words
        that start with the same letter. There is a higher evaluation 
        if it is repetitive.

        Parameters: 
            poem: str - string of poems
        """

        lines = 0
        double_letter = 0
        letter_occurances = 0
        past_word = False
        score = 0

        for word in poem:

            if word == "\n":
                lines += 1

            if(word[0].lower() == letter.lower()):
                if (past_word):
                    double_letter
                letter_occurances += 1
                past_word = True
            
            elif (past_word):
                past_word = False
                
        if (letter_occurances > lines) :
            amount = (letter_occurances - lines) * 3
            score += amount
        
        if (double_letter > 0):
            score += (double_letter * 5)
        return score

   

    def create_poem(self, number_of_poems) -> str:
        """
        this function is the driver function to generate a number of poems

        Parameters:
            number_of_poems: int
                number of poems to generate

        Return:
            full_string: str
                string with all the poems together
        """

        full_string = ""

        poem_count = 1
        while( poem_count <= number_of_poems ):

            speak = SpeakWords()
            full_string += "\nPOEM " + str(poem_count)+ ": \n"

            if self.type_of_poem.upper() == "A":
                poem = self.generate_alliteration_poem(self.word_dictionary, 56)
                
                score = self.evaluate_alliteration(poem, self.start_letter)
            
            if self.type_of_poem.upper() == "R":
                poem = self.generate_rhyming_poem(self.word_dictionary, 25, self.suffix)
                

            full_string += poem + "\n"

            
            if  self.type_of_poem.upper() == "A":
                    poem += "\nEvaluation: " + str(score)

            speak.speak(poem)
            poem_count += 1

        return full_string
            
                                                                                                                    


            
            


