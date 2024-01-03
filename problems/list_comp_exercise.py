numbers1 = [1, 2, 3, 4, 5]
# Desired outcome: [1, 4, 9, 16, 25]
squared = [num**2 for num in numbers1]
print(squared)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Desired outcome: [2, 4, 6, 8, 10]
even = [num for num in numbers if num% 2==0]
print(even)


words = ["apple", "banana", "orange", "grape", "kiwi"]
# Desired outcome: ["apple", "grape"]
specific_fruit = [fruit for fruit in words if fruit == 'apple' or 'grape']
print(specific_fruit)

text = "hello world"
# Desired outcome: "hEllo wOrld"
text = "hello world"
uppercase_vowels = ''.join([char.upper() if char.lower() in 'aeiou' else char for char in text])
print(uppercase_vowels)

numbers2 = [-2, -1, 0, 1, 2]
# Desired outcome: [1, 4]
squ = [num**2 for num in numbers2 if num < 0]
print(squ)

