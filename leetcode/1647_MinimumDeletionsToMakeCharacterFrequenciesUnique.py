class Solution:
    def minDeletions(self, s: str) -> int:
        character_frequency = self.count_character_frequency(s)

        character_by_frequency, duplicated_frequencies = self.get_character_by_frequency(character_frequency)

        return self.calculate_all_deletions(character_by_frequency, duplicated_frequencies)

    def count_character_frequency(self, s: str):
        character_frequency = {}

        for character in s:
            if character not in character_frequency:
                character_frequency[character] = 1
            else:
                character_frequency[character] += 1

        return character_frequency

    def get_character_by_frequency(self, character_frequency):
        character_by_frequency = {}
        duplicated_frequencies = []
 
        for character, frequency in character_frequency.items():
            if frequency not in character_by_frequency:
                character_by_frequency[frequency] = character
            else:
                duplicated_frequencies.append(frequency)

        return (character_by_frequency, duplicated_frequencies)

    def calculate_all_deletions(self, character_by_frequency, duplicated_frequencies):
        deletions = 0

        for frequency in duplicated_frequencies:
            deletions += self.calculate_frequency_deletions(character_by_frequency, frequency)

        return deletions

    def calculate_frequency_deletions(self, character_by_frequency, frequency: int):
        current_deletions = 1
        current_frequency = frequency - 1

        while current_frequency > 0:
            if current_frequency not in character_by_frequency:
                character_by_frequency[current_frequency] = 'Placeholder'
                break
            
            current_deletions += 1
            current_frequency -= 1

        return current_deletions
