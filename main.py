from db import get_connection
from franchise import get_all_franchises, add_franchise
from cars import add_car, view_cars
from customers import add_customer, view_customers
from sales import sell_car, view_sales

def select_franchise():
    franchises = get_all_franchises()
    
    if not franchises:
        print("\nNo franchises found!")
        print("Adding default franchises...")
        add_franchise("AutoVault Amritsar", "Amritsar")
        add_franchise("AutoVault Ludhiana", "Ludhiana")
        add_franchise("AutoVault Delhi", "Delhi")
        franchises = get_all_franchises()
    
    print("\n=== Welcome to AutoVault ===")
    print("Available Franchises:")
    for f in franchises:
        print(f"{f['id']}. {f['name']} - {f['city']}")
    
    choice = int(input("\nSelect Franchise: "))
    selected = next(f for f in franchises if f['id'] == choice)
    print(f"\n✅ {selected['name']} selected!")
    return selected

def main_menu():
    global selected_franchise
    while True:
        print(f"\n=== {selected_franchise['name']} ===")
        print("1. Add Car")
        print("2. View Cars")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Sell Car")
        print("6. View Sales")
        print("7. Switch Franchise")
        print("8. Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            add_car(selected_franchise['id'])
        elif choice == "2":
            view_cars(selected_franchise['id'])
        elif choice == "3":
            add_customer(selected_franchise['id'])
        elif choice == "4":
            view_customers(selected_franchise['id'])
        elif choice == "5":
            sell_car(selected_franchise['id'])
        elif choice == "6":
            view_sales(selected_franchise['id'])
        elif choice == "7":
            selected_franchise = select_franchise()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

selected_franchise = select_franchise()
main_menu()