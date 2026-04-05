name = "Alice"
age = 20
city = "surrey"
address = "No 15026, Ashyby Place, BC V3S 5G2, Canada"
language = "Python"
is_beginner = True

# Print each variable

print("My Name is " + name)

# Using f-string to print the age variable
print(f" I am {age} years old")

# Step 4 : Check Variable Type

print(type(name))
print(type(age))

# step 5 --- do some calculation with variables

my_birthyear = 2026 - age
print(my_birthyear)

bio = """My name is {}.
I am {} years old.
I live in {}. 
My address is {}. 
I am learning {} programming language. 
It is {} that I am a beginner in programming.""".format(
    name, age, city, address, language, is_beginner)
print(bio)
