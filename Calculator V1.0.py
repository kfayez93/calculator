print ("~~~Mini Calulator~~")

num1 = float(input("Enter first number here : "))
num2 = float(input("Enter second number here : "))

print ("press 1 for Addition \npress 2 for Subtraction \npress 3 for Multiplication \npress 4 for Division")

choice = int(input("Enter your choice from 1 - 4: "))

if choice == 1:
  print ("The value of", num1, "+", num2, "is: ", num1 + num2)

elif choice == 2:
  print ("The value of", num1, "-", num2, "is: ", num1 - num2)

elif choice == 3:
  print ("The value of", num1, "*", num2, "is: ", num1 * num2)

elif choice == 4:
  print ("The value of", num1, "/", num2, "is: ", num1 / num2)

else:
  print ("Invalid Input")