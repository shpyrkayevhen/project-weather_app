from tkinter import *
from tkinter import ttk, messagebox
import tkinter
from unittest import result
# Щоб визначити геолокацію запиту за адресою та координатами
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from pprint import pprint


window = Tk()
window.title('Wheather App')
window.geometry('900x500+300+200')
window.resizable(False, False)


def getWeather():
    try:
        city = text_field.get()
        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,  # Довгота
                                 lat=location.latitude)  # view a Europe/Kiev
        print(result)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        # local_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
        print(local_time)
        current_time = local_time.strftime('%I:%M %p')
        print(current_time)
        clock.config(text=current_time)
        name.config(text='CURRENT WEATHER')

        # weather
        api = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
            city+'&appid=afa86948e465dba800e0d259077f48e1'

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, '°С'))
        c.config(text=(condition, '|', 'FEELS', 'LIKE', temp, '°С'))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror('Wheather App', 'Invalid Entry!')


# search box
search_image = PhotoImage(file='search.png')
window_image = Label(image=search_image)
window_image.place(x=20, y=20)


text_field = Entry(window, justify='center', width=17,
                   font=('poppins', 25, 'bold'), background='#404040', border=0, fg='white')
text_field.place(x=50, y=40)
text_field.focus()


search_icon = PhotoImage(file='search_icon.png')
window_icon = Button(image=search_icon, borderwidth=0,
                     cursor='hand2', bg='#404040', command=getWeather)
window_icon.place(x=400, y=34)


# logo
logo_image = PhotoImage(file='logo.png')
window_logo = Label(image=logo_image)
window_logo.place(x=150, y=100)


# Bottom box
box_image = PhotoImage(file='box.png')
window_buttom_box = Label(image=box_image)
window_buttom_box.pack(padx=5, pady=5, side='bottom')


# time
name = Label(window, font=('arial', 15, 'bold'))
name.place(x=30, y=100)
clock = Label(window, font=('Helvetica', 20))
clock.place(x=30, y=130)

# Label (first argument (window) means that this is perent window. The place where we add this elements)
label1 = Label(window, text="WIND", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)

label2 = Label(window, text="HUMIDITY", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)

label3 = Label(window, text="DESCRIPTION", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)

label4 = Label(window, text="PRESSURE", font=(
    'Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)

w = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=120, y=430)

h = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
h.place(x=280, y=430)

d = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
d.place(x=420, y=430)

p = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
p.place(x=670, y=430)

t = Label(font=('arial', 70, 'bold'), fg='#ee666d')
t.place(x=400, y=150)
c = Label(font=('arial', 15, 'bold'))
c.place(x=400, y=250)


# Виконати Tkinder
window.mainloop()
