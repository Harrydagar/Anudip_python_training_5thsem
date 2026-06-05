# --- Step 1: Initialize the inventory dataset and tracking lists ---
stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock_count = 0
available_products_count = 0

restock_required = []
healthy_stock = []

# --- Step 2: Loop through each product's stock quantity ---
for quantity in stock:
    
    # 1. Check if the product is completely out of stock (quantity is 0)
    if quantity == 0:
        out_of_stock_count += 1
    else:
        # 3. If quantity is greater than 0, it counts as an available product type
        available_products_count += 1
        
    # 2. Check if a product needs restocking (quantity less than 10)
    # Note: 0 is less than 10, so out-of-stock items are naturally included here
    if quantity < 10:
        restock_required.append(quantity)
        
    # 4. Check for healthy stock levels (quantity >= 15)
    if quantity >= 15:
        healthy_stock.append(quantity)

# --- Step 3: Display the final inventory alerts ---
print(f"Out of Stock Products: {out_of_stock_count}")
print(f"Restock Required: {restock_required}")
print(f"Available Products: {available_products_count}")
print(f"Healthy Stock: {healthy_stock}")