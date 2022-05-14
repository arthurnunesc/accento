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
    print(alpha)
    print(digits)
    print(punctuation_marks)

    # Deletes every single space in the input
    text_to_be_analyzed_without_spaces = text_to_be_analyzed.replace(" ", "")
    # Length of the input without the spaces
    length_of_text_to_be_analyzed_without_spaces = len(
        text_to_be_analyzed_without_spaces)
    # Makes all the input lowercase
    text_to_be_analyzed_without_spaces_and_all_lower_case = text_to_be_analyzed_without_spaces.lower()

    alpha_counter = Counter()
    # Separates the input in lines
    for line in text_to_be_analyzed_without_spaces_and_all_lower_case:
        # Iterates through every letter in alpha
        for letter in alpha:
            if letter in line:
                alpha_counter.update(line)
            elif letter not in line and letter not in alpha_counter.keys():
                # If the letter is not present in the line and wasn't present in the lines before, declares its value as zero so it appears in the final counter and doesn't mess up and the percentage count
                alpha_counter[letter] = 0
    for value in alpha_counter.values():
        # Adds how many times each letter appeared to a list
        alpha_incidences.append(value)
    for incidence in alpha_incidences:
        # Calculates the percentage of each letter using the times it appeared and the total length of the text
        alpha_percentages.append(
            round(incidence / length_of_text_to_be_analyzed_without_spaces * 100, 4))
    alpha_dictionary = dict(zip(alpha, alpha_percentages))

    digits_counter = Counter()
    for line in text_to_be_analyzed_without_spaces_and_all_lower_case:
        for digit in digits:
            if digit in line:
                digits_counter.update(line)
            elif digit not in line and digit not in digits_counter.keys():
                digits_counter[digit] = 0
    for each in digits_counter.values():
        digits_incidences.append(each)
    for each in digits_incidences:
        digits_percentages.append(
            round(each / length_of_text_to_be_analyzed_without_spaces * 100, 4))
    digits_dictionary = dict(zip(digits, digits_percentages))

    punctuation_marks_counter = Counter()
    for line in text_to_be_analyzed_without_spaces_and_all_lower_case:
        for each in punctuation_marks:
            if each in line:
                punctuation_marks_counter.update(line)
            elif each not in line and each not in punctuation_marks_counter.keys():
                punctuation_marks_counter[each] = 0
    for each in punctuation_marks_counter.values():
        punctuation_marks_incidences.append(each)
    for each in punctuation_marks_incidences:
        punctuation_marks_percentages.append(
            round(each / length_of_text_to_be_analyzed_without_spaces * 100, 4))
    punctuation_marks_dictionary = dict(
        zip(punctuation_marks, punctuation_marks_percentages))

    everything_dictionary = alpha_dictionary.copy()
    everything_dictionary.update(digits_dictionary)
    everything_dictionary.update(punctuation_marks_dictionary)
    sorted_everything_dictionary = sorted(
        everything_dictionary.items(), key=lambda x: x[1], reverse=True)

    return everything_dictionary, sorted_everything_dictionary


# Names of the files containing the texts to be analyzed
files = ['books/ptBrDomCasmurro.txt']

texts = []

# Stores every text in the files in the list texts
for each in files:
    f = open(each, encoding="utf8")
    texts.append(f.read())
    f.close()

dictionaries = []
dictionaries_organizados = []

# Applies the function analyze_text to all the texts and then stores the results in the list dictionaries
for each in texts:
    dictionaries.append(analyze_text(each)[0])
    # dictionaries_organizados.append(analyze_text(each)[1])

dictionaries_geral = dictionaries[0].copy()

# Soma todos os dicionários no vetor dictionaries e os adiciona num único dicionário chamado dictionaries_geral
for index in range(len(dictionaries)):
    if index != 0:
        # Por usar counter, descarta todos os caracteres que tem porcentagem(contagem) igual a 0
        dictionaries_geral = Counter(dictionaries_geral) + \
            Counter(dictionaries[index])

# Divide a soma de todos os dicionários pelo número total de dicionários, efetivamente, calculando a média deles
dictionaries_geral = {k: round(v / len(dictionaries), 4)
                      for k, v in dictionaries_geral.items()}

# Organiza o dictionaries_geral em ordem decrescente
dictionaries_geral_organizado = sorted(
    dictionaries_geral.items(), key=lambda x: x[1], reverse=True)
print(dictionaries_geral_organizado)

# string = "ppkæø°domal"
# counter = Counter()
# counter.update(string)
# print(counter)
