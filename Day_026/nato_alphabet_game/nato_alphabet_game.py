import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv").to_dict()

letters = [letter for letter in alphabet["letter"].values()]
code = [code for code in alphabet["code"].values()]

code_letters_dict = {letters[n]: code[n] for n in range(0, len(letters))}
# print(code_letters_dict)

word = input("Enter a word: ")
word_code = [code_letters_dict[letter] for letter in word.upper()]
print(word_code)
