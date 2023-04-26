# Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
# Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.

# 0. Nad pętlą zdefiniuj pustą listę values = []
# 1. Napisz pętle która wyświetli 10 kolejnych potęg liczby 2
# 2. Zamiast wyświetlać te liczby dodawaj je do listy za pomocą funkcji append()
# 3. Pod spodem za pomocą pętli for przejdź po elementach listy i wyświetl ich wartości

# Czysty Kod - Uncle Bob - Robert C. Martin
# staram się by ta zmienna była liczbą mnogą

values = []
for p in range(1, 11):
    # pow(2, p)
    values.append(2 ** p)

for value in values:
    print(value)