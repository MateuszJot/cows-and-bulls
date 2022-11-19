from misc.difficulty import difficulty

class scene_manager(object):
    CLEAR = "\n" * 100

    #scenes
    MENU_SCENE = 0
    #scene actions
    MENU_NEW_GAME = "1"
    MENU_RULES = "2"
    MENU_SETTINGS = "3"
    MENU_EXIT_GAME = "4"

    RULES_SCENE = 1
    #scene actions
    RULES_TO_MENU = "1"

    SETTINGS_SCENE = 2
    #scene actions
    SETTINGS_CHANGE_DIFFICULTY = "1"
    SETTINGS_CHANGE_TRIES = "2"
    SETTINGS_TO_MENU = "3"

    GAME_SCENE = 3
    #scene actions
    GAME_TO_MENU = "1"

    END_SCENE = 4
    #scene actions
    END_TO_MENU = "1"
    END_SAVE_SCORE = "2"

    current_scene = MENU_SCENE
    engine = None

    def __init__(self, engine):
        self.engine = engine

    ### DRAW LOGIC ###
    def refresh(self):
        self.draw("")

    def set_scene(self, scene: int):
        self.current_scene = scene
        if self.current_scene == self.MENU_SCENE:
            self.engine.stop_game()
        self.refresh()

    def draw(self, argument):
        print(self.CLEAR)
        if self.current_scene == self.MENU_SCENE:
            self.draw_menu_scene(argument)
        elif self.current_scene == self.RULES_SCENE:
            self.draw_rules_scene(argument)
        elif self.current_scene == self.SETTINGS_SCENE:
            self.draw_settings_scene(argument)
        elif self.current_scene == self.GAME_SCENE:
            self.draw_game_scene(argument)
        elif self.current_scene == self.END_SCENE:
            self.draw_end_scene(argument)

    ### SCENES ###
    def draw_menu_scene(self, argument):
        print("============|MENU|============")
        print("1 - New Game")
        print("2 - Rules")
        print("3 - Settings")
        print("4 - Exit")
        print("==============================")

        if argument == self.MENU_NEW_GAME:
            self.engine.start_game()
            self.set_scene(self.GAME_SCENE)
        elif argument == self.MENU_RULES:
            self.set_scene(self.RULES_SCENE)
        elif argument == self.MENU_SETTINGS:
            self.set_scene(self.SETTINGS_SCENE)

    def draw_rules_scene(self, argument):
        print("============|RULES|============")
        print("""
        One player (the Host) thinks of an isogram word (i.e. no letter appears 
        twice) and, if the word length is not pre-determined, announces the 
        number of letters in the word. Other players (the Guessers) try to 
        figure out that word by guessing isogram words containing the same 
        number of letters. The Host responds with the number of Cows & Bulls 
        for each guessed word. As with the digit version, "Cow" means a letter 
        in the wrong position and "Bull" means a letter in the right position.
        """)
        print("1 - Back")
        print("===============================")

        if argument == self.RULES_TO_MENU:
            self.set_scene(self.MENU_SCENE)

    def draw_settings_scene(self, argument):
        print("============|SETTINGS|============")
        print("1 - Modify difficulty")
        if self.engine.difficulty == difficulty.EASY:
            print("EASY")
        elif self.engine.difficulty == difficulty.NORMAL:
            print("NORMAL")
        else:
            print("HARD")
        print("2 - Modify number of tries")
        print(f"{self.engine.tries_amount}")
        print("3 - Come back")
        print("==================================")

        if argument == self.SETTINGS_CHANGE_DIFFICULTY:
            self.engine.change_difficulty()
            self.refresh()
        elif argument == self.SETTINGS_CHANGE_TRIES:
            self.engine.change_tries_amount()
            self.refresh()
        elif argument == self.SETTINGS_TO_MENU:
            self.set_scene(self.MENU_SCENE)

    def draw_game_scene(self, argument):
        print(f"DEBUG [should not be visible] {self.engine.chosen_word}")
        print(f"Chosed word has {len(self.engine.chosen_word)} letters")
        print(f"Bulls {self.engine.stats[-1].bulls} | Cows: {self.engine.stats[-1].cows}")
        print(f"Tries left: {self.engine.tries_amount - len(self.engine.stats) + 1}")
        print("\n\n")
        print("==============================")
        print("1 - Exit to the menu")
        if argument == self.GAME_TO_MENU:
            self.set_scene(self.MENU_SCENE)
        else:
            self.engine.validate_word(argument)
            if argument != "":
                self.refresh()

    def draw_end_scene(self, argument):
        if self.engine.stats[-1].bulls == len(self.engine.chosen_word):
            print("You won!")
            print(f"You made it with {len(self.engine.stats)} tries")
        else:
            print("You lost ;c")

        print(f"The chosen word was: {self.engine.chosen_word}")
        print("\n\n")
        print("==============================")
        print("1 - Exit to the menu")
        print("2 - Save highscore")
        if argument == self.END_TO_MENU:
            self.set_scene(self.MENU_SCENE)
        if argument == self.END_SAVE_SCORE:
            self.engine.save_stats()