# I HAVE MAKE THIS CALCULATOR USING PYTHON AT THE AGE OF 16YEAR'S ONLY
# MY NAME AKSHIT PANDEY

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1*num2

def divide(num1, num2):
  "Divides two numbers (handles division by zero)"
  if num2 == 0:
    return "Error: Cannot divide by zero"
  else:
    return num1 / num2

while True:
  
  num1 = float(input("Enter the first number: "))
  operator = input("Enter the operator (+, -, *, /): ")
  num2 = float(input("Enter the second number: "))

  if operator == "+" :
    result= add(num1, num2)
    print(result)
  
  elif operator == "-":
    result= subtract(num1 , num2)
    print(result)

  elif operator == "*" :
    result= multiply(num1, num2)
    print(result)

  elif operator == "/":
    result= divide(num1, num2)
    print(result)

  else:
    print("Operator invalid")


  print("Thank you for using the calculator!")

  wanttobreakloop= input("Do you want to make other calculation? (y/n): ")
  if wanttobreakloop.lower() != "y":
    break
  else:
    print("Ok, let's continu")