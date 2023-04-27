# scipy - matplotlib (wykres), numpy(obliczenia na macierzach)
# 16.1

import matplotlib.pyplot as plt

value = 1000
inflation = 16.1
number_of_years = 10

data=[value]
for year_number in range(1, number_of_years + 1):
    data.append(
        round(value * ((1 - inflation / 100) ** year_number), 2)
    )

plt.plot(
    range(number_of_years + 1),
    data
)
plt.xlabel('Lata')
plt.ylabel('Wartość nabywcza')
plt.title('Spadek wartości nabywczej pieniądza w przeciągu 10 lat')
plt.show()