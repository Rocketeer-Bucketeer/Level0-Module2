import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring("lower class magic 8 ball", "ask any yes or no question")
    answer = random.randint(0,3)
    print(answer)
    if answer == 0:
        messagebox.showinfo("lower class magic 8 ball", "Yes")
    elif answer == 1:
        messagebox.showinfo("lower class magic 8 ball", "No")
    elif answer == 2:
        messagebox.showinfo("lower class magic 8 ball", "Maybe ask google")
    elif answer == 3:
        messagebox.showinfo("lower class magic 8 ball", "you must not know")

    # Make a variable and initialize it to a random number between 0 and 3

    # If the random number is 0

        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
