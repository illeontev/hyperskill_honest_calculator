def check_is_number(number):
    try:
        float(number)
        return True
    except:
        return False

def is_one_digit(number):
    return -10 < number < 10 and round(number) == number

def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += " ... lazy"
    if (x == 1 or y == 2) and oper == "*":
        msg += " ... very lazy"
    if (x == 0 or y == 0) and oper in ("*", "+", "-"):
        msg += " ... very, very lazy"

    if msg != "":
        msg = "You are" + msg
        print(msg)

memory = 0
while True:
    print("Enter an equation")
    string = input()
    words = string.split()
    a_string, oper, b_string = words

    if a_string == "M":
        a_string = str(memory)
    if b_string == "M":
        b_string = str(memory)

    if not (check_is_number(a_string) and check_is_number(b_string)):
        print("Do you even know what numbers are? Stay focused!")
    else:
        if oper not in ["+", "-", "*", "/"]:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        else:
            a, b = float(a_string), float(b_string)

            check(a, b, oper)

            if oper == "+":
                result = a + b
            elif oper == "-":
                result = a - b
            elif oper == "*":
                result = a * b
            elif oper == "/" and b != 0:
                result = a / b
            else:
                print("Yeah... division by zero. Smart move...")
                continue
            print(result)

            message_list = ["Are you sure? It is only one digit! (y / n)",
                           "Don't be silly! It's just one number! Add to the memory? (y / n)",
                           "Last chance! Do you really want to embarrass yourself? (y / n)"]
            message_index = 0
            while True:
                print("Do you want to store the result? (y / n):")
                answer = input()
                remember_result = True
                if answer == "y":
                    while is_one_digit(result) and message_index <= 2:
                        print(message_list[message_index])
                        answer2 = input()
                        if answer2 == "y":
                            message_index += 1
                        elif answer2 == "n":
                            remember_result = False
                            break
                    if remember_result:
                        memory = result
                    break
                elif answer == "n":
                    break

            print("Do you want to continue calculations? (y / n):")
            answer = input()
            if answer == "n":
                break






