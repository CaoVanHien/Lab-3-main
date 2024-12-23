import tkinter as tk
import pygame
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import string
def letter_to_number(letter):
    return string.ascii_uppercase.index(letter.upper()) + 1

def generate_key():
    letter1 = entry_letter1.get()
    letter3 = entry_letter3.get()
    if len(letter1) != 1 or letter1.upper() not in string.ascii_uppercase:
        messagebox.showerror("Error", "Введіть правильну букву для 1 (A-Z).")
        return
    if len(letter3) != 1 or letter3.upper() not in string.ascii_uppercase :
        messagebox.showerror("Error", "Введіть правильну букву для 3 (A-Z). ")
        return
    num1 = letter_to_number(letter1) 
    num3 = letter_to_number(letter3)   
    start_num = min(num1,num3)
    end_num = max(num1,num3)
    random_letters = random.choices(string.ascii_uppercase[start_num-1:end_num], k=7)
    block2 = ''.join(random_letters)
    generate_key = f"{num1:02d} - {block2} - {num3:02d}"
    result_label.config(text=f"Сгенерированный ключ: {generate_key}")

root = tk.Tk()
root.title("Keygen")
root.geometry("800x1000")
background_image = Image.open("C:/Anh/luffy.JPG")
background_image = background_image.resize((800,1000), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
instruction_label = tk.Label(root, text= "Введите две буквы (1 and 3): ", bg="White", font= ("Arial", 12))
instruction_label.pack(pady=10)

entry_letter1 = tk.Entry(root, font = ("Arial",12), width = 2 )
entry_letter1.pack(pady=5)

entry_letter3 = tk.Entry(root,font=("Arial",12), width = 2)
entry_letter3.pack(pady = 5)

generate_button = tk.Button(root, text="Генерировать ключ", command= generate_key, font=("Arial", 12), bg="Red", fg="white")
generate_button.pack(pady= 10)

result_label = tk.Label(root, text="", bg="white", font=("Arial",12))
result_label.pack(pady=10)

pygame.mixer.init()
pygame.mixer.music.load("C:/Nhac/LamSaoAnhCoTheXoa.mp3")
pygame.mixer.music.play(-1)

root.mainloop()