
from spellchecker import SpellChecker

spell = SpellChecker()

text = input("Enter a sentence: ")

dict_of_autocorrect_words = {}
for i in spell.unknown(text.split()):
    dict_of_autocorrect_words[i] = spell.correction(i)

temp = text.split()
res = []
for wrd in temp:
      
    res.append(dict_of_autocorrect_words.get(wrd, wrd))
      
res = ' '.join(res)

print(res)

