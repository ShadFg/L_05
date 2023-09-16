# try:
#     num = input("enter int - ")
#     print(int(num) * 2)
# except:
#     print("incorrect input info")

# while True:
#     try:
#         num = input("\nenter int - ")
#         print(100 / float(num))
#         break
#     except ValueError:
#         print("error input must be int value")
#     except ZeroDivisionError:
#         print("error input must be != 0")

# while True:
#     try:
#         num = input("\nenter int - ")
#         print(100 / float(num))
#         break
#     except (ValueError, ZeroDivisionError) as error:
#         print("incorrect input", error)
#     finally:
#         print("finished")

def checker(var1):
    if type(var1) != str:
        raise TypeError(f"input type is {type(var1)}, input must be str type")
    else:
        return var1

try:
    print(checker(1))
except(TypeError) as error:
    print("input error,", error)
except:
    print("input error")

try:
    print(checker("1"))
except(TypeError) as error:
    print("input error,", error)
except:
    print("input error")