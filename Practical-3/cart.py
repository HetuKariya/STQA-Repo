def apply_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)

def cart_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total

def apply_coupon(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def shipping_cost(total):
    if total >= 500:
        return 0
    return 50

def item_count(items):
    return sum(item["qty"] for item in items)

def is_eligible_for_bulk(item):
    return item["qty"] >= 10

def final_bill(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, 2)