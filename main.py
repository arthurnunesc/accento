import string
from collections import Counter


def analyze_text(text_to_be_analyzed):
    alpha = list(string.ascii_lowercase)
    
    alpha_apostrophe = ["á", "é", "í", "ó", "ú", "ç"]
    alpha_double_quotes = ["ä", "ë", "ï", "ö", "ü", "ÿ"]
    alpha_grave = ["à", "è", "ì", "ò", "ù"]
    alpha_tilde = ["ã", "ẽ", "ĩ", "õ", "ũ", "ñ"]
    alpha_circumflex = ["â", "ê", "î", "ô", "û"]
    alpha_alt_gr = ["ø", "å", "ß", "µ", "ð", "þ", "œ", "æ"]
    
    alpha_incidences = []
    alpha_percentages = []

    digits = list(string.digits)
    digits_incidences = []
    digits_percentages = []

    punctuation_marks = list(string.punctuation)
    punctuation_marks_incidences = []
    punctuation_marks_percentages = []


    # Deletes every single space in the input
    text_to_be_analyzed_without_spaces = text_to_be_analyzed.replace(" ", "")
    # Length of the input without the spaces
    length_of_text_to_be_analyzed_without_spaces = len(
        text_to_be_analyzed_without_spaces)
    # Makes all the input lowercase
    text_to_be_analyzed_without_spaces_and_all_lower_case = text_to_be_analyzed_without_spaces.lower()

    counter = Counter()
    for line in text_to_be_analyzed_without_spaces_and_all_lower_case:
        counter.update(line)

    # Iterates through every letter, digit and punctuation, if the key is not in the counter, declares its value as zero so it appears in the final counter
    for letter in alpha:
        if letter not in counter.keys():
            counter[letter] = 0
    for digit in digits:
        if digit not in counter.keys():
            counter[digit] = 0
    for punctuation in punctuation_marks:
        if punctuation not in counter.keys():
            counter[punctuation] = 0
            
    
    # Adds values of the counter to lists to make calculating percentages and displaying information easier later
    for letter in alpha:
        alpha_incidences.append(counter[letter])
    for digit in digits:
        digits_incidences.append(counter[digit])
    for punctuation in punctuation_marks:
        punctuation_marks_incidences.append(counter[punctuation])

    # Calculates the percentage of each key using the times it appeared and the total length of the text and rounds it up to 4 decimals
    for incidence in alpha_incidences:
        alpha_percentages.append(round(incidence / length_of_text_to_be_analyzed_without_spaces * 100, 4))
    for incidence in digits_incidences:
        digits_percentages.append(round(incidence / length_of_text_to_be_analyzed_without_spaces * 100, 4))
    for incidence in punctuation_marks_incidences:
        punctuation_marks_percentages.append(round(incidence / length_of_text_to_be_analyzed_without_spaces * 100, 4))

    # Creates dictionaries linking values to its keys to make display information easier
    alpha_dictionary = dict(zip(alpha, alpha_percentages))
    digits_dictionary = dict(zip(digits, digits_percentages))
    punctuation_marks_dictionary = dict(zip(punctuation_marks, punctuation_marks_percentages))

    everything_dictionary = alpha_dictionary.copy()
    everything_dictionary.update(digits_dictionary)
    everything_dictionary.update(punctuation_marks_dictionary)
    
    # Sorts everything_dictionary so it shows in order, from biggest to smallest
    sorted_everything_dictionary = sorted(everything_dictionary.items(), key=lambda x: x[1], reverse=True)

    return everything_dictionary, sorted_everything_dictionary


# Names of the files containing the texts to be analyzed
files = ['books/ptBrDomCasmurro.txt', 'books/enUsTheSubtleArtOfNotGivingAFuck.txt', 'books/esEsElCamino.txt', 'books/catElsCaminsDelParadisPerdut.txt']
texts = []

# Stores every text in the files in the list texts, multiplicating them in descending order so the first text is more influential in the final result
for index in range(len(files)):
    if index == 0:
        for x in range(4):
            f = open(files[index], encoding="utf8")
            texts.append(f.read())
            f.close()
    if index == 1:
        for x in range(3):
            f = open(files[index], encoding="utf8")
            texts.append(f.read())
            f.close()
    if index == 2:
        for x in range(2):
            f = open(files[index], encoding="utf8")
            texts.append(f.read())
            f.close()
    if index == 3:
        f = open(files[index], encoding="utf8")
        texts.append(f.read())
        f.close() 


