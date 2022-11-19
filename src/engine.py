import os
import scene_manager
import dictionary as dic
import misc.difficulty as difficulty
import misc.logger as logger
import validator as v

class stats(object):
    bulls = 0
    cows = 0
    word = None

    def __init__(self, a, b, word):
        self.bulls = a
        self.cows = b
        self.word = word

class engine(object):
    dictionary = dic.dictionary("../data/dictionary.txt")
    validator = v.validator()
    difficulty = difficulty.NORMAL
    tries_amount = 10

    is_playing = False
    chosen_word = None
    stats = []
    
    def __init__(self):
        scene_manager.engine = self
        self.update()

    def start_game(self):
        self.is_playing = True
        self.chosen_word = self.dictionary.get_random_word(self.difficulty)
        self.stats = [stats(0, 0, "-")]

    def stop_game(self):
        self.is_playing = False
        self.chosen_word = ""
        self.stats = [stats(0, 0, "-")]

    def save_stats(self):
        absolute_path = os.path.dirname(__file__)
        absolute_path = os.path.join(absolute_path, "../data/stats.txt")

        try:
            f = open(absolute_path, "w")
            f.write("---STATS---\n")
            f.write(f"WORD: {self.chosen_word}\n")
            f.write(f"TRIES: {len(self.stats) - 1}\n")
            f.write("---HISTORY---\n")

            index = 0
            for x in self.stats:
                if index == 0:
                    index = index + 1
                    continue
                f.write(f"{index}) WORD: {x.word} | BULLS: {x.bulls} COWS: {x.cows}\n")
                index = index + 1
            f.close()
        except:
            logger.log(f"Could not save the file {absolute_path}", logger.ERROR)

    def validate_word(self, word):
        if word == "":
            return

        current_stats = self.validator.validate_word(self.chosen_word, word)

        self.stats.append(stats(current_stats[1], current_stats[0], word))

        if current_stats[1] == len(self.chosen_word):
            scene_manager.set_scene(scene_manager.END_SCENE)
        if len(self.stats) >= self.tries_amount:
            scene_manager.set_scene(scene_manager.END_SCENE)

    def change_difficulty(self):
        if self.is_playing:
            logger.log("Can't change settings ingame!", logger.WARNING)
            return

        self.difficulty = self.difficulty + 1
        if self.difficulty >= 3:
            self.difficulty = 0

    def change_tries_amount(self):
        if self.is_playing:
            logger.log("Can't change settings ingame!", logger.WARNING)
            return

        self.tries_amount = self.tries_amount + 10
        if self.tries_amount > 100:
            self.tries_amount = 10

    def update(self):
        scene_manager.draw("")
        argument = input()
        while argument != "4":
            scene_manager.draw(argument)
            argument = input()