from db import get_connection

def sell_car(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM cars WHERE franchise_id = %s AND sold = FALSE", (franchise_id,))
    cars = cursor.fetchall()
    
    if not cars:
        print("\nNo cars available!")
        conn.close()
        return
    
    print("\n=== Available Cars ===")
    for car in cars:
        print(f"{car['id']}. {car['brand']} {car['model']} | ₹{car['price']}")
    
    car_id = int(input("\nSelect Car ID: "))
    
    cursor.execute("SELECT * FROM customers WHERE franchise_id = %s", (franchise_id,))
    customers = cursor.fetchall()
    
    if not customers:
        print("\nNo customers found! Add customer first.")
        conn.close()
        return
    
    print("\n=== Customers ===")
    for c in customers:
        print(f"{c['id']}. {c['name']} | {c['phone']}")
    
    customer_id = int(input("\nSelect Customer ID: "))
    
    cursor.execute("SELECT price FROM cars WHERE id = %s", (car_id,))
    car = cursor.fetchone()
    
    cursor.execute("UPDATE cars SET sold = TRUE WHERE id = %s", (car_id,))
    cursor.execute(
        "INSERT INTO sales (franchise_id, car_id, customer_id, price) VALUES (%s, %s, %s, %s)",
        (franchise_id, car_id, customer_id, car['price'])
    )
    conn.commit()
    conn.close()
    print(f"\n✅ Car sold successfully!")

def view_sales(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.id, c.brand, c.model, cu.name, s.price, s.sale_date 
        FROM sales s
        JOIN cars c ON s.car_id = c.id
        JOIN customers cu ON s.customer_id = cu.id
        WHERE s.franchise_id = %s
    """, (franchise_id,))
    sales = cursor.fetchall()
    conn.close()
    
    print("\n=== Sales History ===")
    if not sales:
        print("No sales yet!")
        return
    
    for s in sales:
        print(f"{s['id']}. {s['brand']} {s['model']} | {s['name']} | ₹{s['price']} | {s['sale_date']}")