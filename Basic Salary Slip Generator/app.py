#Basic Salary Slip Generator
emp_name=str(input("what is your name:"))
basic_salary=float(input("enter your basic salary:"))
bonus=float(input("enter bonus amount:"))
tax_rate=float(input("enter tax rate:"))
hra=0.20*basic_salary
medical=0.10*basic_salary
gross_salary=basic_salary+hra+medical+bonus
tax_amount=(gross_salary*tax_rate)/100
net_salary=gross_salary-tax_amount
print("🔹 Salary Slip 🔹")
print("Name:",emp_name)
print("Basic Salary:",basic_salary)
print("Bonus:",bonus)
print("HRA (20%):",hra)
print("Medical (10%):",medical)
print("--------------------")
print("Gross Salary:",gross_salary)
print("Tax Deducted (" + str(tax_rate) + "%):", tax_amount)
print("Net Salary:",net_salary)