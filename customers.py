customers = []

def add_customer(franchise_id):
    print("\n=== Add Customer ===")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    customer = {
        "id": len(customers) + 1,
        "franchise_id": franchise_id,
        "name": name,
        "phone": phone,
        "email": email
    }
    customers.append(customer)
    print(f"\n Customer {name} added successfully!")

def view_customers(franchise_id):
    print("\n=== Customers ===")
    franchise_customers = [c for c in customers if c["franchise_id"] == franchise_id]
    
    if not franchise_customers:
        print("No customers found!")
        return
    
    for c in franchise_customers:
        print(f"{c['id']}. {c['name']} | {c['phone']} | {c['email']}")