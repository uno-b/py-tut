from math import *  # various math functions

print("\n///// Strings /////\n");

name = "Uno"
age = 20
print("My name is " + name + " and my age is " + age.__str__() + ".")
print("This will always return true: " + name.upper().isupper().__str__() + ".");
print("The length of my name is: " + len(name).__str__());
print("The character at index [0]: " + name[0]);
print("The index of o is at index: " + name.index("o").__str__());
print("The index of no is at index: " + name.index("no").__str__());  # returns index starting with the string/char
print(name + " is now changed to: " + name.replace("Uno", "Kenichi"));  # replace takes 2 arguments

print("\n///// Numbers /////\n");

my_num = 69;
neg_num = -5;
print(my_num);
print("Two ways to convert to string: " + str(my_num) + " " + my_num.__str__());  # first is recommended
print("Absolute value of neg_num is: ")
print(abs(neg_num));    # 5
print("3 to the power of 2 is: ")
print(pow(3, 5));   # 243
print("Minimum of 5 and 3 is: ")
print(min(5, 3));
print("Rounding 5.3 will give us: ")
print(round(5.3));  # 5
print("The floor of 6.9 is: ")
print(floor(6.9));  # 6
print("The ceil of 5.1 is: ")
print(ceil(5.1));   # 6
print("Square root of 25 is: ")
print(sqrt(36));    # 6

print("\n///// Getting input from users /////\n")

name = input("Enter your name: ")
print("You have entered: " + name);
age = input("Enter your age: ")
print("You are " + age + " years old.")

print("\n///// Lists /////\n")


