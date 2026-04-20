cars = []

def add_car(franchise_id):
    print("\n=== Add Car ===")
    brand = input("Brand (e.g. Maruti, Honda): ")
    model = input("Model (e.g. Swift, City): ")
    price = input("Price: ")
    color = input("Color: ")
    year = input("Year: ")
    
    car = {
        "id": len(cars) + 1,
        "franchise_id": franchise_id,
        "brand": brand,
        "model": model,
        "price": price,
        "color": color,
        "year": year,
        "sold": False
    }
    cars.append(car)
    print(f"\n {brand} {model} added successfully!")

def view_cars(franchise_id):
    print("\n=== Available Cars ===")
    franchise_cars = [c for c in cars if c["franchise_id"] == franchise_id and not c["sold"]]
    
    if not franchise_cars:
        print("No cars available!")
        return
    
    for car in franchise_cars:
        print(f"{car['id']}. {car['brand']} {car['model']} | {car['color']} | {car['year']} | ₹{car['price']}")