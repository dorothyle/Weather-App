import tkinter as tk
from tkinter import *
import requests
import json


def format_response(weather):
    try:
        name = weather['city']['name']
        desc = weather['list'][0]['weather'][0]['description']
        temp = weather['list'][0]['main']['temp']

        weather_info = "City: %s\nConditions: %s\nTemperature (°F): %s" % (name, desc, temp)
    except:
        weather_info = "There is a problem retrieving this information."

    return weather_info


def get_weather(city):
    weather_key = '7bde330e31b0669716f01209cd7c6bf6'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q':city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


root = Tk()

canvas = Canvas(root, height=500, width=600)
canvas.pack()

background_image = PhotoImage(file='weather_background.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Creates top frame
frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=("Courier", 16))
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get Weather", font=("Courier", 16),
                command=(lambda: get_weather(entry.get())))
button.place(relx=.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=("Courier", 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
