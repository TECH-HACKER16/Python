import datetime

hour = datetime.datetime.now().hour
date = datetime.date.today().strftime("%d-%m-%Y")
day = datetime.datetime.today().strftime("%A")
time = datetime.datetime.now().strftime("%H:%M")

def date_today():
    print("Today\'s date is", date, "i.e,", day)

def current_time():
    print("Time :", time)

def wish():
    if 0 <= hour < 12:
        print("Good Morning!")
    elif 12 <= hour < 16:
        print("Good Afternoon!")
    elif 16 <= hour < 19:
        print("Good Evening!")
    else:
        print("Good Night!")


date_today()
current_time()
wish()
