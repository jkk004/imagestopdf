import tkinter as tk
from youtube_dl import YoutubeDL



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

def youtubeToAudio():
    pathlabel = filedialog.askdirectory()
    os.chdir(pathlabel)
    song = YoutubeDL({'format': 'bestaudio'})
    URL = entry1.get()
    try:
        song.extract_info(URL)
    except Exception:
        print("Try Again")




root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=400, bg='yellow')
canvas1.pack()

label2 = tk.Label(root, text = "USEFUL THINGS", bg = 'yellow', fg = 'black')
label2.config(font=('helvetica', 30))
canvas1.create_window(200, 50, window = label2)
saveButton = tk.Button(text='Click On Me To Convert Image(s) to PDF', command=imagesToPDF, bg='black', fg='yellow', font = 30)
canvas1.create_window(200, 130, window=saveButton)

entry1 = tk.Entry (root)
canvas1.create_window(200, 230, window = entry1, width = 330)
button1 = tk.Button(text='Click On Me To Convert Youtube Link To MP3', command=youtubeToAudio, bg='black', fg='yellow', font = 30)
canvas1.create_window(200, 260, window=button1)
label1 = tk.Label(root, text = "Paste Link Below", font = 30, bg = 'yellow', fg = 'blue')
canvas1.create_window(100, 205, window = label1)


root.mainloop()
