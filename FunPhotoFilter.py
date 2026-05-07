import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

current_image = None

def loading_image():
    global current_image
    file_path = filedialog.askopenfilename()

    if file_path:
        current_image = Image.open(file_path)
        show_image(current_image)

# trying to show image in GUI window

def show_image(img):
    img = img.resize((800,800))

    img_tk = ImageTk.PhotoImage(img)

    image_label.config(image=img_tk)
    image_label.image = img_tk 

# what window will show
window = tk.Tk()
window.title("Fun Photo Filters")

image_label = tk.Label(window)
image_label.pack()

tk.Button(window, text= "Load Image", command= loading_image).pack()

window.mainloop()
