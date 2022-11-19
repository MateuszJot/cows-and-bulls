import os
import random
import misc.difficulty as difficulty
import misc.logger as logger

class dictionary(object):
    # Less or equal to 4
    easy_words = None
    # Equal to 5
    normal_words = None
    # Equal or greater than 6
    hard_words = None

    """
    @param path - a relative path to the isogram words dictionary file
    """
    def __init__(self, path: str):
        self.get_words_from_file(path)

    def get_random_word(self, difficulty_level: int) -> str:
        if difficulty_level == difficulty.EASY:
            return random.choice(self.easy_words)
        if difficulty_level == difficulty.NORMAL:
            return random.choice(self.normal_words)
        if difficulty_level == difficulty.HARD:
            return random.choice(self.hard_words)
    
    def get_words_from_file(self, path: str):
        self.easy_words = []
        self.normal_words = []
        self.hard_words = []

        absolute_path = os.path.dirname(__file__)
        absolute_path = os.path.join(absolute_path, path)

        try:
            words_file = open(absolute_path, 'r')
            lines = words_file.readlines()
            for line in lines:
                raw_line = line.replace("\n", "")
                word_length = len(raw_line)
                if word_length == 5:
                    self.normal_words.append(raw_line)
                elif word_length < 5:
                    self.easy_words.append(raw_line)
                else:
                    self.hard_words.append(raw_line)
            words_file.close()
        except:
            logger.log(f"Could not open/read the file {path}", logger.ERROR)