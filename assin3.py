def prime_number():
    a=int(input("enter any number from 1 to 50 to check prime number "))
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a % i== 0:
            return False
    return True
print(prime_number())    
###########
num=list(map(int,input("enter a numbr").split()))
sq_nu =list(map(lambda x:x*x,num))

print("squared number",sq_nu)
##########
def calculation():
    num1= int(input("enter num1"))
    num2 = int(input("enter num2"))
    try:
        result=num1/num2
        print("result",result)
        
    except ZeroDivisionError:
        print("invalid numbers ,zero should not be in denomenatorr")
calculation()        
        
        ##################
def INTEREST():
             def SI():
                p = float(input("enter the principal amount"))
                r = float(input("enter the interest rate"))
                t = float(input("enter time "))
                simple_interest = (p * r * t)/ (100)
                print(simple_interest ," will be your simple interest")
             def CI():
                p = float(input("Principal"))
                r = float(input("Annual interest rate (%)"))
                t = float(input("Time (years)"))
                amount = p*(1+r/100)**t
                compound_interest = amount - p
                print(compound_interest ," is your compound interest")  
             print("what typ of interest calculation you want to do ?")
             print("SIMPLE_INTEREST")
             print("COMPOUND_INTEREST")
             interest_cal = input("enter your choice").lower()
             if interest_cal== "simple_interest":
                  SI()
        
             elif interest_cal== "compound_interest":
                 CI()
           
             else:
                 print( "error")
INTEREST()
#######
def calculator():
    try:
         a=int(input("enter a number "))
         b = int (input("enter a number"))
         def add(a,b):
             return a+b
         def sub(a,b):
             return a-b
         def div(a,b):
             return a/b    
         def mul(a,b):
             return a*b
         print("choose an operation")
         print("1=add")
         print("2=sub")
         print("3=div")
         print("4=mul")
         choice=input("pls choose any number between 1 to 4") 
         if choice == "1":
             print("result",add(a,b))
         elif choice == "2":
             print("result",sub(a,b))
         elif choice == "3":
             print("result",div(a,b))
         elif choice == "4":
             print("result",mul(a,b))      
         else:
             print("invalid")      
                 
    
    except ValueError:
        print("inavlid, pls enteer number only")    
    except ZeroDivisionError:
        print("error , not divisible by zero")    
calculator()        