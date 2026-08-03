#Create an Animal parent class and Dog/Cat child classes that override a speak() method
class Animal():
    
    def speak(self):
        print("animal make sound")
class cat(Animal):
    def speak(self):
        
     print(f"the cat says : meow")
class dog(Animal):
    def speak(self):
        print(f" dog says : woof ")    

    
DOG = dog()
CAT =  cat()
cat.speak()
dog.speak()
#Build a Shape hierarchy (Shape → Circle, Rectangle) with an area() method each overrides
class Shape():
    
    def area(self):
         pass        
class rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
       print(f"AREA: {self.length * self.width}")
class circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(f"area of circle is {3.14 *self.radius*self.radius}")        
CIRCLE = circle(8)
RECTANGLE = rectangle(4,7) 
CIRCLE.area()
RECTANGLE.area()            
#Write a program demonstrating polymorphism by calling the same method on different objects
class SOUND():
    def music(self):
        pass
class paino(SOUND):
    def __init__(self,sound):
        self.sound = sound
    def music(self):
        print(f"the paino make {self.sound} ")
class drum(SOUND):
    def __init__(self,sound):
        self.sound=sound        
    def music(self):
        print(f"the drum make {self.sound}")
            
Paino = paino("tan,tan,tan")        
  
DRUM = drum("dhum ")
for insturment in (Paino,DRUM):
    insturment.music()       
#Use encapsulation to create a Person class where age is private and only accessible via a getter
class Person():
    def __init__(self,name,age,occupation):
        self.name = name
        self.__age = age
        self.occupation = occupation
    def get_age(self):
        return self.__age    
    def details(self):
        print(f"details of the person are {self.name} , {self.get_age()}, {self.occupation}")
person = Person("sara",25,"artist")       
person.details() 
#Create an Employee class and a Manager subclass using super() that adds a team_size attribute and a manage() method

class Employee(): 
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
class Manager(Employee):
    def __init__(self,name,employee_id,team_size):
        super.__init__(name,employee_id)
        self.team_size = team_size
    def manage(self):
        print(f"{self.name} manages a team of {self.team_size} employee")
employee= Manager("sara",30,400)
employee.manage()           