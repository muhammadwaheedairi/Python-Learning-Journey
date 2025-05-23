# 💳 Credit Card Masker & Summary

A beginner-level Python script that takes a credit card number as input, masks it for privacy, and displays key details.

---

## 🧠 What I Learned

✔ Taking user input using `input()`
✔ String slicing and indexing
✔ Masking sensitive data using `*`
✔ Using `len()` to get string length
✔ Formatting output cleanly with `print()`

---

## 🧩 Features

✅ Masks all digits except the last 4 for security
✅ Prints:

* Total length of the card number
* First 6 digits (usually the BIN)
* Last 4 digits (used for reference)
  ✅ Includes a thank-you message

---

## 📤 Output Preview

```
🔹 Credit Card Summary 🔹  
Card Number (Masked): ************1234  
Length of Card Number: 16  
First 6 Digits: 123456  
Last 4 Digits: 1234  
Thank you for using our service!
```