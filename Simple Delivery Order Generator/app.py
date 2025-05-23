#Simple Delivery Order Generator

CustomerName=str(input("Enter your name:"))
ItemName=str(input("Enter your item name:"))
ItemQuantity=int(input("Enter your item quantity:"))
PriceperUnit=float(input("Enter price of item:"))
DeliveryAddress=str(input("Enter your delivery address:"))
ContactNumber=str(input("Enter your contact number:"))
Total=float(ItemQuantity*PriceperUnit)
print("🔹 Delivery Order Summary 🔹\n")
print("Customer Name:",CustomerName)
print("Item:",ItemName)
print("Quantity:",ItemQuantity)
print("Price Per Unit:",PriceperUnit)
print("Total",Total)
print("Deliver to:",DeliveryAddress)
print("Contact:",ContactNumber,"\n")
print("Thank you for ordering with us!")

