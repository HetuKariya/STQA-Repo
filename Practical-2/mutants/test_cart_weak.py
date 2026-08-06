import pytest
from cart import (
    apply_discount, cart_total, apply_coupon,
    shipping_cost, item_count, is_eligible_for_bulk, final_bill
)

class TestApplyDiscount:
    def test_returns_something(self):
        result = apply_discount(200, 10)
        assert result is not None  

    def test_raises_on_negative(self):
        with pytest.raises(ValueError):  
            apply_discount(100, -5)

class TestCartTotal:
    def test_empty_cart(self):
        assert cart_total([]) == 0

    def test_total_is_positive(self):
        items = [{"price": 50, "qty": 2}]
        assert cart_total(items) > 0 

class TestApplyCoupon:
    def test_SAVE10_reduces_total(self):
        result = apply_coupon(200, "SAVE10")
        assert result < 200

    def test_invalid_raises(self):
        with pytest.raises(ValueError): 
            apply_coupon(200, "BOGUS")

class TestShippingCost:
    def test_high_total_free(self):
        assert shipping_cost(1000) == 0

    def test_low_total_paid(self):
        assert shipping_cost(100) == 50

class TestItemCount:
    def test_single(self):
        assert item_count([{"price": 10, "qty": 3}]) == 3

class TestIsEligibleForBulk:
    def test_large_qty(self):
        assert is_eligible_for_bulk({"price": 5, "qty": 20}) is True

    def test_small_qty(self):
        assert is_eligible_for_bulk({"price": 5, "qty": 3}) is False

class TestFinalBill:
    def test_returns_a_number(self):
        items = [{"price": 100, "qty": 2}]
        result = final_bill(items)
        assert isinstance(result, (int, float)) 

    def test_with_coupon_is_less_than_without(self):
        items = [{"price": 200, "qty": 2}]
        without = final_bill(items)
        with_coupon = final_bill(items, "SAVE10")
        assert with_coupon < without 