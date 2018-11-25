from math import *  # various math functions


print("\n///// Strings /////\n")

name = "Uno"
age = 20
print("My name is " + name + " and my age is " + age.__str__() + ".")
print("This will always return true: " + name.upper().isupper().__str__() + ".")
print("The length of my name is: " + len(name).__str__())
print("The character at index [0]: " + name[0])
print("The index of o is at index: " + name.index("o").__str__())
print("The index of no is at index: " + name.index("no").__str__())  # returns index starting with the string/char
print(name + " is now changed to: " + name.replace("Uno", "Kenichi"))  # replace takes 2 arguments

print("\n///// Numbers /////\n")

my_num = 69
neg_num = -5
print(my_num)
print("Two ways to convert to string: " + str(my_num) + " " + my_num.__str__());  # first is recommended
print("Absolute value of neg_num is: ")
print(abs(neg_num))    # 5
print("3 to the power of 2 is: ")
print(pow(3, 5))   # 243
print("We can also use two asterisk for powers. For example, 2 to the power of 5 is: ")
print(2**5)
print("Minimum of 5 and 3 is: ")
print(min(5, 3))
print("Rounding 5.3 will give us: ")
print(round(5.3))  # 5
print("The floor of 6.9 is: ")
print(floor(6.9))  # 6
print("The ceil of 5.1 is: ")
print(ceil(5.1))   # 6
print("Square root of 25 is: ")
print(sqrt(36))    # 6

print("\n///// Getting input from users /////\n")

# name = input("Enter your name: ")
# print("You have entered: " + name);
# age = input("Enter your age: ")
# print("You are " + age + " years old.")

print("\n///// Lists /////\n")

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]     # multiple data types can be inside the string
print("My friend's name at index [1] is: " + friends[1])   # Karen
print("My friend's name at index [1] is: " + friends[-1])  # Toby
# can get the element at index [1] from back of the list
# starts from [-1] index
print(friends[1:])  # ['Karen', 'Jim', 'Oscar', 'Toby']
# returns array with elements beginning at index[1]
print(friends[1:3])     # ['Karen', 'Jim']
# returns array with elements from index [1] to exclusive [3]

print("\n///// List functions /////\n")

lucky_numbers = [12, 99, 69, 33, 123]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends1 = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)   # extends lucky_numbers to friends list
friends.append("Creed")     # adds an element at the end of the list
friends.insert(1, "Kelly")      #inserts "Kelly" at index [1], all other elements are moved
friends.remove("Jim")   # removes element with value "Jim"
friends.pop()       # removes last element in the list ("Creed")
print(friends)      # ['Kevin', 'Kelly', 'Karen', 'Oscar', 'Toby', 12, 99, 69, 33, 123]
print(friends.count("Kevin"))      # returns the number of elements with value "Kevin"
print(friends.index("Karen"))      # returns the first index of element with value "Karen"
friends1.sort()      # sort in ascending order using first letter
print(friends1)     # ['Jim', 'Karen', 'Kevin', 'Oscar', 'Toby']
lucky_numbers.reverse()     # sort in a descending order using numbers
print(lucky_numbers)    # [123, 33, 69, 99, 12]
friends.clear()     # removes every element
print(friends)      # []
friends = friends1.copy()   # friends is the same as friends1 now
print(friends)




