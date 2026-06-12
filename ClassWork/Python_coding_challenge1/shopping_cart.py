def total_cart_value(cart):
    print("Total Cart Value: ₹", sum(cart))


def expensive_cheapest(cart):
    print("\nMost Expensive Product: ₹", max(cart))
    print("Cheapest Product: ₹", min(cart))


def premium_shipping(cart):
    count = 0

    for price in cart:
        if price > 1000:
            count += 1

    print("\nPremium Shipping Eligible Products:", count)


def discount_products(cart):
    discount = []

    for price in cart:
        if price > 1500:
            discount.append(price)

    print("\nDiscount Eligible Products:")
    print(discount)


def average_price(cart):
    avg = sum(cart) / len(cart)
    print("\nAverage Product Price: ₹", round(avg, 2))


cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

total_cart_value(cart)
expensive_cheapest(cart)
premium_shipping(cart)
discount_products(cart)
average_price(cart)