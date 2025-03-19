# people = [
#     {'name': 'Tom', 'age': 39, 'company': 'SuperCorp', 'Languages': ['Python', 'JavaScript']},
#     {'name': 'Bob', 'age': 43, 'company': 'BigCorp', 'Languages': ['Python', 'C++', 'C#']},
#     {'name': 'Sam', 'age': 28, 'company': 'LittleCorp', 'Languages': ['Python', 'Java']}
# ]

# for person in people:
#     print(f"Name: {person['name']}\nLast language: {person['Languages'][-1]}\n")

# def calculate_scrabble_score(word):
#     letter_values = {
#         'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
#         'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#         'D': 2, 'G': 2,
#         'B': 3, 'C': 3, 'M': 3, 'P': 3,
#         'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#         'K': 5,
#         'J': 8, 'X': 8,
#         'Q': 10, 'Z': 10
#     }

#     score = 0
#     for char in word.upper():
#         if char in letter_values:
#             score += letter_values[char]
#         else:
#             print(f'Такая буква не поддерживается {char}')
#     return score


# user_input = input('Введите любое слово: ')
# result = calculate_scrabble_score(user_input)
# print(result)

# def to_dict(lst):
#     return {element: element for element in lst}

# print(to_dict([1, 2, 3, 4]))

# my_dict = {'first': 'we can do it'}

# def biggest_dict(**kwargs):
    
#     my_dict.update(kwargs)

# biggest_dict(second='this is second')
# print(my_dict)