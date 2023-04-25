# bmi = masa / (wzrost * wzrost)
#      weight   height
# Napisz program który odbierze od użytkownika jego masę w
# kilogramach i wzrost w metrach, wyliczy i wypisze BMI.

# We are all adults (Wszyscy jesteśmy dorośli)

weight = float(input('Ile ważysz? (kg) '))
height = float(input('Ile masz wzrostu? (m) '))
bmi = weight / height ** 2

print(bmi)