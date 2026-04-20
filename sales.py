sales = []

def sell_car(franchise_id):
    from cars import cars
    from customers import customers
    
    print("\n=== Sell Car ===")
    
    available_cars = [c for c in cars if c["franchise_id"] == franchise_id and not c["sold"]]
    if not available_cars:
        print("No cars available!")
        return
    
    print("\nAvailable Cars:")
    for car in available_cars:
        print(f"{car['id']}. {car['brand']} {car['model']} | ₹{car['price']}")
    
    car_id = int(input("\nSelect Car ID: "))
    
    franchise_customers = [c for c in customers if c["franchise_id"] == franchise_id]
    if not franchise_customers:
        print("No customers found! Add customer first.")
        return
    
    print("\nCustomers:")
    for c in franchise_customers:
        print(f"{c['id']}. {c['name']} | {c['phone']}")
    
    customer_id = int(input("\nSelect Customer ID: "))
    
    car = next((c for c in cars if c["id"] == car_id), None)
    customer = next((c for c in customers if c["id"] == customer_id), None)
    
    if car and customer:
        car["sold"] = True
        sale = {
            "id": len(sales) + 1,
            "franchise_id": franchise_id,
            "car": f"{car['brand']} {car['model']}",
            "customer": customer["name"],
            "price": car["price"]
        }
        sales.append(sale)
        print(f"\n✅ {car['brand']} {car['model']} sold to {customer['name']}!")

def view_sales(franchise_id):
    print("\n=== Sales History ===")
    franchise_sales = [s for s in sales if s["franchise_id"] == franchise_id]
    
    if not franchise_sales:
        print("No sales yet!")
        return
    
    for s in franchise_sales:
        print(f"{s['id']}. {s['car']} | {s['customer']} | ₹{s['price']}")