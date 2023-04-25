# Przefiltruj słowa zaczynające się i kończące na tę samą literę
# słowa zaczynające się od a były .upper()
# słowa zaczynające się od innej litery były .lower()
#
# 1. Mapowanie    (zamiana na upper() lub lower())
# 2. Filtrowanie  (tylko słowa zaczynające i kończące się na tę samą literę
#

words = ['aNNa', 'baObAb', 'pralka']
result = []

for word in words:
    if word[0] == word[-1]:
        # 1. Wersja dłuższa
        # if word[0] == 'a' or word[0] == 'A':
        #     result.append(word.upper())
        # else:
        #     result.append(word.lower())

        # 2. Skrócony if
        result.append(
            word.upper() if word[0] == 'a' or word[0] == 'A' else word.lower()
        )

# print(result)
#    to co ma być w liście (to co jest w append)

result = [word.upper() if word[0] == 'a' or word[0] == 'A' else word.lower() for word in words if word[0] == word[-1]]
print(result)
