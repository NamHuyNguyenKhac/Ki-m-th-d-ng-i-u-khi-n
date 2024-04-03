def calculate_total_price(quantity, customer_type):
    # Check quantity là int và customer_type là bool
    if not isinstance(quantity, int) or not isinstance(customer_type, bool):
        return None
    
    if quantity <= 0:
        return None
    # Tính tổng tiền trước khi áp dụng chiết khấu
    total_price = quantity * 10
    
    # Áp dụng chiết khấu cho số lượng sản phẩm mua
    if 10 <= quantity <= 20:
        discount = 0.05
    elif quantity > 20:
        discount = 0.1
    else:
        discount = 0
    
    # Áp dụng chiết khấu cho loại khách hàng
    if customer_type == True:
        discount += 0.1
    
    # Tính tổng tiền sau khi áp dụng chiết khấu
    total_price -= total_price * discount
    
    return total_price

# Test cases
test_cases_table = [
    (True, 21),     # Biến đầu vào k hợp lệ
    (0, False),     # Số lượng sản phẩn <= 0, Khách thường
    (5, False),     # Số lượng sản phẩm từ 5-10, khách hàng thường
    (15, False),    # Số lượng sản phẩm từ 10-20, khách hàng thường
    (25, False),    # Số lượng sản phẩm hơn 20, khách hàng thường
    (-1, True),     # Số lượng sản phẩn <= 0, Khách VIP
    (4, True),      # Số lượng sản phẩm 5-10, khách hàng VIP
    (14, True),     # Số lượng sản phẩm 10-20, khách hàng VIP
    (24, True),     # Số lượng sản phẩm lớn hơn 20, khách hàng VIP
]

# Kiểm thử các test case và in kết quả
for i, (quantity, customer_type) in enumerate(test_cases_table, start=1):
    total_price = calculate_total_price(quantity, customer_type)
    if total_price is None:
        print(f"Test Case R{i}: Invalid input: Quantity={quantity}, CustomerType={customer_type}")
    else:
        print(f"Test Case R{i}: Quantity: {quantity}, CustomerType: {customer_type}, Total Price: ${total_price}")
