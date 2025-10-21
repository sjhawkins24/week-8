from collections import defaultdict, Counter
import numpy as np
import re 

class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):

        #First split the one string into a list of words 
        split_words = self.corpus.split(" ")
        #get the unique words for the keys 
        #I was origonally transforming this into a set and then a list to 
        #get the unique words, but it didn't match the output given
        unique_words = split_words
        #Create empty dictionary
        return_dict = defaultdict(list)
        #Get a list of all the words in the corpus
        for word in unique_words: 
            indices =  [i for i, x in enumerate(split_words) if x == word]

            for index in indices: 
                try: 
                    return_dict[word].append(split_words[index + 1])
                except: 
                    print(f"{word} is the last word in the corpus. No further words")    


        self.term_dict = return_dict

        return None


    def generate(self, seed_term=None, term_count=15):
        """Main generator function"""
        #Start by getting the corresponding word 
        print(seed_term)
        print(term_count)
        if seed_term is None: 
            seed_word = self.get_seed_word()#str(np.random.choice(self.corpus)) 
        else: 
            seed_word = seed_term#self.corpus.split(" ")[seed_term]
        #If the seed word exists, run the function 
        if seed_word in self.corpus:
            #Get the new sentance 
            sentance = self.get_next_word(seed_term = seed_word,
                                        term_count =  term_count,
                                        sentance =  [seed_word])
            #Add the sentance to the initial word
            self.sentance = " ".join(sentance)
        
        else: 
            raise ValueError("Selected word does not exist in corpus")

        return None
    
    def get_next_word(self, seed_term, term_count, sentance):
        """Recursive function to generate series of words to turn into a sentance"""
        #Start by getting the corresponding word 
        seed_word = seed_term #self.corpus.split(" ")[seed_term]
        
        #sentance = [seed_word]
        if term_count != 0:
            #get the possible next words
            states = self.term_dict[seed_word]
            #IF there are no next words, select a word at random 
            if(len(states) == 0):
                next_word = self.get_seed_word()#str(np.random.choice(self.corpus)) 
            else:     
            #pick a new word 

                if(len(states) > 1):
                    next_word = self.get_next_state(states)#str(np.random.choice(self.corpus))

                else: 
                    next_word = states[0]
            
            try:
                sentance.append(next_word)

            except: 
                print("No next word ")
            return self.get_next_word(next_word, term_count - 1, sentance)    
            
        else: 
            return sentance  
    def get_seed_word(self):
        """Functio to select a random word from the corpus"""
        try: 
            split_words = self.corpus.split(" ")
        except: 
            print("Corpus is empty, cannot work without vailid text docs")   
        n_words = len(split_words)
        selected_index = np.random.choice(range(1,n_words))
        return(split_words[selected_index])
    def get_next_state(self, states):
        """Function to select a random word from the states list"""
        n_words = len(states)
        selected_index = np.random.choice(range(1,n_words))
        return(states[selected_index])