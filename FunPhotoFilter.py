import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

current_image = None

def load_image():
    global current_image
    file_path = file_dialog.askopenfilename()

    if file_path:
    

