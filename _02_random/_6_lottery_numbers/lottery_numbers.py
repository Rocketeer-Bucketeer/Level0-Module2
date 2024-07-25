import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket

    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    number3 = random.randint(1, 9)
    number4 = random.randint(1, 9)
    number5 = random.randint(1, 9)
    number6 = random.randint(1, 9)
    supernumner = random.randint(1, number6 + number5 + number4 + number3 + number2 + number1)
    da_answer = number1.__str__() + number2.__str__() + number3.__str__() + number4.__str__() + number5.__str__() + number6.__str__()
    print(da_answer)
    print(supernumner)

    messagebox.showinfo("ticket", number1.__str__() + number2.__str__() + number3.__str__() + number4.__str__() + number5.__str__() + number6.__str__())

    number1a = random.randint(1, 9)
    number2a = random.randint(1, 9)
    number3a = random.randint(1, 9)
    number4a = random.randint(1, 9)
    number5a = random.randint(1, 9)
    number6a = random.randint(1, 9)
    supernumnera = random.randint(1, number6 + number5 + number4 + number3 + number2 + number1)
    da_realanswer = number1a.__str__() + number2a.__str__() + number3a.__str__() + number4a.__str__() + number5a.__str__() + number6a.__str__()
    print(da_realanswer)
    print(supernumnera)
    if da_answer == da_realanswer:
        messagebox.showinfo("OMG YOU WON THE LOTTERY", "YOU WON THE LOTTERY TOO BAD IT WASN'T IN REAL LIFE... BUT STILL YOU GET A FREE NOTHING!!! CONGRATS!!!")
    if supernumnera == supernumner:
        messagebox.showinfo("NICE YOU GOT THE SUPA NUMBER", "YOU WIN THE SUPERNUMBER AND ERM YEAH YOU GET HALF A FREE NOTHING")
    if number6 == number6a:
        messagebox.showinfo("thats fine ig", "nice your number 6 matches you get 0.1 a free nothing")
    if number4 == number4a:
         messagebox.showinfo("thats fine ig", "nice your number 4 matches you get 0.1 a free nothing")
    if number5 == number5a:
         messagebox.showinfo("thats fine ig", "nice your number 5 matches you get 0.1 a free nothing")
    if number2 == number2a:
         messagebox.showinfo("thats fine ig", "nice your number 2 matches you get 0.1 a free nothing")
    if number3 == number3a:
         messagebox.showinfo("thats fine ig", "nice your number 3 matches you get 0.1 a free nothing")
    if number1 == number1a:
         messagebox.showinfo("thats fine ig", "nice your number 1 matches you get 0.1 a free nothing")








    # TODO 2) Display the selected numbers to the user in a pop-up

    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket

    # TODO 4) ULTRABONUS: Make the lottery system so that if the numbers match it says you won the "lottery"
