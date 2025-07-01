# 👋 Good Morning Sir

## 🔹 **Project Introduction**
This simple Python project greets the user based on the current time of day — saying **Good Morning**, **Good Afternoon**, or **Good Evening** — and displays the current system time. A great example of using real-time data and conditional logic in Python.

---

## 🧠 **What I Learned**
- `input()` function for taking user input
- `time` module in Python
- Using `strftime()` to get current hour and time
- Conditional statements (`if`, `elif`, `else`)
- String formatting with `f-strings`

---

## 🧩 **Features**
- 🕰️ Dynamic greeting based on real-time system clock  
- 🙋 Personalized message using user input  
- 🧾 Displays current time in HH:MM:SS format  

---

## ⚙️ **How It Works**
1. Takes the user's name as input.
2. Fetches the current hour using `time.strftime('%H')`.
3. Applies conditional logic:
   - If hour is between 0–11 → Good Morning  
   - If hour is between 12–17 → Good Afternoon  
   - Otherwise → Good Evening  
4. Displays the appropriate greeting and the current time.

---

## 📤 **Output Preview**
```

enter your name: Waheed
Good Evening Waheed!
Current time is: 19:45:12

```

---

Thanks for checking out this mini project! 🚀  
Feel free to fork, modify, or use it to learn how Python handles time and user interaction. 😊  
Happy coding! 💻🐍
