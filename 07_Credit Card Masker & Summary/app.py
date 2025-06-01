#Credit Card Masker & Summary
cardnumber=str(input("Enter your credit card number:"))
n = len(cardnumber)
masked="*"*(n-4)+cardnumber[-4:]
print("🔹 Credit Card Summary 🔹")
print("Card Number (Masked):",masked)
print("Length of Card Number:",n)
print("First 6 Digits:",cardnumber[0:6])
print("Last 4 Digits:",cardnumber[12:16])
print("Thank you for using our service!")
