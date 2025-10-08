import random
import string

def random_password_generator(length):

    random_password = ""
    upper_condition = False
    lower_condition = False
    number_condition = False
    special_condition = False
    numbers = [1,2,3,4,5,6,7,8,9,0]
    characters = (string.ascii_lowercase + string.ascii_uppercase + string.punctuation
                  + numbers)
    
    
    while (upper_condition is False or lower_condition is False
            or number_condition is False or special_condition is False):
        random_password = "".join(random.choice(characters)
                              for random_password in range(8))
        
        if (random_password.isupper()):
             upper_condition = True
        if (random_password.islower()):
             lower_condition = True
        if (random_password.isdigit()):
            number_condition = True
        if check_string(random_password) == True: 
             special_condition = True
        print(upper_condition, lower_condition, number_condition, special_condition)
             
    return random_password

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

# Test passwords

passwords = ["hello", "Hello123", "PASSWORD", "MyPass123!", "hello!"
             , random_password_generator(8)]
for pwd in passwords:
    score, issues = check_password_strength(pwd)
    rating = score_rating(score)
    print(f"'{pwd}': Score {score}/5", "You got a", rating)
    for issue in issues:
        print(f"  - {issue}")
    print()

