from sympy import *
from tabulate import tabulate

#Exponent value
e = 2.71828182846
x = symbols('x', real=True)


def function(value):
    f = (4 * sin(x)) - (e**x)
    a = f.subs(x, value)
    return float(a)


def table(positive, negative):
    i = 0
    list = []

    while i < 15:
        a = []
        a.append(positive)
        a.append(negative)

        mid = (positive+negative)/2
        a.append(mid)

        fun = function(mid)
        a.append(fun)

        if fun > 0:
            positive = mid
        elif fun < 0:
            negative = mid
        else:
            list.append(a)
            return list

        list.append(a)
        i += 1
    return list


possitive = int(input("Enter the Possitive number: "))
negative = int(input("Enter the Negative number: "))

list = table(possitive, negative)
list = list[:-1]

headers = ["Possitive", "Negative", "Mid", "Function"]
print(tabulate(list, headers=headers, tablefmt="github", floatfmt=".10f"))
print("Github is connected")
