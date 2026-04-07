word = "Python"


# sequence[start : stop : step]


print(word[0])
print(word[1])
print(word[2])
# Printing last character of the string
print(word[-1])

# Printing second last character of the string
print(word[-2])

# Slicing and grab a range
print("Slicing and grab a range")
print(word[0:4])
print(word[1:5])
print(word[2:5])
print(word[:4])

print(word[1:])
print(word[:])

# Slicing with step

print("Slicing with the step")
print(word[0:4:2])  # Pton
print(word[0:6:2])  # Ph
print(word[0:6:3])  # Pn
print(word[::-1])


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[::2])


print(nums[1:8:2])

print(nums[::-1])


print(nums[8:2:-2])


text = "Python"


print(text[::2])
print(text[::-2])


# [:] → copy whole sequence
# [::2] → every 2nd item
# [::-1] → reverse
# [start:stop:step] → full control slicing
