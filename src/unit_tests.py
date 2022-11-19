import unittest
from validator import validator
from dictionary import dictionary
from misc.difficulty import difficulty

class unit_tests(unittest.TestCase):
    validator = validator()
    dictionary = dictionary("../data/dictionary.txt")

    #Verification of the validator operations (basic and edge-cases)
    def test_validator_1(self):
        self.assertEqual((0, 6), self.validator.validate_word("spacex", "spacex"))

    def test_validator_2(self):
        self.assertEqual((0, 5), self.validator.validate_word("spacex", "spacew"))
    
    def test_validator_3(self):
        self.assertEqual((0, 0), self.validator.validate_word("spacex", "wwwwww"))

    def test_validator_4(self):
        self.assertEqual((0, 0), self.validator.validate_word("spacex", ""))

    def test_validator_5(self):
        self.assertEqual((0, 0), self.validator.validate_word("spacex", "wwwwwwspacex"))

    def test_validator_6(self):
        self.assertEqual((6, 0), self.validator.validate_word("spacex", "xecaps"))

    def test_validator_7(self):
        self.assertEqual((0, 1), self.validator.validate_word("spacex", "s"))

    def test_validator_7(self):
        self.assertEqual((0, 0), self.validator.validate_word("spacex", "sawwww"))


    #Verify the length of a random word based on the difficulty
    #(Done 3 times for each difficulty to make sure that randomness doesn't affect the result)
    def test_dictionary_8(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.EASY)), 4)

    def test_dictionary_9(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.EASY)), 4)

    def test_dictionary_10(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.EASY)), 4)

    def test_dictionary_11(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.NORMAL)), 5)

    def test_dictionary_12(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.NORMAL)), 5)

    def test_dictionary_13(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.NORMAL)), 5)

    def test_dictionary_14(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.HARD)), 6)

    def test_dictionary_15(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.HARD)), 6)

    def test_dictionary_16(self):
        self.assertEqual(len(self.dictionary.get_random_word(difficulty.HARD)), 6)

unittest.main()