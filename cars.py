from db import get_connection

def add_car(franchise_id):
    print("\n=== Add Car ===")
    brand = input("Brand (e.g. Maruti, Honda): ")
    model = input("Model (e.g. Swift, City): ")
    price = input("Price: ")
    color = input("Color: ")
    year = input("Year: ")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO cars (franchise_id, brand, model, price, color, year) VALUES (%s, %s, %s, %s, %s, %s)",
        (franchise_id, brand, model, price, color, year)
    )
    conn.commit()
    conn.close()
    print(f"\n✅ {brand} {model} added successfully!")

def view_cars(franchise_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cars WHERE franchise_id = %s AND sold = FALSE", (franchise_id,))
    cars = cursor.fetchall()
    conn.close()
    
    print("\n=== Available Cars ===")
    if not cars:
        print("No cars available!")
        return
    
    for car in cars:
        print(f"{car['id']}. {car['brand']} {car['model']} | {car['color']} | {car['year']} | ₹{car['price']}")