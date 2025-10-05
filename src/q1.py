"""
Please implement count_words() according to the documentation. There is an example input/output below.
"""

# Example:
# Input: "Rasika has a cat. Ellen has a cat."
# Output: {Rasika: 1, has: 2, a: 2, cat.: 2, Ellen: 1}
# (The keys are the words that appear in the text, and the values are the number of times that each word appears.)
# To obtain the words in a string, you may split it using a space as the delimiter (ignoring the issues with punctuation).

from typing import List, Dict

def count_words(text: str) -> dict[str, int]:
    """Counts the number of times that each word appears in the text.
    
    Parameters
    ----------
    text : str
        The text in which we want to count words
    
    Returns
    -------
    dict[str, int]
        Maps from each word to the number of times it appears in the text.
    """
    words:List[str] = text.split()
    return_frequency:Dict[str,int] = {}
    for word in words:
        if word not in return_frequency:
            return_frequency[word] = 1
        else:
            return_frequency[word] += 1
    return return_frequency
