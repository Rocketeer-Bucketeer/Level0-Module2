import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    number3 = random.randint(1, 9)
    supernumner = random.randint(1, number3 + number2 + number1)
    da_answer = number1.__str__() + number2.__str__() + number3.__str__()
    print(da_answer)
    print(supernumner)

    messagebox.showinfo("ticket", number1.__str__() + number2.__str__() + number3.__str__())

    number1a = random.randint(1, 9)
    number2a = random.randint(1, 9)
    number3a = random.randint(1, 9)
    supernumnera = random.randint(1, number3 + number2 + number1)
    da_realanswer = number1a.__str__() + number2a.__str__() + number3a.__str__()
    print(da_realanswer)
    print(supernumnera)
    if da_answer == da_realanswer:
        messagebox.showinfo("OMG YOU WON THE LOTTERY", "YOU WON THE LOTTERY TOO BAD IT WASN'T IN REAL LIFE... BUT STILL YOU GET A FREE NOTHING!!! CONGRATS!!!")
    if supernumnera == supernumner:
        messagebox.showinfo("NICE YOU GOT THE SUPA NUMBER", "YOU WIN THE SUPERNUMBER AND ERM YEAH YOU GET HALF A FREE NOTHING")
    if number2 == number2a:
         messagebox.showinfo("thats fine ig", "nice your number 2 matches you get 0.1 a free nothing")
    if number3 == number3a:
         messagebox.showinfo("thats fine ig", "nice your number 3 matches you get 0.1 a free nothing")
    if number1 == number1a:
         messagebox.showinfo("thats fine ig", "nice your number 1 matches you get 0.1 a free nothing")





