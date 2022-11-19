import misc.difficulty as difficulty

CLEAR = "\n" * 100
MENU_SCENE = 0
RULES_SCENE = 1
SETTINGS_SCENE = 2
GAME_SCENE = 3
END_SCENE = 4

current_scene = MENU_SCENE
engine = None

def set_scene(scene: int):
    global current_scene
    current_scene = scene
    if current_scene == MENU_SCENE:
        engine.stop_game()
    draw("")

def refresh():
    draw("")

def draw(argument):
    print(CLEAR)
    if current_scene == MENU_SCENE:
        draw_menu_scene(argument)
    elif current_scene == RULES_SCENE:
        draw_rules_scene(argument)
    elif current_scene == SETTINGS_SCENE:
        draw_settings_scene(argument)
    elif current_scene == GAME_SCENE:
        draw_game_scene(argument)
    elif current_scene == END_SCENE:
        draw_end_scene(argument)

def draw_game_scene(argument):
    print(f"DEBUG [should not be visible] {engine.chosen_word}")
    print(f"Chosed word has {len(engine.chosen_word)} letters")
    print(f"Bulls {engine.stats[-1].bulls} | Cows: {engine.stats[-1].cows}")
    print(f"Tries left: {engine.tries_amount - len(engine.stats) + 1}")
    print("\n\n")
    print("==============================")
    print("1 - Exit to the menu")
    if argument == "1":
        set_scene(MENU_SCENE)
    else:
        engine.validate_word(argument)
        if argument != "":
            refresh()

def draw_end_scene(argument):
    if engine.stats[-1].bulls == len(engine.chosen_word):
        print("You won!")
        print(f"You made it with {len(engine.stats)} tries")
    else:
        print("You lost ;c")

    print(f"The chosen word was: {engine.chosen_word}")
    print("\n\n")
    print("==============================")
    print("1 - Exit to the menu")
    print("2 - Save highscore")
    if argument == "1":
        set_scene(MENU_SCENE)
    if argument == "2":
        engine.save_stats()

def draw_menu_scene(argument):
    print("============|MENU|============")
    print("1 - New Game")
    print("2 - Rules")
    print("3 - Settings")
    print("4 - Exit")
    print("==============================")

    if argument == "1":
        engine.start_game()
        set_scene(GAME_SCENE)
    elif argument == "2":
        set_scene(RULES_SCENE)
    elif argument == "3":
        set_scene(SETTINGS_SCENE)

def draw_rules_scene(argument):
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
    print("1 - Come back")
    print("===============================")

    if argument == "1":
        set_scene(MENU_SCENE)

def draw_settings_scene(argument):
    print("============|SETTINGS|============")
    print("1 - Modify difficulty")
    if engine.difficulty == difficulty.EASY:
        print("EASY")
    elif engine.difficulty == difficulty.NORMAL:
        print("NORMAL")
    else:
        print("HARD")
    print("2 - Modify number of tries")
    print(f"{engine.tries_amount}")
    print("3 - Come back")
    print("==================================")

    if argument == "1":
        engine.change_difficulty()
        refresh()
    elif argument == "2":
        engine.change_tries_amount()
        refresh()
    elif argument == "3":
        set_scene(MENU_SCENE)