# Napisz program który wyświetli w konsoli niepuste linie z pliku tekstowego którego nazwę
# poda użytkownik. (Usuwamy puste linie)

with open('22_ex_puste_linie.txt', 'r', encoding='utf8') as file, \
        open('output_file.txt', 'w', encoding='utf8') as output:
    for line in file:
        if len(line.strip()) > 0:
            print(line.strip())
            output.write(line)
