import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    for i in range (10):
        window = Tk()
        window.withdraw()

        random_number = random.randint(1, 5)

        print(random_number)

        if random_number == 1:
            messagebox.showinfo("complementer", "you nice")
        elif random_number == 2:
            messagebox.showinfo("complementer", "you good")
        elif random_number == 3:
            messagebox.showinfo("complementer", "you look nice today")
        elif random_number == 4:
            messagebox.showinfo("complementer", "you kind")
        elif random_number == 5:
            messagebox.showinfo("complementer", "your great at whatever you enjoy doing!")
        elif random_number == 6:
            messagebox.showinfo("complementer", "i like your shoes")
        elif random_number == 7:
            messagebox.showinfo("complementer", "i like your shirt")
        elif random_number == 8:
            messagebox.showinfo("complementer", "your outfit looks fire today")
        elif random_number == 9:
            messagebox.showinfo("complementer", "you nice")
        elif random_number == 10:
            messagebox.showinfo("complementer", "AAAH I CANT THINK OF ANY MORE COMPLIMENTS")

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
