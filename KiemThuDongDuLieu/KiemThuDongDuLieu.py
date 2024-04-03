def cal(quantity, type):
    if not isinstance(quantity, int) or not isinstance(type, bool) or quantity <= 0:
        return None
    total_price = quantity * 5
    if quantity > 10:
        total_price = total_price - 10
    if type == True:
        total_price = total_price - 5
    return total_price

# Test cases
test_cases = [
    (3, True),   # 1 – 2 – 3F – 5T – 6 – 7
    (3, False),  # 1 – 2 – 3F – 5F – 7
    (14, True),  # 1 – 2 – 3T – 4 – 5T – 6 – 7
    (12, False)  # 1 – 2 – 3T – 4 – 5F – 7
]

print("Kiểm thử all use")
# Kiểm thử các test case và in kết quả
for i, (quantity, type) in enumerate(test_cases, start=1):
    total_price = cal(quantity, type)
    if total_price is None:
        print(f"Test Case {i}: Invalid input!")
    else:
        print(f"Test Case {i}: Total Price: ${total_price}")

