# 2 Програма повинна вивести трикутник як на малюнку. Програма отримує число - скільки вивести рядків.
# Кожен рядок має номер та число вирівняне по правому краю з кількистю нулів відповіно до номера рядку.

amount_lines = int(input("Введи кількість рядків ->"))
for i in range(0, amount_lines):
    if i < 10:
        print("{}".format(i) + "{}".format(10 ** i).rjust(amount_lines + 2))
    else:
        print("{}".format(i) + "{}".format(10 ** i).rjust(amount_lines + 1))