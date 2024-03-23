def calculate_total_price(quantity, customer_type):
    # Giá mỗi sản phẩm
    unit_price = 10
    
    # Tính tổng tiền trước khi áp dụng chiết khấu
    total_price = quantity * unit_price
    
    # Áp dụng chiết khấu cho số lượng sản phẩm mua
    if 10 <= quantity <= 20:
        discount = 0.05
    elif quantity > 20:
        discount = 0.1
    else:
        discount = 0
    
    # Áp dụng chiết khấu cho loại khách hàng
    if customer_type == "Khách VIP":
        discount += 0.1
    
    # Tính tổng tiền sau khi áp dụng chiết khấu
    total_price -= total_price * discount
    
    return total_price

# Test cases
test_cases = [
    (5, "Khách thường"),   # Số lượng sản phẩm ít hơn 10, khách hàng thường
    (15, "Khách thường"),  # Số lượng sản phẩm từ 10-20, khách hàng thường
    (25, "Khách thường"),  # Số lượng sản phẩm lớn hơn 20, khách hàng thường
    (8, "Khách VIP"),      # Số lượng sản phẩm ít hơn 10, khách hàng VIP
    (18, "Khách VIP"),     # Số lượng sản phẩm từ 10-20, khách hàng VIP
    (30, "Khách VIP")      # Số lượng sản phẩm lớn hơn 20, khách hàng VIP
]

# Kiểm thử các test case và in kết quả
for quantity, customer_type in test_cases:
    total_price = calculate_total_price(quantity, customer_type)
    print(f"Số lượng sản phẩm: {quantity}, Loại khách hàng: {customer_type}, Tổng tiền: ${total_price}")