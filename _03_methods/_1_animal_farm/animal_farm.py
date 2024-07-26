import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound

window = None


def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.

    playing = 0

    while playing == 0:
        animal = simpledialog.askstring("Animal dude", "which animal would you like to see? Choices are dog, cow, cat, duck, and llama.")
        if animal == 'cat':
            show_image(filename='cat.jpg')
            meow()
        if animal == 'dog':
            show_image(filename='dog.jpg')
            woof()
        if animal == 'cow':
            show_image(filename='cow.jpg')
            moo()
        if animal == 'duck':
            show_image(filename='duck.jpg')
            quack()
        if animal == 'llama':
            show_image(filename='llama.jpg')
            llama_scream()
        useless_number = simpledialog.askstring("Animal Dude", "Would you like to exit?")
        if useless_number == 'yes':
            playing = 1







    # TODO 2. Make it so that the user can keep entering new animals.

    # TODO 3. If the user enters 'exit', stop the program


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()


def moo():
    show_image('cow.jpg')
    playsound('moo.wav')


def quack():
    show_image('duck.jpg')
    playsound('quack.wav')


def woof():
    show_image('dog.jpg')
    playsound('woof.wav')


def meow():
    show_image('cat.jpg')
    playsound('meow.wav')


def llama_scream():
    show_image('llama.jpg')
    playsound('llama.wav')


if __name__ == '__main__':
    animals()
