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
    img = img.resize((600,600))

    img_tk = ImageTk.PhotoImage(img)

    image_label.config(image=img_tk)
    image_label.image = img_tk 

# FILTER TIME
def noir():
    global current_image

    if current_image:
        current_image = ImageOps.grayscale(current_image).convert("RGB")
        show_image(current_image)

def saturated():
    global current_image

    if current_image:
        current_image = current_image.convert("RGB")

        r, g, b = current_image.split()

        r = r.point(lambda i: min(255, int(i * 5.2)))
        g = g.point(lambda i: min(255, int(i * 5.2)))
        b = b.point(lambda i: min(255, int(i * 5.2)))

        current_image = Image.merge("RGB", (r, g ,b))
        show_image = current_image

# what window will show
window = tk.Tk()
window.title("Fun Photo Filters")

image_label = tk.Label(window)
image_label.pack()

tk.Button(window, text= "Load Image", command= loading_image).pack()

tk.Button(window, text= "Noir Filter", command= noir).pack()
tk.Button(window, text= "Saturated Filter", command= saturated).pack()

window.mainloop()
