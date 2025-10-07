##Activity 1: 

#Predict) 1) 32
        2) 48
        3) 212

#Run)1 and 3 were right while i was wrong for 2, the correct answer being 68

#Investigate) it just returns the same value when a negative number is used

#Modify)
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / (9/5)
    return celsius

    def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / (9/5)
    return celsius

#Make)
def km_to_miles(km):
    miles = km * 0.621371
    return miles
print(km_to_miles(100))

##Activity 2:

Predict) 
    1) 120.00
    2) 110.00
    3) 97.20

Run) 
output:
£120.00
£110.00
£97.20
# my predicitions were correct in terms of the values however i  did not add the "£" to each of the values

Investigate)
    1) this parameter is the basline tax rate, it will remain 0.2 unless it is overidden by a new value when entering the parameters
    2) no discount is applied
    3) ensures that the value only features 2 decimal values at most, it will round up or down to the nearest second decimal place in the scenario where the value features more than 2 decimal places

Modify)
def calculate_total(price, tax_rate=0.20, discount=0, tip_rate+0.12):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax
    total += total * tip_rate
    return total

Make)
THIS IS A SHOPPING CALCULATOR NOT A ASSIGNMENT GRADER??

also i have no idea what that request means

Activity 3)
Run) 
    "hello" will score low as it only meets one of the scoring conditions
    "Hello123" will score score very high as it has a capital, a lower case, a digit and it is 8 charcaters minimum
    "HELLO" will score low for the same reasons as "hello"
    "MyPass123!" will score high for the same reasons as "Hello123"

Investigate)
    1) any() checks all of the characters in the string for a certain conditon that can be specified by the coder, in this case it is to check for any upper or lower case words and any digits so that it can be scored appropriately 
    2) for .isupper(), .islower(), isdigit(), check for upper case, lower case and digits respectively and if there is one present, it will return a True output
    

