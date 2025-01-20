# Step 1: Define the add_to_cart function
def add_to_cart(cart, item_name, price, *args, **kwargs):
    # Check if item is already in the cart
    for item in cart:
        if item['name'] == item_name:
            print(f"{item_name} is already in the cart!")
            return cart

    # Apply discounts if any m
    discount = sum(args) if args else 0
    final_price = price * (1 - discount / 100)

    # Add the item to the cart
    item = {
        'name': item_name,
        'final_price': round(final_price, 2),
        'details': kwargs
    }
    cart.append(item)
    print(f"Item added: {item_name} - Final Price: ${item['final_price']}")
    return cart


# Step 2: Create an empty cart
cart = []

# Step 3: Input loop for adding items
while True:
    # Input item name
    item_name = input("Enter item name (or 'done' to finish): ").strip()
    if item_name.lower() == 'done':
        break

    # Input price
    try:
        price = float(input("Enter item price: "))
    except ValueError:
        print("Invalid price. Please try again.")
        continue

    # Input discounts
    discounts = input("Enter discounts (if any, separated by spaces): ").strip()
    discount_values = [float(d) for d in discounts.split()] if discounts else []

    # Input additional details
    details_input = input("Enter item details (e.g., color=red size=large): ").strip()
    details = dict(item.split('=') for item in details_input.split() if '=' in item)

    # Add the item to the cart
    cart = add_to_cart(cart, item_name, price, *discount_values, **details)

# Step 4: Display the cart summary
if cart:
    print("\n--- Cart Summary ---")
    total_cost = 0
    for item in cart:
        details = ", ".join([f"{key}={value}" for key, value in item['details'].items()])
        print(f"{item['name']} - ${item['final_price']} ({details})")
        total_cost += item['final_price']
    print(f"Total Cost: ${total_cost}")
else:
    print("Your cart is empty!")
