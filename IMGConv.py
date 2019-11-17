import sys
import tkinter as tk
from PIL import Image
from tkinter import filedialog

h2 = 0

# file dialog to choose image
def open_dialog():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

# Manipulate image data
def img_manip(img, w2):
    # Store width and height values
    w, h = img.size
    aRatio = h / w

    h2 = int(aRatio * w2 * 0.55)
    img = img.resize((w2, h2))
    # Convert image to grey-scale
    img = img.convert('L')
    return img.getdata()

# Convert Pixel data to char
def main():
    asciiChar = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

    # Open received path from file dialog
    img = Image.open(open_dialog())
    # Choose character width and height for ASCII
    width = 200
    pixelData = img_manip(img, width)
    newPixelData = ''.join([asciiChar[pixel//25] for pixel in pixelData])
    imgASCII = "\n".join([newPixelData[index:index + width] for index in range(0, len(newPixelData), width)])
    print(imgASCII)

if __name__ == "__main__":
    main()
