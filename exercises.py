# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

print('===================')
print('Exercise 1 List and Indexing')
print('-------------------')



def manage_students():
    students = ['Ahmed', 'Hameed', 'Saeed']
    first_student = students[1]
    last_student = students[-1]

    return students, first_student, last_student

# Call the function and print the result
print('Exercise 1:', manage_students())

print('===================')

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

print('===================')
print('Exercise 2 Loop and String Concatenation')
print('-------------------')

def combine_foods():
    foods = ('Pizza', 'Pasta', 'Burger')
    meal = ''
    for food in foods:
        meal += food + ' '

    return foods, meal


# Call the function and print the result
print('Exercise 2:', combine_foods())

print('===================')


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

print('===================')
print('Exercise 3 Slicing Tuples')
print('-------------------')

def slice_foods():
    foods = ('Pizza', 'Pasta', 'Burger', 'Fries', 'Salad')
    last_two_foods = foods[-2:]

    return foods, last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())

print('===================')

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

print('===================')
print('Exercise 4 Dictionaries and String Formatting')
print('-------------------')

def hometown_info():
    home_town = {
        'city': 'New York',
        'state': 'New York',
        'population': '8.4 million'
    }

    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"

    return home_town, home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())

print('===================')

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

print('===================')
print('Exercise 5 Iterating Over Dictionary Items')
print('-------------------')

def list_home_town_items():
    home_town = {
        'city': 'New York',
        'state': 'New York',
        'population': '8.4 million'
    }

    home_town_items = []
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")

    return home_town_items


# Call the function and print the result
print('Exercise 5:', list_home_town_items())


print('===================')