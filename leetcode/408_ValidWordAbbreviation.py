class Solution:
    '''
    We can have two pointers, one for the word and another for the abbreviation.
    1. We will check the abbreviation first, we have the following cases:
        1. If we have a letter, it has to be the same as the current letter on the word, if not return False
        2. If we find a zero before any other number, return False
        3. If we have a number, keep moving the abbreviation pointer to get the number,
           increase the word pointer that number plus one
    2. At the end we should have the word pointer at the size of the word
    '''
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        digits = "0123456789"
        word_index = 0

        building_int = False
        count = ''
        for i, c in enumerate(abbr):
            if building_int:
                if c in digits:
                    count += c
                    continue
                else:
                    int_count = int(count)
                    word_index += int_count
                    count = ''
                    building_int = False

            if c == '0':
                return False

            if c not in digits:
                if word_index >= len(word) or c != word[word_index]:
                    return False
                word_index += 1
            else:
                count += c
                building_int = True

        if count != '':
            int_count = int(count)
            word_index += int_count

        return word_index == len(word)