dictionaries = []
dictionaries_organizados = []

# Applies the function analyze_text to all the texts and then stores the results in the list dictionaries
for text in texts:
    dictionaries.append(analyze_text(text)[0])
    # dictionaries_organizados.append(analyze_text(text)[1])

dictionaries_geral = dictionaries[0].copy()

# Soma todos os dicionários no vetor dictionaries e os adiciona num único dicionário chamado dictionaries_geral
for index in range(len(dictionaries)):
    if index != 0:
        # Por usar counter, descarta todos os caracteres que tem porcentagem(contagem) igual a 0
        dictionaries_geral = Counter(dictionaries_geral) + Counter(dictionaries[index])

# Divide a soma de todos os dicionários pelo número total de dicionários, efetivamente, calculando a média deles
dictionaries_geral = {k: round(v / len(dictionaries), 4) for k, v in dictionaries_geral.items()}

# Organiza o dictionaries_geral em ordem decrescente
dictionaries_geral_organizado = sorted(dictionaries_geral.items(), key=lambda x: x[1], reverse=True)
print(dictionaries_geral_organizado)

# Counter({'a': 38892, 'e': 37133, 'o': 29575, 's': 22618, 'i': 18282, 'r': 17647, 'm': 15458, 'n': 13938, 'u': 13781, 'd': 13477, 't': 12202, 'c': 9813, 'l': 8962, '\n': 8701, 'p': 8036, ',': 6870, 'v': 5083, '.': 4649, 'q': 4224, 'h': 4202, 'g': 3234, '-': 3206, 'ã': 3163, 'f': 2893, 'b': 2511, 'z': 1515, 'ç': 1311, 'é': 1167, ';': 1088, 'x': 1045, 'j': 960, 'á': 944, 'ó': 418, '?': 362, 'ú': 352, '!': 287, ':': 223, 'ê': 186, 'õ': 163, '_': 148, '«': 119, '»': 117, 'y': 99, 'ô': 64, "'": 60, 'í': 48, '0': 33, '1': 27, '(': 27, ')': 27, 'ò': 26, '8': 21, '*': 16, '7': 13, '5': 13, '4': 10, '2': 9, 'è': 8, '6': 6, '$': 5, 'k': 4, 'w': 3, 'à': 3, '9': 2, '+': 1, '=': 1, '"': 0, '#': 0, '%': 0, '&': 0, '/': 0, '<': 0, '>': 0, '@': 0, '[': 0, '\\': 0, ']': 0, '^': 0, '`': 0, '{': 0, '|': 0, '}': 0, '~': 0})
# Counter({'a': 38892, 'e': 37133, 'o': 29575, 's': 22618, 'i': 18282, 'r': 17647, 'm': 15458, 'n': 13938, 'u': 13781, 'd': 13477, 't': 12202, 'c': 9813, 'l': 8962, '\n': 8701, 'p': 8036, ',': 6870, 'v': 5083, '.': 4649, 'q': 4224, 'h': 4202, 'g': 3234, '-': 3206, 'ã': 3163, 'f': 2893, 'b': 2511, 'z': 1515, 'ç': 1311, 'é': 1167, ';': 1088, 'x': 1045, 'j': 960, 'á': 944, 'ó': 418, '?': 362, 'ú': 352, '!': 287, ':': 223, 'ê': 186, 'õ': 163, '_': 148, '«': 119, '»': 117, 'y': 99, 'ô': 64, "'": 60, 'í': 48, '0': 33, '1': 27, '(': 27, ')': 27, 'ò': 26, '8': 21, '*': 16, '7': 13, '5': 13, '4': 10, '2': 9, 'è': 8, '6': 6, '$': 5, 'k': 4, 'w': 3, 'à': 3, '9': 2, '+': 1, '=': 1, '3': 0, '"': 0, '#': 0, '%': 0, '&': 0, '/': 0, '<': 0, '>': 0, '@': 0, '[': 0, '\\': 0, ']': 0, '^': 0, '`': 0, '{': 0, '|': 0, '}': 0, '~': 0})