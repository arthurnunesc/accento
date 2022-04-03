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


    ### IMPLEMENTAÇÃO ANTIGA ###
    # for each in alpha:
    #     alphaIncidence.append(textToBeAnalysedWithoutSpacesAndAllLowerCase.count(each))
    # for each in alphaIncidence:
    #     alphaPercentages.append(round(each / lengthOfTextToBeAnalysedWithoutSpaces * 100, 4))
    # alphaDictionary = dict(zip(alpha, alphaPercentages))

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

    ### IMPLEMENTAÇÃO ANTIGA ###
    # for each in digits:
    #     digitsIncidence.append(textToBeAnalysedWithoutSpacesAndAllLowerCase.count(each))
    # for each in digitsIncidence:
    #     digitsPercentages.append(round(each / lengthOfTextToBeAnalysedWithoutSpaces * 100, 4))
    # digitsDictionary = dict(zip(digits, digitsPercentages))


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
    # print(sortedEverythingDictionary)

arquivos = ['books\engDracula.txt', 'books\engFrankenstein.txt', 'books\esEsElCamino.txt', 'books\esPeTupacAmaru.txt', 'books\ptBrDomCasmurro.txt', 'books\ptPtOsLusiadas.txt', 'books\catElsCaminsDelParadisPerdut.txt', 'books\catEnPereIAltresContes.txt']

textos = []

for each in arquivos:
    f = open(each, encoding="utf8")
    textos.append(f.read())
    f.close()

dicionarios = []
dicionariosOrganizados = []

for each in textos:
    dicionarios.append(analyseText(each)[0])
    dicionariosOrganizados.append(analyseText(each)[1])

print(dicionarios)
print(dicionariosOrganizados)

# f = open('books\engDracula.txt', encoding="utf8")
# dracula = f.read()
# f.close()
# draculaDictionary, draculaDictionarySorted = analyseText(dracula)

# f = open('books\engFrankenstein.txt', encoding="utf8")
# frankenstein = f.read()
# f.close()
# frankensteinDictionary, frankensteinDictionarySorted = analyseText(frankenstein)

# f = open('books\esEsElCamino.txt', encoding="utf8")
# elCamino = f.read()
# f.close()
# elCaminoDictionary, elCaminoDictionarySorted = analyseText(elCamino)

# f = open('books\esPeTupacAmaru.txt', encoding="utf8")
# tupacAmaru = f.read()
# f.close()
# tupacAmaruDictionary, tupacAmaruDictionarySorted = analyseText(tupacAmaru)

# f = open('books\ptBrDomCasmurro.txt', encoding="utf8")
# domCasmurro = f.read()
# f.close()
# domCasmurroDictionary, domCasmurroDictionarySorted = analyseText(domCasmurro)

# f = open('books\ptPtOsLusiadas.txt', encoding="utf8")
# osLusiadas = f.read()
# f.close()
# osLusiadasDictionary, osLusiadasDictionarySorted = analyseText(osLusiadas)

# f = open('books\catElsCaminsDelParadisPerdut.txt', encoding="utf8")
# elsCaminsDelParadisPerdut = f.read()
# f.close()
# elsCaminsDelParadisPerdutDictionary, elsCaminsDelParadisPerdutDictionarySorted = analyseText(elsCaminsDelParadisPerdut)

# f = open('books\catEnPereIAltresContes.txt', encoding="utf8")
# enPereIAltresContes = f.read()
# f.close()
# enPereIAltresContesDictionary, enPereIAltresContesDictionarySorted = analyseText(enPereIAltresContes)