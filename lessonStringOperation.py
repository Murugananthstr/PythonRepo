# Concontenation of string
first_name = "Muruganantham"
last_name = "Devaraj"

full_name = first_name + " " + last_name

print(f" Full Name is {full_name}")

# Repetition of string
print("Hello " * 5)

# String indexing
language = "Python"
print(language[0])


# String methods
print(language.upper())
print(language.lower())
print(language.replace("P", "J"))
print("I love tea".replace("tea", "coffee"))

# slicing
print(language[0:4])

print(language[-4:])

# String length

print(len(language))

# Find/in

print("Python" in "I love Python programming")

print("I love Python programming".split(" "))

# Strip space method or trim method
print("  hi   ".strip() + " there")
print("  hi   ".lstrip() + " there")
print("  hi   ".rstrip() + " there")


text = "  hello, python world!  "

print(text.upper())           # "  HELLO, PYTHON WORLD!  "
print(text.lower())           # "  hello, python world!  "
print(text.strip())           # "hello, python world!"  (removes spaces)
print(text.strip().title())   # "Hello, Python World!"

sentence = "I love data science"
print(sentence.replace("love", "enjoy"))   # "I enjoy data science"
print(sentence.split(" "))                 # ["I", "love", "data", "science"]
print(len(sentence))                       # 19

split_sentence = """ Start {} {} {} {}  End """.format(*sentence.split(" "))

print(split_sentence)

# Check if something is inside a string
print("data" in sentence)     # True
print("AI" in sentence)       # False

# Find the position of a word
print(sentence.find("data"))  # 7


name = "Ravi"
score = 95.6789

print(f"Student: {name}")
print(f"Score: {score:.2f}")       # limit to 2 decimal places → 95.68
print(f"Score: {score:.0f}")       # no decimals → 96
print(f"Name upper: {name.upper()}")  # call methods inside {}
print(f"Length of name: {len(name)}")

print("artificial intelligence".title())
print(len("artificial intelligence"))
print("intel" in "artificial intelligence")

print("100,200,300,400,500".split(",")[2])


c = 10 % 2

print(" Result is ", c)

print("Useful string methods in python")
text = "  hello, python world!  "

print(text.upper())           # "  HELLO, PYTHON WORLD!  "
print(text.lower())           # "  hello, python world!  "
print(text.strip())           # "hello, python world!"  (removes spaces)
print(text.strip().title())   # "Hello, Python World!"

sentence = "I love data science"
print(sentence.replace("love", "enjoy"))   # "I enjoy data science"
print(sentence.split(" "))                 # ["I", "love", "data", "science"]
print(len(sentence))                       # 19

# Check if something is inside a string
print("data" in sentence)     # True
print("AI" in sentence)       # False

# Find the position of a word
print(sentence.find("data"))  # 7

print("=".join(["Python", "is", "awesome"]))  # "Python=is=awesome"

print(".".join(['P', 'y', 't', 'h', 'o', 'n']))

template = "Hello, {name}! You're {age}."
print(template.format(name="Alice", age=30))  # "Hello, Alice! You're 30."
help(print)
