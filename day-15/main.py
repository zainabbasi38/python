import time

timestamp = time.strftime("%H:%M:%S")
hours = int(time.strftime("%H"))
# hours = 15
if hours > 0 and hours < 12:
    print("Good Morning")
elif hours >= 12 and hours < 16:
    print("Good AfterNoon")
else:
    print("Good Night")

print(timestamp)