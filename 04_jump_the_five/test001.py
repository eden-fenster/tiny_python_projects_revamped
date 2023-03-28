DATA = {
    'Eden':
        {'age': 24, 'hobbies': [' Music', 'Reading']},
    'Dean':
        {'age': 28, 'hobbies': ['Computers', 'Anoogie']}
}

for name in DATA:
    information = DATA[name]
    age = information['age']
    hobbies = information['hobbies']
    formatted_hobbies = ", ".join(hobbies)
    print(f"{name} is {age} years old and likes {formatted_hobbies}")
    for hobby in hobbies:
        if hobby == "Reading":
            print(f"{name} is a scholar")