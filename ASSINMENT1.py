name=input("enter your name: ")
age=int(input("enter your age: "))
city=input("enter your city: ")
print("Hello, my name is", name, "I am", age, "years old and I live in", city)
 
 
 
a=int(5)
b=str("hello")
c=float(3.563)
d=bool(True)
print("a",type(a))
print("b",type(b))
print("c",type(c))
print("d",type(d))        
 
##calculator
a=int(input("enter first number: "))
b=int(input("enter second number: "))
operation=input("enter operation (+, -, *, /): ")
if operation=="+":
    print("output is", a+b)       
elif operation=="-":
    print("output is", a-b)
elif operation=="*":
    print("output is", a*b)
elif operation=="/":
    if b!=0:
        print("output is", a/b)
    else:
        print("not divisible as denominator is zero.")
else:
    print("Invalid operation")                    


###string slicing
text=input("enter your text: ")
print("originalstring",text)
print("sliced string",text[0:6])
print("reverse string",text[::-1]) 
print("reverse sliced string",text[1:6][::-1])
print("sliced string ,reversed",text[1:6:3])





### profile
name=input("enter your name: ")
age=int(input("enter your age: "))
city=input("enter your city: ")
fav_hobby=input("enter your favourite hobby: ")
print("===========PROFILE===========")
print("NAME:",name)
print("AGE:",age)
print("CITY:",city)
print("FAVOURITE HOBBY:",fav_hobby)
print("===========END OF PROFILE===========")