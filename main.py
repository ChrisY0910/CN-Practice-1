#Chris Yang 7/27/21 Python practice on Repl
import turtle

#Problem 2: Averages
#Ask for numbers
num1 = int(input("Give me the first number."))
num2 = int(input("Give me the second number."))
num3 = int(input("Give me the third number."))
num4 = int(input("Give me the fourth number."))
#Finds the average
print("This is your average: " + str((num1 + num2 + num3 + num4) / 4))


#Problem 3: Dinner bill
#Ask user for total cost of dinner.
total = int(input("What is your total bill?:"))
#Asks user how many people were there.
diners = int(input("How many diners ate this meal?:"))
#Calculate and print how much each person should pay
print("This is how much each person should pay: $" + str(total/diners))