# All Imports
from cars import cars, add_car, view_cars 
from customers import customers, add_customer, view_customers



# Franchise selection

franchises = [
    {"id": 1, "name": "AutoVault Amritsar"},
    {"id": 2, "name": "AutoVault Ludhiana"},
    {"id": 3, "name": "AutoVault Delhi"}
]

def select_franchise():
    print("\n======= Welcome to AutoVault =======")
    print("Available Franchises:")
    for f in franchises:
        print(f"{f['id']}. {f['name']}")
    
    choice = int(input("\nSelect Franchise: "))
    selected = franchises[choice - 1]
    print(f"\n {selected['name']} selected!")
    return selected

selected_franchise = select_franchise()

# Main Menu(Features)

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
            print("Sell Car - coming soon")
        elif choice == "6":
            print("View Sales - coming soon")
        elif choice == "7":
            selected_franchise = select_franchise()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_menu()