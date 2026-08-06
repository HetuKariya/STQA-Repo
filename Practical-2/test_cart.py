import pytest
from cart import (
    apply_discount, cart_total, apply_coupon,
    shipping_cost, item_count, is_eligible_for_bulk, final_bill
)

class TestApplyDiscount:
    def test_zero_discount(self):
        assert apply_discount(200, 0) == 200.0

    def test_full_discount(self):
        assert apply_discount(200, 100) == 0.0

    def test_10_percent(self):
        assert apply_discount(500, 10) == 450.0

    def test_50_percent(self):
        assert apply_discount(300, 50) == 150.0

    def test_negative_discount_raises(self):
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            apply_discount(100, -1)

    def test_over_100_raises(self):
        with pytest.raises(ValueError, match="Discount must be between 0 and 100"):
            apply_discount(100, 101)

    def test_boundary_0_valid(self):
        assert apply_discount(100, 0) == 100.0

    def test_boundary_100_valid(self):
        assert apply_discount(100, 100) == 0.0

class TestCartTotal:
    def test_single_item(self):
        items = [{"price": 100, "qty": 2}]
        assert cart_total(items) == 200

    def test_multiple_items(self):
        items = [
            {"price": 50, "qty": 3},
            {"price": 200, "qty": 1},
        ]
        assert cart_total(items) == 350

    def test_empty_cart(self):
        assert cart_total([]) == 0

    def test_qty_one(self):
        items = [{"price": 99, "qty": 1}]
        assert cart_total(items) == 99

    def test_large_qty(self):
        items = [{"price": 10, "qty": 100}]
        assert cart_total(items) == 1000

class TestApplyCoupon:
    def test_SAVE10(self):
        assert apply_coupon(200, "SAVE10") == 180.0

    def test_SAVE20(self):
        assert apply_coupon(200, "SAVE20") == 160.0

    def test_HALFOFF(self):
        assert apply_coupon(200, "HALFOFF") == 100.0

    def test_invalid_coupon_raises(self):
        with pytest.raises(ValueError, match="Invalid coupon"):
            apply_coupon(200, "FAKE99")

    def test_coupon_on_zero_total(self):
        assert apply_coupon(0, "SAVE10") == 0.0

class TestShippingCost:
    def test_below_threshold(self):
        assert shipping_cost(499) == 50

    def test_at_threshold(self):
        assert shipping_cost(500) == 0

    def test_above_threshold(self):
        assert shipping_cost(1000) == 0

    def test_zero_total(self):
        assert shipping_cost(0) == 50

    def test_just_below_threshold(self):
        assert shipping_cost(499.99) == 50

class TestItemCount:
    def test_single_item(self):
        assert item_count([{"price": 10, "qty": 5}]) == 5

    def test_multiple_items(self):
        items = [{"price": 10, "qty": 3}, {"price": 20, "qty": 7}]
        assert item_count(items) == 10

    def test_empty(self):
        assert item_count([]) == 0

class TestIsEligibleForBulk:
    def test_exactly_10(self):
        assert is_eligible_for_bulk({"price": 5, "qty": 10}) is True

    def test_above_10(self):
        assert is_eligible_for_bulk({"price": 5, "qty": 15}) is True

    def test_below_10(self):
        assert is_eligible_for_bulk({"price": 5, "qty": 9}) is False

    def test_qty_1(self):
        assert is_eligible_for_bulk({"price": 5, "qty": 1}) is False

class TestFinalBill:
    def test_no_coupon_below_shipping_threshold(self):
        items = [{"price": 100, "qty": 2}]
        assert final_bill(items) == 250.0

    def test_no_coupon_above_shipping_threshold(self):
        items = [{"price": 200, "qty": 3}]
        assert final_bill(items) == 600.0

    def test_with_coupon_still_below_threshold(self):
        items = [{"price": 200, "qty": 2}]
        assert final_bill(items, "SAVE10") == 410.0

    def test_with_coupon_pushes_below_threshold(self):
        items = [{"price": 200, "qty": 3}]
        assert final_bill(items, "HALFOFF") == 350.0

    def test_with_coupon_stays_above_threshold(self):
        items = [{"price": 500, "qty": 2}]
        assert final_bill(items, "SAVE10") == 900.0

    def test_empty_cart_no_coupon(self):
        assert final_bill([]) == 50.0