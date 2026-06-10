"""2. E-Commerce Inventory & Sales Dashboard
Problem Statement
An online store wants to manage products and sales.
Example Structure
products = { "P101": { "name": "Laptop", "price": 55000, "stock": 12, "sold": 25 } }
Maintain records of at least 30 products.
Requirements
1.
Display all products.
2.
Add a new product.
3.
Update stock after sales.
4.
Find out-of-stock products.
5.
Find products with stock less than 5.
6.
Calculate total inventory value.
7.
Find best-selling product.
8.
Find least-selling product.
9.
Calculate total revenue generated.
10.
Generate a low-stock report.
11.
Display products whose sales exceed the average sales.
12.
Create a dictionary of products eligible for promotion (sales < 10).
Challenge
Generate a complete business report."""
# ==========================================
# E-Commerce Inventory & Sales Dashboard
# ==========================================

products = {
"P101":{"name":"Laptop","price":55000,"stock":12,"sold":25},
"P102":{"name":"Mouse","price":500,"stock":20,"sold":40},
"P103":{"name":"Keyboard","price":1200,"stock":15,"sold":18},
"P104":{"name":"Monitor","price":12000,"stock":8,"sold":12},
"P105":{"name":"Printer","price":8000,"stock":4,"sold":9},
"P106":{"name":"Scanner","price":7000,"stock":3,"sold":6},
"P107":{"name":"Webcam","price":2500,"stock":10,"sold":14},
"P108":{"name":"Speaker","price":3000,"stock":5,"sold":11},
"P109":{"name":"Headphone","price":2000,"stock":7,"sold":22},
"P110":{"name":"SSD","price":4500,"stock":9,"sold":19},
"P111":{"name":"Hard Disk","price":5500,"stock":6,"sold":13},
"P112":{"name":"Pendrive","price":700,"stock":25,"sold":35},
"P113":{"name":"Router","price":2500,"stock":2,"sold":8},
"P114":{"name":"Smartwatch","price":5000,"stock":11,"sold":21},
"P115":{"name":"Tablet","price":18000,"stock":5,"sold":7},
"P116":{"name":"Mobile","price":25000,"stock":14,"sold":30},
"P117":{"name":"Power Bank","price":1500,"stock":16,"sold":28},
"P118":{"name":"Charger","price":800,"stock":18,"sold":26},
"P119":{"name":"Camera","price":35000,"stock":4,"sold":5},
"P120":{"name":"Tripod","price":2000,"stock":6,"sold":10},
"P121":{"name":"Microphone","price":4000,"stock":3,"sold":4},
"P122":{"name":"Projector","price":28000,"stock":2,"sold":3},
"P123":{"name":"Graphics Card","price":45000,"stock":5,"sold":15},
"P124":{"name":"Processor","price":22000,"stock":7,"sold":17},
"P125":{"name":"Motherboard","price":12000,"stock":8,"sold":16},
"P126":{"name":"RAM","price":3500,"stock":12,"sold":24},
"P127":{"name":"Cabinet","price":5000,"stock":9,"sold":11},
"P128":{"name":"UPS","price":6000,"stock":4,"sold":8},
"P129":{"name":"Cooling Fan","price":900,"stock":15,"sold":20},
"P130":{"name":"LAN Cable","price":300,"stock":30,"sold":50}
}

# ==========================================
# Functions
# ==========================================

def display_products():
    print("\nPRODUCT LIST")
    print("-"*80)

    for pid in products:
        p = products[pid]

        print(pid,
              p["name"],
              "Price:", p["price"],
              "Stock:", p["stock"],
              "Sold:", p["sold"])


def add_product():

    pid = input("Enter Product ID: ")

    if pid in products:
        print("Product already exists")
        return

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    sold = int(input("Enter Sold Quantity: "))

    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock,
        "sold": sold
    }

    print("Product Added Successfully")


def update_stock_after_sale():

    pid = input("Enter Product ID: ")

    if pid not in products:
        print("Product Not Found")
        return

    quantity = int(input("Quantity Sold: "))

    if quantity > products[pid]["stock"]:
        print("Not Enough Stock")
        return

    products[pid]["stock"] -= quantity
    products[pid]["sold"] += quantity

    print("Stock Updated Successfully")


