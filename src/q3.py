"""
This question will take the dictionary built in count_char_n_grams() as an argument
to calculate the possibilities for the next letter given the previous n-1 letters 
(from the prompt string).
You can assume that the parameter prompt has length n-1, and counts has the 
format of the map output by count_char_n_grams().
There are comments describing its functionality, but you will need to write the documentation.
"""
from typing import Dict

def next_letter_frequency(prompt: str, counts: Dict[str, int]) -> Dict[str, int]:
    # Return a dictionary where the keys are the options for the nth character (given
    # the previous n-1 characters), and the values are the number of times that that
    # character is the nth character in the counts.
    # For example, in the string "Rasika has a cat. Ellen has a cat. Miguel has a dog."
    # with n=4, we know that count_char_n_grams() should have included that " a c"
    # appears twice and " a d" appears once. So, next_letter_frequency(" a ", counts)
    # should return the dictionary {c: 2, d: 1} because, out of all the times that
    # " a *" appears, * is c twice and * is d once.
    """Counts the frequency of possible next letters given a prompt and n-gram counts
    
    Parameters
    -------------
    prompt
        str: the first n-1 letters of the n-gram we want to search for
    counts
        Dict[str, int]: the dictionary of n-grams and their frequencies from count_char_n_grams()
    
    Return
    -------------
    Dict[str, int]
        A dictionary where the keys are possible nth letters after prompt,
        values are the number of times that each letter appears as the nth
    """
    possible_n:Dict[str, int] = {}
    for key, value in counts.items():
        if key[:-1] == prompt:
            possible_n[key[-1]] = value
    return possible_n
