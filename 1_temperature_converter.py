def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / (9/5)
    return celsius

def km_to_miles(km):
    miles = km * 0.621371
    return miles

# Test the function
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-40))

print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(68))
print(fahrenheit_to_celsius(212))

print(km_to_miles(100))