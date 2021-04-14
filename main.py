from PIL import Image
import tkinter as tk
from tkinter import filedialog
import numpy as np

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300, bg='slateblue', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Images to PDF', bg='slateblue')
label1.config(font=('helvetica', 30))
canvas1.create_window(150, 60, window=label1)

#browseButton = tk.Button(text="Select File", command=getFiles, bg='green', fg='white',
#                         font=('helvetica', 12, 'bold'))
#canvas1.create_window(150, 130, window=browseButton)


def convertToPdf():
    imageList = []
    global im1
    global image1

    import_file_path = filedialog.askopenfilenames()
    for i in range(len(import_file_path)):
        if i == 0:
            im1 = Image.open(import_file_path[i])
            im1 = im1.convert('RGB')
            continue
        image1 = Image.open(import_file_path[i])
        imageList.append(image1.convert('RGB'))
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    im1.save(export_file_path, save_all = True, append_images = imageList)
    #im1.save(export_file_path)

saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, bg='green', fg='white',
                         font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=saveAsButton)

canvas1.create_window(150, 230)

root.mainloop()
