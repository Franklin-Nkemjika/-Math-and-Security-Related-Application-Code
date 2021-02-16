"""the following commands password ,percentage ,days ,cosine, volume ,exit"""
import math
import random
import string


def handle_percentage():
    """calculates the percentage"""
    stp = input("Calculating percentage \nuse comma to denote end \n what are your values ? : \n")

    print(stp)

    if len(stp.split(",")) < 3:
        stp = input("please make sure you use three values numerator,denominator,decimal_places")
    else:
        numerator = stp.split(',')[0]
        denominator = stp.split(',')[1]
        num_format = stp.split(",")[2]

        val = str(int(numerator) / int(denominator))

        try:
            decimal = val.split(".")[1]
            print("The percentage is :" + str(float(val.split(".")[0] + "." + decimal[:int(num_format)]) * 100) + "%")
        except IndexError:
            print("the percentage is : " + str(int(val) * 100) + "%")
            main()


def generate_password():
    """creating password"""
    length = input("How long do you want your password ?\n")

    type = input("Do you want uppercase alphabets ? Yes(y) or No(n) \n")

    if type in 'Y' or type in 'Yes' or type in 'y':
        password = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits)
            for _ in range(int(length)))
    elif type in 'n' or type in "N" or type in "No":
        password = ''.join(
            random.SystemRandom().choice(string.ascii_lowercase + string.digits)
            for _ in range(int(length)))

        print("Here is your formidable password :" + password)
    main()


def time_difference():
    """calculates the time difference"""
    from datetime import date

    today = date.today()
    d1 = date(2025, 7, 4)
    delta = d1 - today
    print("The days are ")
    print(delta.days)
    main()


def value_of_c():
    """C value"""
    a = input("What is the value of side a : ")
    b = input("What is the value of side b : ")

    angle = input("what is the sie of the angle between a & b : ")
    square_c = math.pow(int(a), 2) + math.pow(int(b), 2) - (2 * int(a) * int(b) * math.cos(int(angle)))

    c = math.sqrt(square_c)

    print("The value of c =" + str(c))
    main()


def calc_volume():
    """volume"""
    radius = input("What is the radius : ")

    height = input("what is the height of the cylinder : ")

    volume = (math.pow(int(radius), 2)) * int(height)

    print("The volume of right cylinder : " + str(volume))
    main()


def main():
    """
    the main function for the program making
    decisions based on the user input and interactions
    """
    action = input("What do you wish to do \n percent ,password,time,cosine,volume,exit ?")

    if action in "percentage" or action in "percent":
        handle_percentage()
    elif action == 'password':
        generate_password()
    elif action in 'time' or action in 'days':
        time_difference()
    elif action in 'angle' or action in 'cosine' or action in 'cos':
        value_of_c()
    elif action == 'volume':
        calc_volume()
    elif action == 'exit':
        print("__Thank you for visiting the application__")
    else:
        print("Please enter a valid commands")
        main()


main()
