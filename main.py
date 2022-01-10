import json


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def percentage(part, whole):
    percent = 100 * float(part) / float(whole)
    return str(percent) + "%"


def square(x):
    return x * x


def calculator():
    print("Select operation:")
    print("1.Plus")
    print("2.Minus")
    print("3.Multiply")
    print("4.Divide")
    print("5.Percent")
    print("6.Square")
    try:
        while True:

            choice = input("Enter number(1, 2, 3, 4, 5, 6): ")

            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", plus(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", minus(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))

                elif choice == '5':
                    print(num1, "is", percentage(num1, num2), "percent of", num2)

                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                    break
            elif choice == '6':
                num_square = float(input("Enter number to square it: "))
                print(square(num_square))

                next_calculation = input("Let's do next calculation? (yes/no): ")
                if next_calculation == "no":
                    break
            else:
                print("You have to choose number from 1 to 6")


    except:
        print("Something went wrong!")

    finally:
        print("Thank you for using our calculator!")


print("Welcome to our app!")
signed_in = 0
male_dict = {"Name":[],"Gender":[],"Age":[]}
female_dict = {"Name":[],"Gender":[],"Age":[]}
gender = str(input("What is your gender: Male/Female :  "))
if gender == "Male":
    age = int(input("Your gender is male, now tell us your age: "))
    print("You are male and your age is", age)
    name = str(input("Please enter your name: " ))
    male_dict["Name"].append(name)
    male_dict["Gender"].append(gender)
    male_dict["Age"].append(age)
    male_txt = open("male_people.txt", 'a')
    for key, value in male_dict.items():
        male_txt.write('%s:%s\n' % (key, value))
    male_txt.write("--------------------------------------------------------" "\n")
    male_txt.close()
    signed_in += 1
elif gender == "Female":
    age = int(input("Your gender is female, now tell us your age: "))
    print("You are male and your age is", age)
    name = str(input("Please enter your name: " ))
    female_txt = open("female_people.txt", 'w')
    female_dict["Name"].append(name)
    female_dict["Gender"].append(gender)
    female_dict["Age"].append(age)
    for key, value in female_dict.items():
        female_txt.write('%s:%s\n' % (key, value))
    female_txt.write("--------------------------------------------------------" "\n")
    female_txt.close()
    signed_in += 1
else:
    print("Enter text correctly!")

if signed_in == 1:
    print("You are signed in successfully", name, ", Enjoy our calculator!")
    calculator()


