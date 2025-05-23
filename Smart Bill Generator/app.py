#Smart Bill Generator
customer_name =str("waheed")
item_name = str("Notebook")
item_quantity = str("5")     
item_price =float(75.5)         
quantity=int(item_quantity)
total=quantity*item_price
print("Smart Bill Generator\n")
print("Coustomer Name:",customer_name)
print("Item Name:",item_name)
print("Qanatity:",quantity)
print("Item Price:",item_price)
print("Total bill:",total)
print("Type of total price is",type(total))
