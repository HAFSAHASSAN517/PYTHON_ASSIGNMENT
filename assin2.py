#==========
shopping_list =["milk","bananas","soya beans","boiled eggs","feta cheese"]
print("shopping_list_1:", shopping_list)

shopping_list.append("flour")
print("shopping_list_2:", shopping_list)
shopping_list.remove("boiled eggs")
print("shopping_list_3:", shopping_list)
print("final shopping list")
for item in shopping_list:
    print(item)
#===========
k=0
m=1
while k<=100:
    print(k)
    f=k+m
    k=m
    m=f
#==============
#phonebook
phonebook={"sara":{"phone_number":"1579455699","email":"havsghd@gmail.com"},
           "jsd":{"phone_number":"484682545655","email":"xghdghj@gmai.com"}}
print(phonebook)
print(phonebook["sara"]["email"])
phonebook.pop("jsd")
print(phonebook)
##==============

s1={1,2,3,4,58,453,45325}
s2={1,2,3,4,5,6744,56313,654,58}
print(s1.intersection(s2))




marks=input("enter your marks: ")
if int(marks)>=85:
    print("Grade is A")
elif int(marks)>=70:
    print("Grade is B")
elif int(marks)>=60:
    print("Grade is C")
elif int(marks)>=50:
    print("Grade is D")    
else:
    print("failed")       
    
    

menu = {
    "fast_food": {"burger": "$12", "pizza": "$20", "fries": "$5"},
    "drinks": {"coke": "$3", "pepsi": "$3", "water": "$1"},
    "desserts": {"ice cream": "$4", "cake": "$6", "cookies": "$2"},
}
pizza_flavours = ["Pepperoni", "Margherita", "BBQ Chicken", "Hawaiian", "Veggie Supreme"]
burger_flavors = [
    "Classic Cheeseburger", "BBQ Bacon Burger", "Mushroom Swiss", "Spicy Jalapeno", "Veggie Black Bean"
]
print("welcome to our app")
print("would you like to order something?")
print('insert "YES" for ordering or "NO" for exiting')
customer_input = input("enter your choice: ").lower()
if customer_input == "yes":
    print("select from the menu below")
    for category, items in menu.items():
      print(category)
      for item, price in items.items():
        print(f"  {item}: {price}") 
    category = input("enter your category: ").lower()
    if category in menu:
        print("select from the menu below")
        for item, price in menu[category].items():
            print(f"{item}: {price}")
        item = input("enter your item: ").lower()
        if item == "pizza":
            print("please select your pizza flavour")
            print(pizza_flavours)
            flavour = input("enter flavour of your pizza: ").title()
            if flavour in pizza_flavours:
                print(f"your order pizza flavour {flavour} is being processed")
            else:
                print("not availble")    
        elif item == "burger":
            print("pls select your burger flavour")
            print(burger_flavors)
            flavour = input("enter your burger flavour: ").title()
            if flavour in burger_flavors:
            
                print(f"your order of burger flavour {flavour} is being processed")
            else:
                print("not availble")
        elif item == "fries":
            print("your order of fries is being processed")
        else:
            print("the item you selected is not available")
    else:
        print("the category you selected is not available")
elif customer_input == "no":
    print("thank you for visiting")
else:
    print('Invalid choice, pls enter "YES" or "NO".')

print("menu after adding cutlery and sauces")
menu["cutlery"] = {"fork": "$1", "knife": "$1", "spoon": "$2"}
menu["sauces"] = {"ketchup": "$1", "mayo": "$1", "mustard": "$1"}
print(menu)
del menu["cutlery"]
print(menu)
