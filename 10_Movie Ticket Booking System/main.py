name=str(input("Enter your name:"))
age=int(input("Enter your age: "))
movie_type=str(input("Enter the movie type  (Kids/General/18+):"))
if movie_type=="18+" and age>=18:
        tickets=int(input("Enter the number of tickets: "))
        price_pr_tickets=float(input("Enter the price per ticket:"))
        total_price=tickets*price_pr_tickets
        print("Welcome to Python Cinema!")
        print("Name:", name.title())
        print("Age:", age)
        print("Movie Type:",movie_type.title())
        print("Tickets:", tickets)
        print("Price per Ticket:", price_pr_tickets)
        if tickets > 3:
            total_price = tickets * price_pr_tickets * 0.9 
            print("You get a 10% discount for booking more than 3 tickets.")
            print("Final amount after discount:", total_price) 
        print("Final amount to pay:", total_price)
        print("Thank you for booking with Python Cinema!") 
else:
    print("You are not eligible to book tickets for this movie.")