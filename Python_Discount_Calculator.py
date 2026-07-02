def apply_discount(price, discount):
    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return "The price should be a number"
    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The discount should be a number"
    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    final_price = price - (price * discount / 100)
    return final_price
# Test cases
print(apply_discount(100, 20))        
print(apply_discount(200, 50))        
print(apply_discount(50, 0))          
print(apply_discount(50, 100))        
print(apply_discount(74.5, 20.0))     
# Error cases
print(apply_discount("50", 20))       
print(apply_discount(50, "20"))       
print(apply_discount(-10, 20))        
print(apply_discount(50, 150))        