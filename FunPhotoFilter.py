import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

current_image = None

def loading_image():
    global current_image
    file_path = file_dialog.askopenfilename()

    if file_path:
        current_image = Image.open(file_path)
        show_image(current_image)

# trying to show image in GUI window

def showcase_image(img):
    img = img.resize(400,400)

    img_Tk = ImageTk.PhotoImage(img)

    image_label.config(image=img_Tk)
    image_label.image = img_Tk 


    

