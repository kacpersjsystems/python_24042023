# Plik ten sam co bez litery b, natomiast nie zawierający komentrzy (wersja ostateczna)

def calculate_bmi(weight: float, height: float):
    """This function calculates bmi

    :param weight: person weight in kg
    :param height: person height in meters
    :return:
    """
    if height > 4:
        height /= 100

    return weight / height ** 2


def convert_bmi_to_text(bmi: float) -> str:
    if bmi < 17:
        return 'wychudzenie'

    if bmi < 18.5:
        return 'niedowaga'

    if bmi < 25:
        return 'wszystko ok'

    if bmi < 30:
        return 'nadwaga'

    return 'otyłość'


with open('17_csv_plik.txt', encoding='utf8') as file:
    data = [[int(element) if element.isnumeric() else element for element in line.strip().split(',')] for line in file]

for row in data:
    first_name, last_name, height, weight = row
    bmi = calculate_bmi(weight, height)
    print(first_name, last_name, weight, height, bmi, convert_bmi_to_text(bmi))
