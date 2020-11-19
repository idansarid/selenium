import enchant
import itertools


lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

all = []
all = lower_a
permotations = []
english_dictionary = enchant.Dict("en")

str("a")
def is_part_of_existing_word(string, words_dictionary):
    suggestions = words_dictionary.suggest(string)
    return any(string in suggestion
               for suggestion in suggestions)


for r in range(0, 5):
    for s in itertools.product(all, repeat=r):
        if len(s) == 0:
            continue
        srt = ''.join(s)
        if is_part_of_existing_word(string=srt, words_dictionary=english_dictionary) and (len(srt) == 3
                                                                                          or len(srt) == 4):
            permotations.append(''.join(s))
            print(''.join(s))

permotation_len = len(permotations)
with open('list.txt', 'w') as f:
    for item in permotations:
        f.write("%s\n" % item)
