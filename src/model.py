import os
from typing import List, Dict
import random
from src.q3 import next_letter_frequency
from src.q2 import count_char_n_grams
from src.q4 import generate_next_char


# 1. get song length
# 2. get line length
# 3. generates song using gen_next_char and get song and get line

class SongGenerator:
    """Generates a song based on a given prompt"""
    def __init__(self, prompt: str) -> None:
        """Initializes the SongGenerator with a prompt and sets song and line lengths to 0."""
        self.prompt = prompt
        self.song_length:int = 0
        self.line_length:int = 0
        self.__n_gram_size:int = len(prompt)

    def process_input(self) -> Dict[str, int]:
        """Opens all files and use get_song_length() and get_line_length()
        to set the song and line lengths attributes, return n_gram counts"""

    def generate_song(self) -> str:
        """Use generate_next_char() iterate throughout song terminate based on lengths"""
