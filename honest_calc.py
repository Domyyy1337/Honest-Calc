msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = 0


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "i"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

def is_one_digit(v):
    if -10 < float(v) < 10 and (float(v) - round(float(v)) == 0):
        return True
    else:
        return False

while True:
    try:
        calc = input("Enter an equation").split()
        if calc[0] == "M" and calc[2] != "M":
            x, operator, y = float(memory), calc[1], float(calc[2])
            check(x, y, operator)
            my_equations = {"+": x + y, "-": x - y, "*": x * y}
            if operator != "/":
                result = my_equations.pop(operator)
            elif operator == "/":
                result = x / y
            print(result)
        elif calc[2] == "M" and calc[0] != "M":
            x, operator, y = float(calc[0]), calc[1], float(memory)
            check(x, y, operator)
            my_equations = {"+": x + y, "-": x - y, "*": x * y}
            if operator != "/":
                result = my_equations.pop(operator)
            elif operator == "/":
                result = x / y
            print(result)
        elif calc[0] == "M" and calc[2] == "M":
            x, operator, y = float(memory), calc[1], float(memory)
            my_equations = {"+": x + y, "-": x - y, "*": x * y}
            check(x, y, operator)
            if operator != "/":
                result = my_equations.pop(operator)
            elif operator == "/":
                result = x / y
            print(result)
        else:
            x, operator, y = float(calc[0]), calc[1], float(calc[2])
            my_equations = {"+": x + y, "-": x - y, "*": x * y}
            check(x, y, operator)
            if operator != "/":
                result = my_equations.pop(operator)
            elif operator == "/":
                result = x / y
            print(result)
        print("Do you want to store the result? (y / n):")
        answer = str(input())
        possible_answer = ["y", "n"]
        while answer not in possible_answer:
            print("Do you want to store the result? (y / n):")
            answer = str(input())
        if answer == possible_answer[0]:
            if is_one_digit(result):
                msg_index_value = 0
                msg_index = [msg_10, msg_11, msg_12]
                while msg_index_value <= 2:
                    print(msg_index[msg_index_value])
                    answer_msg = str(input())
                    while answer_msg not in possible_answer:
                        print(msg_index[msg_index_value])
                        answer_msg = str(input())
                    if answer_msg == possible_answer[0]:
                        msg_index_value += 1
                    else:
                        msg_index_value = 0
                        break
                if answer_msg == possible_answer[0]:
                    memory = result
                    msg_index_value = 0
            else:
                memory = result
        print("Do you want to continue calculations? (y / n):")
        continue_answer = str(input())
        while continue_answer not in possible_answer:
            print("Do you want to continue calculations? (y / n):")
            continue_answer = str(input())
        if continue_answer == possible_answer[0]:
            continue
        elif continue_answer == possible_answer[1]:
            break
        break
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    except KeyError:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")