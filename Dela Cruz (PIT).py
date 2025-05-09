visitor_log = []

def show_menu():
    print("\n=== VISITOR LOG MANAGEMENT SYSTEM ===")
    print("1. Log In Visitor")
    print("2. Search Visitor by Name")
    print("3. Add New Visitor")
    print("4. View All Visitors")
    print("5. Exit")

def log_in_visitor():
    print("\n=== VISITOR LOG IN ===")
    name = input("Enter visitor name: ")
    purpose = input("Enter purpose of visit: ")
    time_in = input("Enter time in (HH:MM): ")
    date = input("Enter date: ")
    address = input("Enter address: ")

    visitor_log.append({
        "name": name,
        "purpose": purpose,
        "time_in": time_in,
        "date": date,
        "address": address
     
    })
    print(f"Visitor '{name}' logged successfully.")

def search_visitor():
    print("\n=== SEARCH VISITOR ===")
    search_name = input("Enter name to search: ").lower()
    found = False
    for visitor in visitor_log:
        if search_name in visitor["name"].lower():
            print(f"Found: {visitor}")
            found = True
    if not found:
        print("No visitor found with that name.")

def add_new_visitor():
    print("\n=== ADD NEW VISITOR===")
    name = input("Enter new visitor's full name: ")
    purpose = input("Enter purpose: ")
    time_in = input("Enter time in: ")
    date = input("Enter date: ")
    address = input("Enter address: ")
   
    
    visitor_log.append({
        "name": name,
        "purpose": purpose,
        "time_in": time_in,
        "date": date,
        "address": address
        
    })
    print(f"New visitor '{name}' added.")

def view_all_visitors():
    print("\n VIEW ALL VISITORS")
    if not visitor_log:
        print("No visitors logged yet.")
    else:
        print("\n=== Visitor List ===")
        for i, visitor in enumerate(visitor_log, 1):
            print(f"{i}. Name: {visitor['name']}, Purpose: {visitor['purpose']}, Time In: {visitor['time_in']},Date: {visitor['date']}, Address: {visitor['address']} ")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        log_in_visitor()
    elif choice == '2':
        search_visitor()
    elif choice == '3':
        add_new_visitor()
    elif choice == '4':
        view_all_visitors()
    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")