repeat = " "
while repeat !="n" and repeat !="N":
    print ("Calculator")
    print("")

    input_value = input("What do you want to calculate: ")
    print(" ")
    operator = ""
    numbers_to_calculate = ""

    if "+" in input_value:
        numbers_to_calculate = input_value.split("+")

        operator = "+"

    elif "-" in input_value:
        numbers_to_calculate = input_value.split("-")

        operator = "-"

    elif "*" in input_value:
        numbers_to_calculate = input_value.split("*")

        operator = "*"

    elif "/" in input_value:
        numbers_to_calculate = input_value.split("/")

        operator = "/"

    number_1 = numbers_to_calculate[0]
    number_2 = numbers_to_calculate[1]

    number_1.strip()
    number_2.strip()
    if operator == "+":
        print(float(number_1) + float(number_2))
    elif operator == "-":
        print(float(number_1) - float(number_2))
    elif operator == "*":
        print(float(number_1) * float(number_2))
    elif operator == "/":
        print(float(number_1) / float(number_2))

    print("")
    repeat = input("repeat(Y/n):")



