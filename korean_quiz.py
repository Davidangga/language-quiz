import os,sys
import random

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2",os.path.abspath("."))

    return os.path.join(base_path, relative_path)

def remove_space(str):
    if str != '\n':
        return str.removesuffix('\n')

def data_process(file_address):
    f = open(resource_path(file_address), "r")
    f1 = f.readlines()
    data = map(remove_space, f1)
    data = list(data)
    data = list(filter(None, data))
    return data

def generate_quiz():
    data = data_process("quiz.txt")
    random.shuffle(data)
    correct = 0
    wrong = 0
    over = False
    print("-------------------------------------------------")
    print("Welcome Petra")
    while not over:
        n = int(input("How many questions you want to answer today? "))
        if n <= len(data):
            for i in range(n):
                temp = data[i].split()
                ans = input(temp[1] + " = ")
                if ans == temp[0]:
                    correct += 1
                else:
                    wrong += 1
                    print(f'Wrong, the correct answer is ({temp[0]})\n')
            over = True
        else:
            print("Number exceeds the questions bank, Please add more questions first")

    print("Congrats you have completed today quiz\n")
    print(f"Here is your result:\n"
          f"Correct: {int(correct)}\n"
          f"Wrong: {int(wrong)}\n")
    print(print("-----------------------END--------------------------"))



generate_quiz()