def out_of_stock():

    print("\nOUT OF STOCK PRODUCTS")

    found = False

    for pid in products:
        if products[pid]["stock"] == 0:
            print(pid, products[pid]["name"])
            found = True

    if not found:
        print("No Out Of Stock Products")


def stock_less_than_five():

    print("\nSTOCK LESS THAN 5")

    for pid in products:

        if products[pid]["stock"] < 5:
            print(pid,
                  products[pid]["name"],
                  "Stock:",
                  products[pid]["stock"])


def inventory_value():

    total = 0

    for pid in products:

        total += (
            products[pid]["price"]
            * products[pid]["stock"]
        )

    print("\nTotal Inventory Value =", total)


def best_selling_product():

    best_id = ""
    max_sale = -1

    for pid in products:

        if products[pid]["sold"] > max_sale:

            max_sale = products[pid]["sold"]
            best_id = pid

    print("\nBEST SELLING PRODUCT")

    print(best_id,
          products[best_id]["name"],
          "Sold:",
          max_sale)


def least_selling_product():

    low_id = ""
    min_sale = 999999

    for pid in products:

        if products[pid]["sold"] < min_sale:

            min_sale = products[pid]["sold"]
            low_id = pid

    print("\nLEAST SELLING PRODUCT")

    print(low_id,
          products[low_id]["name"],
          "Sold:",
          min_sale)


def total_revenue():

    revenue = 0

    for pid in products:

        revenue += (
            products[pid]["price"]
            * products[pid]["sold"]
        )

    print("\nTOTAL REVENUE =", revenue)


def low_stock_report():

    print("\nLOW STOCK REPORT")
    print("-"*50)

    for pid in products:

        if products[pid]["stock"] < 5:

            print(pid,
                  products[pid]["name"],
                  "Stock:",
                  products[pid]["stock"])


def above_average_sales():

    total_sales = 0

    for pid in products:
        total_sales += products[pid]["sold"]

    avg_sales = total_sales / len(products)

    print("\nAverage Sales =", round(avg_sales,2))

    print("\nPRODUCTS ABOVE AVERAGE SALES")

    for pid in products:

        if products[pid]["sold"] > avg_sales:

            print(pid,
                  products[pid]["name"],
                  products[pid]["sold"])


def promotion_products():

    promo = {}

    for pid in products:

        if products[pid]["sold"] < 10:

            promo[pid] = products[pid]

    print("\nPROMOTION PRODUCTS")

    for pid in promo:

        print(pid,
              promo[pid]["name"],
              "Sold:",
              promo[pid]["sold"])


def business_report():

    print("\n")
    print("="*60)
    print("BUSINESS REPORT")
    print("="*60)

    inventory_value()
    total_revenue()
    best_selling_product()
    least_selling_product()

    total_stock = 0

    for pid in products:
        total_stock += products[pid]["stock"]

    print("\nTotal Products:", len(products))
    print("Total Stock Available:", total_stock)


# ==========================================
# Main Menu
# ==========================================

while True:

    print("\n")
    print("="*60)
    print("E-COMMERCE INVENTORY & SALES DASHBOARD")
    print("="*60)

    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock After Sale")
    print("4. Find Out Of Stock Products")
    print("5. Products With Stock Less Than 5")
    print("6. Calculate Inventory Value")
    print("7. Best Selling Product")
    print("8. Least Selling Product")
    print("9. Calculate Revenue")
    print("10. Low Stock Report")
    print("11. Products Above Average Sales")
    print("12. Promotion Products")
    print("13. Business Report")
    print("0. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_products()

    elif choice == "2":
        add_product()

    elif choice == "3":
        update_stock_after_sale()

    elif choice == "4":
        out_of_stock()

    elif choice == "5":
        stock_less_than_five()

    elif choice == "6":
        inventory_value()

    elif choice == "7":
        best_selling_product()

    elif choice == "8":
        least_selling_product()

    elif choice == "9":
        total_revenue()

    elif choice == "10":
        low_stock_report()

    elif choice == "11":
        above_average_sales()

    elif choice == "12":
        promotion_products()

    elif choice == "13":
        business_report()

    elif choice == "0":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")