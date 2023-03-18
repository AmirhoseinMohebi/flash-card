from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
dic_data = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("data/french_words.csv")
    dic_data = org_data.to_dict(orient="records")
else:
    dic_data = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dic_data)
    canvas.itemconfig(card_titel, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_titel, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


def is_kn():
    dic_data.remove(current_card)
    Data = pandas.DataFrame(dic_data)
    Data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_titel = canvas.create_text(
    400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, font=("ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unkn_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unkn_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
kn_button = Button(image=check_image, highlightthickness=0, command=is_kn)
kn_button.grid(row=1, column=1)

next_card()

window.mainloop()
