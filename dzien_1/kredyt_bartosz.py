loan = int(input('Podaj kwote kredytu'))
percent_per_year = float(input('Podaj oprocentowanie roczne'))
x = int(input('Podaj wysokosc splacanej raty'))
month_number = 1

while loan > 0:
    # wartosc odsetek
    loan_installment = loan * percent_per_year / 12

    # calkowita wartosc do splaty wraz z odsetkami
    loan += loan_installment
    # if loan < loan_installment
    # loan_installment = loan

    loan -= x
    print(f'Miesiac {month_number}, wartosc odsetek{round(loan_installment, 2)}, pozostalo do splaty {loan}')
    month_number += 1