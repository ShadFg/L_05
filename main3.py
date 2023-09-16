def check(num1, num2, action):
    if action == "plus":
        print(num1 + num2)
    elif action == "minus":
        print(num1 - num2)
    elif action == "multiply":
        print(num1 * num2)
    elif action == "divide":
        print(num1 / num2)
    else:
        raise SyntaxError(f"action {action} is incorrect, action must be = plus, minus, multiply or divide")

while True:
    try:
        num1 = float(input("enter first num - "))
        num2 = float(input("enter first num - "))
        break
    except:
        print("input error inputs must be numbers")

while True:
    try:
        action = input("enter action: plus / minus / multiply / divide - ")
        check(num1, num2, action)
        break
    except (SyntaxError) as error:
        print("input error", error)
    except:
        print("input error")