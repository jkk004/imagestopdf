from PIL import Image
import tkinter as tk
from tkinter import filedialog
from youtube_dl import YoutubeDL
import os
import requests
from random import randrange
import re
from time import strftime
import webbrowser

def song_recommender():
    choices = ["Billy Joel", "Elton John", "Jim Croce", "Nujabes", "Eagles", "Radiohead", "Eminem", "Eagles", "Nobou Uematsu", "Stevie Wonder", "Eric Clapton", "The Beatles", "Joe Hisaishi", "Mac Demarco", "Pablo Cikaso", "Yoko Shimomura", "Queen", "Santana",
               "Nirvana", "Bob Marley", "John Denver", "Rammstein", "XXXTentacion", "Outkast", "Sting", "Simon & Garfunkel", "Frank Sinatra", "Bee Gees", "Usher", "The Police", "Cypress Hill", "DMX", "Hans Zimmer", "Elvis Presley", "ABBA", "Chicago", "The Beach Boys"
               ,"The Doors", "The Who", "The Carpenters", "George Michael", "Willie Nelson", "The Weeknd", "George Harrison", "Paul McCartney", "John Lennon", "Led Zeppelin", "Michael Jackson", "Norah Jones", "George Michael", "Rich Brian"]

    artist_choice = randrange(len(choices))

    url = "https://www.google.com/search?q=" + choices[artist_choice] + " spotify"
    link = requests.get(url)
    leng = link.text.find("https://open.spotify")
    final = ""
    while link.text[leng] != '&':
        final += link.text[leng]
        leng += 1
    url1 = final
    link1 = requests.get(url1)
    leng1 = [m.start() for m in re.finditer('true."name"', link1.text)]
    final1 = ""
    song_list = []
    for i in leng1:
        while link1.text[i + 13] != '"':
            final1 += link1.text[i + 13]
            i += 1
        song_list.append(final1)
        final1 = ""
    chosen = (song_list[randrange(len(song_list))])
    chosen = chosen.replace("&#39;", "")
    chosen = chosen.replace("&amp", "")
    chosen = chosen.replace("&quot;", "")
    presentation = '"' + chosen + '"' + " by " + choices[artist_choice]
    print(presentation)
    label3.config(text=presentation)

    check = ""
    r = requests.get("https://www.youtube.com/results?search_query=" + presentation)
    results = r.text
    loc = results.index("/watch?")
    for i in range(loc, loc + 100):
        tally = 1
        if results[i] == '"':
            tally += 1
            break
        if tally == 1:
            check += results[i]
    ytlink = "https://www.youtube.com" + check
    linkk.config(text = ytlink)

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
        print("Couldn't download the audio")

def time():
    string = strftime('%H:%M:%S')
    label4.config(text = string)
    label4.after(1000, time)


root = tk.Tk()
root.title("Useful Things")
canvas1 = tk.Canvas(root, width=700, height=600, bg='yellow')
canvas1.pack()


label2 = tk.Label(root, text = "USEFUL THINGS", bg = 'yellow', fg = 'black')
label2.config(font=('Times New Roman', 35))
canvas1.create_window(350, 50, window = label2)
saveButton = tk.Button(text='Click On Me To Convert Image(s) to PDF', command=imagesToPDF, bg='black', fg='yellow', font = 30)
canvas1.create_window(200, 130, window=saveButton)
saveButton.config(font=("Times New Roman", 15))

entry1 = tk.Entry(root)
canvas1.create_window(240, 220, window = entry1, width = 430, height = 30)
button1 = tk.Button(text='Click On Me To Convert Youtube Link To Audio File', command=youtubeToAudio, bg='black', fg='yellow', font = 30)
canvas1.create_window(245, 260, window=button1)
button1.config(font=("Times New Roman", 15))
label1 = tk.Label(root, text = "Paste Link Below (Can Convert Youtube Playlists Too): ", font = 30, bg = 'yellow', fg = 'blue')
canvas1.create_window(220, 190, window = label1)
label1.config(font=("Times New Roman", 13))

button2 = tk.Button(text='Click On Me For A Song Recommendation', command=song_recommender, bg='black', fg='yellow', font = 30)
canvas1.create_window(200, 360, window=button2)
button2.config(font=("Times New Roman", 15))


label3=tk.Label(root,bg='yellow',fg='black')
label3.place(x= 30, y= 400)
label3.config(font=("Times New Roman", 15))

linkk = tk.Label(root, bg = "yellow", fg= "blue", width = 400)
canvas1.create_window(235, 440, window=linkk)
linkk.config(font=("Times New Roman", 15))
linkk.bind("<Button-1>", lambda event: webbrowser.open(linkk.cget("text")))


label4 = tk.Label(root, font=('calibri', 40, 'bold'),bg='yellow',fg= "black")
canvas1.create_window(580, 550, window = label4)

time()




root.mainloop()
