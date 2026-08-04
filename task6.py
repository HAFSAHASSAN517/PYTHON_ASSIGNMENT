#Create a BankAccount class with deposit, withdraw, and balance methods
class BankAccount:
    def __init__(self):
         self.amount=10000
    def deposit(self):
        print("how much money do you want to deposit")
        deposit_amount=int(input("enter the amount : "))
        if 5000<= deposit_amount <=20000 and deposit_amount % 5 == 0:
            self.amount += deposit_amount
            
            print("you can deposit this amount")
        else:
            print("you can not deposit  this amount")    
     
        
        
    def withdraw(self): 
        print("how much money do you want to withdraw")
        withdraw_amount=int(input("enter the amount only divisible by 5 "))
        if withdraw_amount % 5 == 0 and withdraw_amount<=self.amount:
            self.amount-=  withdraw_amount
            
            print("withdraw successful")
        else:
                    print("you can not deposit  this amount")    
                
        
           
    def balance(self): 
        print("do you want to know your balance ")
        account_number= input("enter your account number to see the balance in your account")
        if account_number == "12345":
            print("your balance is " , self.amount)
        else:
            print("invalid input")    
           
account = BankAccount()        

print("1= deposit")
print("2=withdraw")
print("3=balance ")
user_input=input("enter a number of your choice")
if user_input == "1":
    account.deposit()
elif user_input=="2":
    account.withdraw()
elif user_input == "3":
    account.balance()
else:
    print("invalid entry of number")
 #===Build a Student class with name/grade attributes and a method to compute GPA===#
 
class Students():
     def __init__(self,student_name,student_grade):
          self.student_name = student_name
          self.student_grade= student_grade
     def GPA(self):
         grade = int(input("enter your grades to know your GPA"))
         if grade >= 84 :
            print("your gpa is '4'")
         elif grade >= 70 :
            print ("your gpa is 3")
         elif grade >= 60 :
            print("your gpa is 2") 
         else:
            
            print("fail")
student = Students("jhon",86)
print("know your gpa")
student.GPA()
#Write a Car class with attributes make/model/year and a display_info() method

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.make},{self.year},{self.model}")    
showroom = [
    Car("toyota","cramy",2024),
    Car("Ford", "Mustang", 2023),
    Car("Honda", "Civic", 2024),
    Car("BMW", "M3", 2025),
    Car("Tesla", "Model 3", 2026)
]    
for car in showroom:
    car.display_info()
    
#Create 5 objects from a Product class and store them in a list; print all using str   
class Product():
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
    def __str__(self):
        print(f"{self.name} , {self.price} , {self.category}")
        
        
warehouse_inventory = [
    Product("Laptop", 999.99, "Electronics"),
    Product("Wireless Mouse", 25.50, "Electronics"),
    Product("Coffee Maker", 49.99, "Appliances"),
    Product("Running Shoes", 85.00, "Footwear"),
    Product("Backpack", 45.00, "Accessories")
]  
for item in warehouse_inventory:
    print(str(item))        
#Build a Library class that stores a list of books and has methods to add, remove, and search books
class Library():
      books = [
    "The Pragmatic Programmer",
    "Clean Code",
    "Python Crash Course",
    "Automate the Boring Stuff with Python",
    "Fluent Python",
    "Think Python",
    "Introduction to Algorithms",
    "The Art of Computer Programming",
    "Deep Learning with Python",
    "Effective Python"
]
      def add(self):
          add_book = input("do you want to enter book")
          self.books.appen(add_book)
          print("book has bee added")
      def remove(self):
          
          remove_book = input("do you want to remove book")
          if remove_book in self.books:
            self.books.remove(remove_book)
            print("book has been removed")
          else:
              print("book not found")  
      def search(self):
          search_books = input("searcch book")
          if search_books in self.books:
              print("book is available")
          else:
              print("book not found")    
lib = Library()          
print("WELCOME TO THE LIABRARY")
print("1== ADD BOOK")
print("2== REMOVE BOOK")
print("3== search BOOK")
enter_input = input("enter a number")   
if enter_input== "1":
    lib.add()
elif enter_input == "2":
    lib.remove()
        
elif enter_input == "3":
    lib.search()
else:
    print("invalid input")               
                 
                   