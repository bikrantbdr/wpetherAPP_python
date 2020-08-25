import tkinter as tk
import requests
from tkinter import font
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600



def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'ERROR 404'

    return final_str


def get_weather(city):
    weather_key = '1002932df04b95b2ac77f92e8df7c2fe'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size = int(lower_frame.winfo_height() * 0.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='e.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=3.6)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=36)
entry.place(relwidth=0.69, relheight=1)

button = tk.Button(frame, text="Get Weather", font=36, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=9.69)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.69, anchor='n')

label = tk.Label(lower_frame,font=("times", 19,"bold"))
label.place(relwidth=1, relheight=1)


weather_icon = tk.Canvas(lower_frame, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=0.25, relheight=0.25)

root.mainloop()