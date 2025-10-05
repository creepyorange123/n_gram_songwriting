"""
When we process text in machine learning, we often use character ngrams instead of entire words, to avoid dealing with punctuation and typos.
For example, the text "Rasika", with a value of n=4, has these character ngrams: "Rasi", "asik", and "sika".
Each of these character ngrams appears once in "Rasika", and each of them appears twice in "RasikaRasika"
(and "RasikaRasika" also has the additional character ngrams "ikaR", "kaRa", and "aRas", each of which appears once).

Please implement count_char_n_grams() below according to the comments describing its functionality.
You will need to write the documentation.
"""
from typing import Dict

def count_char_n_grams(text: str, n: int = 3) -> dict[str, int]:
    """Counts number of appearance of n-grams of a word
    
    Parameters
    -------------
    text
        str: target word we process
    n
        int: length of n-grams
    
    Return
    -------------
    dict[str, int]
        Dictionary of all existing n-grams of "text" and how many times they each appeared
    """
    pointer = 0
    ngram_counter:Dict[str,int] = {}
    while pointer <= len(text) - n:
        ngram = text[pointer: pointer+n]
        if ngram not in ngram_counter:
            ngram_counter[ngram] = 1
        else:
            ngram_counter[ngram] += 1
        pointer += 1
    return ngram_counter
