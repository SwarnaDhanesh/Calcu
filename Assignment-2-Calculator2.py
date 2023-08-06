class Calculator: 
 def __init__(self,num1,num2):
     self.num1=num1
     self.num2=num2
     pass
 def add(self):
    return self.num1+self.num2
    pass
 def subtract(self):
    return self.num1-self.num2
    pass
 def multiply(self):
  return self.num1*self.num2
  pass
 def divide(self):
      return self.num1/self.num2
pass
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice=input(

"""
a.Add
b.Subtract
c.Multiply
d.divide
e.Exit
""") 
obj=Calculator(num1,num2)
if choice=="a":
  print("The Result is:",end="")
  print (obj.add())
elif choice=="b":
   print("The Result is:",end="")
   print (obj.subtract())
elif choice=="c":
   print("The Result is:",end="")
   print (obj.multiply())
elif choice=="d":
   print("The Result is:",end="")
   print (obj.divide())
else:
  print("Error! operator is not correct")