import time
greeting=str(input("enter your name:"))

hour = int(time.strftime('%H'))

if hour >= 0 and hour < 12:
    print(f"Good Morning {greeting}!")
elif hour >= 12 and hour < 18:
    print(f"Good Afternoon {greeting}!")
else:
    print(f"Good Evening {greeting}!")

current_time=time.strftime('%H:%M:%S')
print(f"Current time is: {current_time}")