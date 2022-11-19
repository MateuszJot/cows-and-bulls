class validator(object):
    def validate_word(self, base_word, word):
        cows = 0
        bulls = 0

        if not self.is_isogram(word):
            return (0, 0)

        if len(word) > len(base_word):
            word = word[0:(len(base_word) - 1)]

        for i in range (0, len(base_word)):
            if i >= len(word):
                break

            if(word.count(base_word[i]) == 1):
                cows = cows + 1
            if base_word[i] == word[i]:
                bulls = bulls + 1
                cows = cows - 1
                if cows < 0:
                    cows = 0

        return (cows, bulls)

    def is_isogram(self, word):
        unique_letters = []

        for l in word:
            if l in unique_letters:
                return False
            unique_letters.append(l)
 
        return True