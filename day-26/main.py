import time

timestamp = time.strftime("%H:%M:%S")
hours = int(time.strftime("%H"))
# hours = 15
if hours >= 0 and hours < 12:
    
    print("Good Morning")
elif hours >= 12 and hours <= 17:
    if hours > 12:
        hours = hours - 12
    print("Good AfterNoon")
else:
    
    hours = hours - 12
    print("Good Night")

print("It's time is",hours,"o'clock")