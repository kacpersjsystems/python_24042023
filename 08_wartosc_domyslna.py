def calculate_salary(number_of_hours: int, hourly_rate: float, bonus: float = 0, bonus_percent: float = 0):
    return number_of_hours * hourly_rate + bonus + (number_of_hours * hourly_rate) * bonus_percent


                        # pozycyjne    nazwane
salary = calculate_salary(160, 20, bonus_percent=0.5, bonus=300)

# mogę też tak
salary = calculate_salary(number_of_hours=160, hourly_rate=20, bonus_percent=0.5, bonus=300)
print(salary)

# argument pozycyjny - musi występować na danej pozycji
# argument nazwany - występuje w dowolnej kolejności


