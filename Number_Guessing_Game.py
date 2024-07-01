import random
from tkinter import *
from tkinter import messagebox

def submit(choiceScale, bot, window):
    User_choice = int(choiceScale)
    if User_choice > bot:
        messagebox.showinfo(title='show info', message='TOO HIGH!')
    elif User_choice < bot:
        messagebox.showinfo(title='show info', message='TOO LOW!')
    else:
        messagebox.showinfo(title='show info', message='CORRECT!')
        if messagebox.askyesno(title='ask yes no', message='would you like to play again'):
            window.destroy()
            game()
        else:
            messagebox.showinfo(title='show info', message='THANKS FOR PLAYING!')
            window.destroy()

def game():
    Range = range(100)
    bot = random.choice(Range)
    window = Tk()
    window.geometry("420x420")
    choiceScale = Scale(window, resolution=1, length=300, bigincrement=1, from_=0, to=100, font=("Sans serif", 20, "bold"))
    choiceScale.pack()

    submitButton = Button(window, text='submit', command=lambda: submit(choiceScale.get(), bot, window) )
    submitButton.pack()
    window.mainloop()

def main():
    game()


if __name__ == '__main__':
    main()
