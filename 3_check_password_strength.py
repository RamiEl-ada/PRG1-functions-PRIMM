import random
import string

def score_rating(score):
    rating = "No Rating"
    if score <= 2:
        rating = "Weak Rating"
    elif score == 3:
        rating = "Medium Rating"
    elif score <= 5:
        rating = "Strong Rating"
    return rating

def check_string(password):
    for pwd in password:
        if pwd in string.punctuation:
            return True 

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain uppercase letters")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain lowercase letters")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain numbers")
    if check_string(password) == True:
        score += 1
    else:
        feedback.append("Password should contain a Special Character")
    return score, feedback

def random_password_generator():
    random_password = ""
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    special_characters = string.punctuation
    numbers = "1234567890"
    all_chars = numbers + special_characters + letters
    random_password += random.choice(letters[:25]) + random.choice(letters[25:]) + random.choice(numbers) + random.choice(special_characters)
    for i in range(4):
        random_password += random.choice(all_chars)
    return random_password
# Test passwords
random_password = random_password_generator()
passwords = ["hello", "Hello123", "PASSWORD", "MyPass123!", "hello!", random_password]
for pwd in passwords:
    score, issues = check_password_strength(pwd)
    rating = score_rating(score)
    print(f"'{pwd}': Score {score}/5", "You got a", rating)
    for issue in issues:
        print(f"  - {issue}")
