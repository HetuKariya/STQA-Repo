

from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_apply_discount__mutmut: MutantDict = {}  # type: ignore
@_mutmut_mutated(mutants_x_apply_discount__mutmut)
def apply_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_orig(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_1(price, percent):
    if percent < 0 and percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_2(price, percent):
    if percent <= 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_3(price, percent):
    if percent < 1 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_4(price, percent):
    if percent < 0 or percent >= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_5(price, percent):
    if percent < 0 or percent > 101:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_6(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError(None)
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_7(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("XXDiscount must be between 0 and 100XX")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_8(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("discount must be between 0 and 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_9(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("DISCOUNT MUST BE BETWEEN 0 AND 100")
    return price * (1 - percent / 100)
def x_apply_discount__mutmut_10(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price / (1 - percent / 100)
def x_apply_discount__mutmut_11(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 + percent / 100)
def x_apply_discount__mutmut_12(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (2 - percent / 100)
def x_apply_discount__mutmut_13(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent * 100)
def x_apply_discount__mutmut_14(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - percent / 101)

mutants_x_apply_discount__mutmut['_mutmut_orig'] = x_apply_discount__mutmut_orig # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_1'] = x_apply_discount__mutmut_1 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_2'] = x_apply_discount__mutmut_2 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_3'] = x_apply_discount__mutmut_3 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_4'] = x_apply_discount__mutmut_4 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_5'] = x_apply_discount__mutmut_5 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_6'] = x_apply_discount__mutmut_6 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_7'] = x_apply_discount__mutmut_7 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_8'] = x_apply_discount__mutmut_8 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_9'] = x_apply_discount__mutmut_9 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_10'] = x_apply_discount__mutmut_10 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_11'] = x_apply_discount__mutmut_11 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_12'] = x_apply_discount__mutmut_12 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_13'] = x_apply_discount__mutmut_13 # type: ignore # mutmut generated
mutants_x_apply_discount__mutmut['x_apply_discount__mutmut_14'] = x_apply_discount__mutmut_14 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_cart_total__mutmut)
def cart_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total

def x_cart_total__mutmut_orig(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total

def x_cart_total__mutmut_1(items):
    total = None
    for item in items:
        total += item["price"] * item["qty"]
    return total

def x_cart_total__mutmut_2(items):
    total = 1
    for item in items:
        total += item["price"] * item["qty"]
    return total

def x_cart_total__mutmut_3(items):
    total = 0
    for item in items:
        total = item["price"] * item["qty"]
    return total

def x_cart_total__mutmut_4(items):
    total = 0
    for item in items:
        total -= item["price"] * item["qty"]
    return total

def x_cart_total__mutmut_5(items):
    total = 0
    for item in items:
        total += item["price"] / item["qty"]
    return total

def x_cart_total__mutmut_6(items):
    total = 0
    for item in items:
        total += item["XXpriceXX"] * item["qty"]
    return total

def x_cart_total__mutmut_7(items):
    total = 0
    for item in items:
        total += item["PRICE"] * item["qty"]
    return total

def x_cart_total__mutmut_8(items):
    total = 0
    for item in items:
        total += item["price"] * item["XXqtyXX"]
    return total

def x_cart_total__mutmut_9(items):
    total = 0
    for item in items:
        total += item["price"] * item["QTY"]
    return total

mutants_x_cart_total__mutmut['_mutmut_orig'] = x_cart_total__mutmut_orig # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_1'] = x_cart_total__mutmut_1 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_2'] = x_cart_total__mutmut_2 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_3'] = x_cart_total__mutmut_3 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_4'] = x_cart_total__mutmut_4 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_5'] = x_cart_total__mutmut_5 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_6'] = x_cart_total__mutmut_6 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_7'] = x_cart_total__mutmut_7 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_8'] = x_cart_total__mutmut_8 # type: ignore # mutmut generated
mutants_x_cart_total__mutmut['x_cart_total__mutmut_9'] = x_cart_total__mutmut_9 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_apply_coupon__mutmut)
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

def x_apply_coupon__mutmut_orig(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_1(total, coupon_code):
    coupons = None
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_2(total, coupon_code):
    coupons = {
        "XXSAVE10XX": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_3(total, coupon_code):
    coupons = {
        "save10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_4(total, coupon_code):
    coupons = {
        "SAVE10": 11,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_5(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "XXSAVE20XX": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_6(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "save20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_7(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 21,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_8(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "XXHALFOFFXX": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_9(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "halfoff": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_10(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 51,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_11(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_12(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(None)
    discount = coupons[coupon_code]
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_13(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = None
    return apply_discount(total, discount)

def x_apply_coupon__mutmut_14(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(None, discount)

def x_apply_coupon__mutmut_15(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, None)

def x_apply_coupon__mutmut_16(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(discount)

def x_apply_coupon__mutmut_17(total, coupon_code):
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "HALFOFF": 50,
    }
    if coupon_code not in coupons:
        raise ValueError(f"Invalid coupon: {coupon_code}")
    discount = coupons[coupon_code]
    return apply_discount(total, )

mutants_x_apply_coupon__mutmut['_mutmut_orig'] = x_apply_coupon__mutmut_orig # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_1'] = x_apply_coupon__mutmut_1 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_2'] = x_apply_coupon__mutmut_2 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_3'] = x_apply_coupon__mutmut_3 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_4'] = x_apply_coupon__mutmut_4 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_5'] = x_apply_coupon__mutmut_5 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_6'] = x_apply_coupon__mutmut_6 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_7'] = x_apply_coupon__mutmut_7 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_8'] = x_apply_coupon__mutmut_8 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_9'] = x_apply_coupon__mutmut_9 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_10'] = x_apply_coupon__mutmut_10 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_11'] = x_apply_coupon__mutmut_11 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_12'] = x_apply_coupon__mutmut_12 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_13'] = x_apply_coupon__mutmut_13 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_14'] = x_apply_coupon__mutmut_14 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_15'] = x_apply_coupon__mutmut_15 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_16'] = x_apply_coupon__mutmut_16 # type: ignore # mutmut generated
mutants_x_apply_coupon__mutmut['x_apply_coupon__mutmut_17'] = x_apply_coupon__mutmut_17 # type: ignore # mutmut generated
mutants_x_shipping_cost__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_shipping_cost__mutmut)
def shipping_cost(total):
    if total >= 500:
        return 0
    return 50

def x_shipping_cost__mutmut_orig(total):
    if total >= 500:
        return 0
    return 50

def x_shipping_cost__mutmut_1(total):
    if total > 500:
        return 0
    return 50

def x_shipping_cost__mutmut_2(total):
    if total >= 501:
        return 0
    return 50

def x_shipping_cost__mutmut_3(total):
    if total >= 500:
        return 1
    return 50

def x_shipping_cost__mutmut_4(total):
    if total >= 500:
        return 0
    return 51

mutants_x_shipping_cost__mutmut['_mutmut_orig'] = x_shipping_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x_shipping_cost__mutmut['x_shipping_cost__mutmut_1'] = x_shipping_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x_shipping_cost__mutmut['x_shipping_cost__mutmut_2'] = x_shipping_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x_shipping_cost__mutmut['x_shipping_cost__mutmut_3'] = x_shipping_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x_shipping_cost__mutmut['x_shipping_cost__mutmut_4'] = x_shipping_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x_item_count__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_item_count__mutmut)
def item_count(items):
    return sum(item["qty"] for item in items)

def x_item_count__mutmut_orig(items):
    return sum(item["qty"] for item in items)

def x_item_count__mutmut_1(items):
    return sum(None)

def x_item_count__mutmut_2(items):
    return sum(item["XXqtyXX"] for item in items)

def x_item_count__mutmut_3(items):
    return sum(item["QTY"] for item in items)

mutants_x_item_count__mutmut['_mutmut_orig'] = x_item_count__mutmut_orig # type: ignore # mutmut generated
mutants_x_item_count__mutmut['x_item_count__mutmut_1'] = x_item_count__mutmut_1 # type: ignore # mutmut generated
mutants_x_item_count__mutmut['x_item_count__mutmut_2'] = x_item_count__mutmut_2 # type: ignore # mutmut generated
mutants_x_item_count__mutmut['x_item_count__mutmut_3'] = x_item_count__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_eligible_for_bulk__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_is_eligible_for_bulk__mutmut)
def is_eligible_for_bulk(item):
    return item["qty"] >= 10

def x_is_eligible_for_bulk__mutmut_orig(item):
    return item["qty"] >= 10

def x_is_eligible_for_bulk__mutmut_1(item):
    return item["XXqtyXX"] >= 10

def x_is_eligible_for_bulk__mutmut_2(item):
    return item["QTY"] >= 10

def x_is_eligible_for_bulk__mutmut_3(item):
    return item["qty"] > 10

def x_is_eligible_for_bulk__mutmut_4(item):
    return item["qty"] >= 11

mutants_x_is_eligible_for_bulk__mutmut['_mutmut_orig'] = x_is_eligible_for_bulk__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_eligible_for_bulk__mutmut['x_is_eligible_for_bulk__mutmut_1'] = x_is_eligible_for_bulk__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_eligible_for_bulk__mutmut['x_is_eligible_for_bulk__mutmut_2'] = x_is_eligible_for_bulk__mutmut_2 # type: ignore # mutmut generated
mutants_x_is_eligible_for_bulk__mutmut['x_is_eligible_for_bulk__mutmut_3'] = x_is_eligible_for_bulk__mutmut_3 # type: ignore # mutmut generated
mutants_x_is_eligible_for_bulk__mutmut['x_is_eligible_for_bulk__mutmut_4'] = x_is_eligible_for_bulk__mutmut_4 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_final_bill__mutmut)
def final_bill(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_orig(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_1(items, coupon_code=None):
    total = None
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_2(items, coupon_code=None):
    total = cart_total(None)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_3(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = None
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_4(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(None, coupon_code)
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_5(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, None)
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_6(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(coupon_code)
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_7(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, )
    total += shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_8(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total = shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_9(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total -= shipping_cost(total)
    return round(total, 2)

def x_final_bill__mutmut_10(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(None)
    return round(total, 2)

def x_final_bill__mutmut_11(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(None, 2)

def x_final_bill__mutmut_12(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, None)

def x_final_bill__mutmut_13(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(2)

def x_final_bill__mutmut_14(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, )

def x_final_bill__mutmut_15(items, coupon_code=None):
    total = cart_total(items)
    if coupon_code:
        total = apply_coupon(total, coupon_code)
    total += shipping_cost(total)
    return round(total, 3)

mutants_x_final_bill__mutmut['_mutmut_orig'] = x_final_bill__mutmut_orig # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_1'] = x_final_bill__mutmut_1 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_2'] = x_final_bill__mutmut_2 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_3'] = x_final_bill__mutmut_3 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_4'] = x_final_bill__mutmut_4 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_5'] = x_final_bill__mutmut_5 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_6'] = x_final_bill__mutmut_6 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_7'] = x_final_bill__mutmut_7 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_8'] = x_final_bill__mutmut_8 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_9'] = x_final_bill__mutmut_9 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_10'] = x_final_bill__mutmut_10 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_11'] = x_final_bill__mutmut_11 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_12'] = x_final_bill__mutmut_12 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_13'] = x_final_bill__mutmut_13 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_14'] = x_final_bill__mutmut_14 # type: ignore # mutmut generated
mutants_x_final_bill__mutmut['x_final_bill__mutmut_15'] = x_final_bill__mutmut_15 # type: ignore # mutmut generated