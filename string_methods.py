# Question no. 1: write a python program that converts the string "Hello World" into all uppercase and all lowercase letters.

letters = "Hello World"
print(letters.upper())

letters = "Hello World"
print(letters.lower())

# Question no.2: Given the "  python  " , remove the extra spaces from both sides and print the result.
text = "  python  "
print(text.strip())

# Question no.3: Replace "Java" with "Python" in the string "I love Java"
sentence = "I love Java"
print(sentence.replace("Java", "Python"))

# Question no.4: Find the position of the word "code" in the string "I write code every day".
sentence = "I write code every day"
print(sentence.find("code"))

# Question no.5 : Count how many times the letter "a" appears in "banana ".
word = "banana"
print(word.count("a"))

# Question no.6: checks whether the string "python_progrm.py ": starts with "python" and ends with ".py".
filename = "python-program.py"
print(filename.startswith("python"))
print(filename.endswith(".py"))
print(filename.startswith(".py"))
print(filename.endswith("python"))

# Question no.7 : Split the string "apple,banana.orange" into a list.
fruits = "apple,banana,orange"
print(fruits.split(","))

# Questio no.8 : join the list["Learn", "python", "today"] into a single string with spaces.
words = ["Learn", "python", "today"]
print(" ".join(words))

# Question no.9 : Check whether the string "Hello123" contains only alphabets.
text = "Hello123"
print(text.isalpha())

# Question no. 10:Check whether the string "2025" contains only digits.
number = "2025"
print(number.isdigit())
