import random
import sys
from tkinter import messagebox, Tk
from playsound import playsound


def crack_the_safe():
    pass
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations
    for i in range (999999999999):
        try_code(i)

dsfkls = random.randint(0, 237)
jkhdsfjkhejihdsfh = random.randint(0 , dsfkls)
sdfjkeiusfiu = random.randint(0, dsfkls * jkhdsfjkhejihdsfh)

# ======================= DO NOT EDIT THE CODE BELOW =========================

wekncrzpasfdkjhcfjse = random.randint(0, sdfjkeiusfiu)
print(wekncrzpasfdkjhcfjse)
print(9999999 - wekncrzpasfdkjhcfjse)
def try_code(guess):
    print("trying " + str(guess))

    secret_code = 9999999 - wekncrzpasfdkjhcfjse


    if guess == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        play_the_sound_of_success()
        sys.exit(0)


def play_the_sound_of_success():
    playsound('me-gusta.wav')


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    crack_the_safe()
