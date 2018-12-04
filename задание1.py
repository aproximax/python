import sys

input("Введите число:", )

try:
    digits = sys.arg[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: задание1.py <numer>")
except ValueError:
    print(err, "in", digits)