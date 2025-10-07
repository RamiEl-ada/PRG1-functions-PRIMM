def calculate_total(price, tax_rate=0.20, discount=0, tip_rate=0.12):
    subtotal = price - discount
    tax = subtotal * tax_rate
    total = subtotal + tax
    total += total * tip_rate
    return total

# Test cases
print(f"£{calculate_total(100):.2f}")
print(f"£{calculate_total(100, 0.1):.2f}")
print(f"£{calculate_total(100, 0.08, 10):.2f}")

