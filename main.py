import string
from collections import Counter

def analyseText(textToBeAnalysed):
    alpha = list(string.ascii_lowercase)
    alpha.insert(14, "ñ")
    alpha.insert(3, "ç")
    alphaIncidence = []
    alphaPercentages = []
    digits = list(string.digits)
    digitsIncidence = []
    digitsPercentages = []
    punctuation = list(string.punctuation)
    punctuationIncidence = []
    punctuationPercentages = []

    textToBeAnalysedWithoutSpaces = textToBeAnalysed.replace(" ", "")
    lengthOfTextToBeAnalysedWithoutSpaces = len(textToBeAnalysedWithoutSpaces)
    textToBeAnalysedWithoutSpacesAndAllLowerCase = textToBeAnalysedWithoutSpaces.lower()


    alphaCounter = Counter()
    for line in textToBeAnalysedWithoutSpacesAndAllLowerCase:
        for each in alpha:
            if each in line:
               alphaCounter.update(line)
            elif each not in line and each not in alphaCounter.keys():
                alphaCounter[each] = 0
    for each in alphaCounter.values():
        alphaIncidence.append(each)
    for each in alphaIncidence:
        alphaPercentages.append(round(each / lengthOfTextToBeAnalysedWithoutSpaces * 100, 4))
    alphaDictionary = dict(zip(alpha, alphaPercentages))


    digitsCounter = Counter()
    for line in textToBeAnalysedWithoutSpacesAndAllLowerCase:
        for each in digits:
            if each in line:
               digitsCounter.update(line)
            elif each not in line and each not in digitsCounter.keys():
                digitsCounter[each] = 0
    for each in digitsCounter.values():
        digitsIncidence.append(each)
    for each in digitsIncidence:
        digitsPercentages.append(round(each / lengthOfTextToBeAnalysedWithoutSpaces * 100, 4))
    digitsDictionary = dict(zip(digits, digitsPercentages))
    

    punctuationCounter = Counter()
    for line in textToBeAnalysedWithoutSpacesAndAllLowerCase:
        for each in punctuation:
            if each in line:
                punctuationCounter.update(line)
            elif each not in line and each not in punctuationCounter.keys():
                punctuationCounter[each] = 0
    for each in punctuationCounter.values():
        punctuationIncidence.append(each)
    for each in punctuationIncidence:
        punctuationPercentages.append(round(each / lengthOfTextToBeAnalysedWithoutSpaces * 100, 4))
    punctuationDictionary = dict(zip(punctuation, punctuationPercentages))

    everythingDictionary = alphaDictionary.copy()
    everythingDictionary.update(digitsDictionary)
    everythingDictionary.update(punctuationDictionary)
    sortedEverythingDictionary = sorted(everythingDictionary.items(), key=lambda x: x[1], reverse=True)

    return everythingDictionary, sortedEverythingDictionary

# Nomes dos arquivos nos quais os textos se encontram, em plain text
arquivos = ['books\engDracula.txt', 'books\engFrankenstein.txt', 'books\esEsElCamino.txt', 'books\esPeTupacAmaru.txt', 'books\ptBrDomCasmurro.txt', 'books\ptPtOsLusiadas.txt', 'books\catElsCaminsDelParadisPerdut.txt', 'books\catEnPereIAltresContes.txt']

textos = []

# Armazena cada um dos textos no vetor textos
for each in arquivos:
    f = open(each, encoding="utf8")
    textos.append(f.read())
    f.close()

dicionarios = []
dicionariosOrganizados = []

# Aplica a função analyseText a todos os textos armazenados e armazena os resultados no vetor dicionarios
for each in textos:
    dicionarios.append(analyseText(each)[0])
    # dicionariosOrganizados.append(analyseText(each)[1])

dicionarioGeral = dicionarios[0].copy()

# Soma todos os dicionários no vetor dicionarios e os adiciona num único dicionário chamado dicionarioGeral
for index in range(len(dicionarios)):
    if index != 0:
        # Por usar counter, descarta todos os caracteres que tem porcentagem(contagem) igual a 0
        dicionarioGeral = Counter(dicionarioGeral) + Counter(dicionarios[index])

# Divide a soma de todos os dicionários pelo número total de dicionários, efetivamente, calculando a média deles
dicionarioGeral = {k: round(v / len(dicionarios), 4) for k, v in dicionarioGeral.items()}

# Organiza o dicionarioGeral em ordem decrescente
dicionarioGeralOrganizado = sorted(dicionarioGeral.items(), key=lambda x: x[1], reverse=True)
print(dicionarioGeralOrganizado)