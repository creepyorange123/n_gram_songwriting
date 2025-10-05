"""generate next character"""
from typing import List, Dict
import random
from src.q3 import next_letter_frequency
from src.q2 import count_char_n_grams

"""
Please implement generate_next_char() according to the comments describing its functionality.
You will need to write the documentation.
There are extra challenges below it, if you are interested in creating a small language model.
"""


def generate_next_char(prompt: str, counts: dict[str, int]) -> str:
    """ Generates the next character based on a given prompt and n-gram counts
    Parameters
    -------------
    prompt
        str: the first n-1 letters of the n-gram we want to search for
    counts
        dict[str, int]: the dictionary of n-grams and their frequencies from count_char_n

    Return
    -------------
    str
        A single character that is chosen randomly by frequency from the possible next characters
        based on the prompt and counts, or randomly chosen from a-z if no such characters exist
    """
    # This function should call next_letter_frequency() to get the options for 
    # the next character given the prompt (which you can assume has length n-1),
    # and then randomly choose one of the characters and return it.
    # You can also assume that counts has the format output by count_char_n_grams().

    # First call next_letter_frequency().
    # If the dictionary returned is empty (because the character ngram prompt was
    # not there in the original text), this function should randomly choose a
    # letter between a and z and return it.
    # If the dictionary returned is not empty, then this function should randomly
    # choose one of the characters which is listed as an option in the map and 
    # return it.
    next_char:Dict[str, int] = next_letter_frequency(prompt, counts)
    if next_char is not None:
        possible_char_pool:List[str] = []
        for char, freq in next_char.items():
            for i in range(freq):
                possible_char_pool.append(char)
        return random.choice(possible_char_pool)
    letter:List[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    return random.choice(letter)



# You may test out this function by calling it in a for loop and printing the letters one by one:

# text = 'catcatcatcatcat'
# n_gram_counts = count_char_n_grams(text, 4)
# prompt = 'cat'

# for i in range(1, 20):
#     next_letter = generate_next_char(prompt, n_gram_counts)
#     print(next_letter)
#     prompt = prompt[1:] + next_letter
n_gram_counts = count_char_n_grams("catcatcatcatcatcatcat", 4)
print(generate_next_char("cat", n_gram_counts))

# If you are looking for an added challenge, use the counts returned by 
# next_letter_frequency() to indicate how likely each next letter should be. 
# For example, if next_letter_frequency() returns the map {c: 2, d: 1} then 
# generate_next_char() should be twice as likely to generate c as d. You can 
# do this by generating a random number between 0 and 3. If the number is 0 
# or 1, then return c, and if the number is 2, then return d. This is an 
# added challenge, and it is expected that if you attempt it, this lab will 
# take longer than the amount of time available in class.
# DONE

# And for even more of a challenge (it is likely that you are working outside of 
# lab time): Questions 2, 3, and 4 together comprise a small language model. 
# Time to have it read some song lyrics, and have it generate songs!
# Here is a dataset of Olivia Rodrigo song lyrics: 
# https://www.kaggle.com/datasets/mehaksingal/olivia-rodrigo-lyrics-datasetl
# You may also use any dataset of song lyrics that you would like. A longer file 
# containing a large number of song lyrics will be better (since it will contain 
# more options for character ngrams).
# Once you have a string containing a large amount of song lyrics text, use the 
# for loop (from testing out q4) to generate a bunch of characters!
