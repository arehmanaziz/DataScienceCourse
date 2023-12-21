print("Thank you for chooisng Python Pizza Deliveries..")

size = input("Enter size of pizza (s, m, l): ").lower()

price = 0

if size == "s":
    price = 600
    opt = input("want to add extra chicken (y/n)? ").lower()
    if opt == "y":
        price += 100
    elif opt != "n":
        print("Invalid Option")


elif size == "m":
    price = 1000
    opt = input("want to add extra chicken (y/n)? ").lower()
    if opt == "y":
        price += 200
    elif opt != "n":
        print("Invalid Option")
    



elif size == "l":
    price = 2000
    opt = input("want to add extra chicken (y/n)? ").lower()
    if opt == "y":
        price += 300
    elif opt != "n":
        print("Invalid Option")


else:
    print("Invalid Option")

print(f"Total bill is {price}Rs.")



