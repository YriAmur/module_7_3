import io
from pprint import pprint


print()      # Отступ


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):

        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':']
                    for punct in punctuation:
                        line = line.replace(punct, '')
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        places = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1

        return places

    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder3 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder3.get_all_words())
print(finder3.find('child'))
print(finder3.count('child'))

finder4 = WordsFinder('Rudyard Kipling - If.txt')
print(finder4.get_all_words())
print(finder4.find('you'))
print(finder4.count('you'))

finder = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder.get_all_words())
print(finder.find('the'))
print(finder.count('the'))