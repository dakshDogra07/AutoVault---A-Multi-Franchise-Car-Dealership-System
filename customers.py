from db import get_connection

def add_customer(franchise_id):
    print("\n=== Add Customer ===")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (franchise_id, name, phone, email) VALUES (%s, %s, %s, %s)",
        (franchise_id, name, phone, email)
    )
    conn.commit()
    conn.close()
    print(f"\n✅ Customer {name} added successfully!")

def view_customers(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers WHERE franchise_id = %s", (franchise_id,))
    customers = cursor.fetchall()
    conn.close()
    
    print("\n=== Customers ===")
    if not customers:
        print("No customers found!")
        return
    
    for c in customers:
        print(f"{c['id']}. {c['name']} | {c['phone']} | {c['email']}")