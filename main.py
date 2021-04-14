from PIL import Image
import tkinter as tk
from tkinter import filedialog

def imagesToPDF():
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
root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300, bg='white')
canvas1.pack()

saveButton = tk.Button(text='Click On Me To Convert Images to PDF', command=imagesToPDF, bg='black', fg='yellow', font = 30)
canvas1.create_window(150, 130, window=saveButton)

canvas1.create_window(150, 230)

root.mainloop()
