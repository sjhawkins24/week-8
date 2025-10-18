from collections import defaultdict, Counter
import numpy as np


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
                    print(f"{word}, is the last word in the corpus. No further words")    


        self.term_dict = return_dict

        return None


    def generate(self, seed_term=None, term_count=15):
        #Start by getting the corresponding word 
        seed_word = self.corpus.split(" ")[seed_term]
        #Get the new sentance 
        sentance = self.get_next_word(term_count, [seed_word])
        #Add the sentance to the initial word
        self.sentance = " ".join(sentance)

        return None
    
    def get_next_word(self, seed_term, sentance):
        #Start by getting the corresponding word 
        seed_word = self.corpus.split(" ")[seed_term]
        
        #sentance = [seed_word]
        if seed_term != 0:
            #get the possible next words
            states = self.term_dict[seed_word]
            #pick a new word 
            next_word = str(np.random.choice(states))
            
            try:
                sentance.append(next_word)

            except: 
                print("No next word ")
            return self.get_next_word(seed_term - 1, sentance)    
            
        else: 
            return sentance  