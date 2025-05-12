# get users name and print a random greeting along with their name

import re
import random

def valid_name(name):
    name = name.strip() # remove leading and trailing whitespace
    if not name:
        return False, "Name cannot be empty"
    name = re.sub(r'\s+', ' ', name) # collapses multiple spaces
    if not any(c.isalpha() for c in name):
        return False, "Name must contain at least one letter"
    if len(name) > 50:
        return False, "Name is too long(max 50 characters)"
    if not re.match(r'^[a-zA-Z\s\'\-]+$', name):
        return False, "Name can only contain letters, spaces, hyphens, apostrophes" # alpha+spaces+hyphens+apostrophes only
    return True, name 

max_attempts = 3 
for attempt in range(max_attempts):
    user_name = input("Enter your name: ")
    is_valid, result = valid_name(user_name)
    if is_valid:
        user_name = result
        break
    print(f"Error: {result}")
    if attempt == max_attempts - 1:
        print("Too many invalid attempts. Exiting")
        exit(1)

greetings = ["Hello, {}!", "Yo {} wassup?", "Beannachtaí, {}"]
selected_greeting = random.choice(greetings)
formatted_greeting = selected_greeting.format(user_name)
print(formatted_greeting)