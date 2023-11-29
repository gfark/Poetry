Poetry Generator: Silverstein Spin Off
By Greta Farkas

This poetry generator uses an inspiring set of Shel Silverstein poems to generate new poems. It can generate alliteration poems and rhyming poems based off the user input. There are 3 classes involved in this poetry generator. The FilerReader class, the WritePoems class, and the SpeakWords class. 

How it works:

Open the FilerReader class and click run. The system will prompt the user for a knowledge base,  which, "Inspiring Set" or the folder containing the words, should be entered. 

It will then ask the user: "What type of poem? R for rhyming or A for alliteration:" The user should then enter R or A.

Following that, if the user enters A, the user will be prompted to enter the letter that should be used for alliteration in the poem, examples: A, P, G R. If the user enters R, the user will be prompted to enter a suffix. Examples ed, er, ing, ster.

Following that, the user will be prompted with how many poems they would like to generate. 
The poems will appear one by one on the screen and will be spoken to the user.

The FileReader Class:

This class opens a file based off the file name. It then reads in all the lines of the file, which are poems. When doing this it splits the line up into words, then adds each word to a word dictionary. The word dictionary key is the word and the value is a frequency dictionary of the word that follows and amount of times it follows. 

The WritePoems Class: 

This class generates the poems. After the word dictionary is constructed it is passed through to the WritePoems class. The poem generates the first word based on if it is an alliteration poem or rhyming poem. From there, the next words are chosen based off a frequency map, and probability matrix which directs the program to use a high, medium, or low frequency word. The poem lines are then concatenated together and added to the list of all poems generated. The write poems class also evaluates the poems based on various characteristics of each type of poem.

The SpeakWords Class:

The speak words class, speaks the lines of the poem to the consul, while presenting each poem individually. 

How was I challenged:

This project challenged me in several ways. Breaking apart poems and generating new ones based off the set called for many obstacles. Understanding how the structure and basis of poems should be constructed affect how I created the rhyming and alliteration poem. Several of the inputs may be the same word but have different capitalization and punctuation. When determining what word came next, I was challenged to come up with a way to choose the next word, in a non-random way. Although sometimes I had to use a random word. When constructing the probability matrix andI changed the values to see the different effects on the poems. After determining which probability, sorting through the word list to find which words had a high, medium, or low frequency challenged me. Figuring out what inputs to give the sorter, and the best way to return it. Through the process of creating this project, I challenged myself by trying to sort the words into categories by subject, pronoun, verbs, etc in order to create a more sensible poem, but ended up running into several issues. This expanded my mindset in how these poetry generations work. I was also challenged with my inspiring set. Shel Silverstein poems do not have the most general word choice.

Articles:

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8563571/
https://spectrum.ieee.org/this-ai-poet-mastered-rhythm-rhyme-and-natural-language-to-write-like-shakespeare
https://onlinelibrary.wiley.com/doi/abs/10.1111/oli.12274


