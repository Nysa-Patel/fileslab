"""
Project Name: Target Business Planner
Developer: Nysa Patel
Date: 2026-02-18
Purpose: This app manages target business data by persisting data to business_data.txt.
"""

def save_business_data(businesstype, salesmodel, scale):
    with open("business_data.txt", "a") as file:
        file.write(f"{businesstype}, {salesmodel}, {scale}\n")
    print("Business data saved!\n")

def load_business_data():
    try:
        with open("business_data.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No business data found.\n")
                return
            
            print("\n------- Saved Businesses -------")
            for line in lines:
                parts = line.strip().split(",")
                if len(parts) ==3:
                    print(f"Business Type: {parts[0]}")
                    print(f"Sales Model: {parts[1]}")
                    print(f"Scale: {parts[2]}")
                    print("-------------------------------")
    except FileNotFoundError:
        print("File not found.\n")
def main():
    while True:
        print("\n--- Target Business Planner ----")
        print("1. Add new business data")
        print("2. View Currently saved businesses")
        print("3. Exit out of the program")
        choice = input("Which do you want to do: ")
        
        if choice == "1":
            businesstype = input("Enter business type: ").strip()
            salesmodel = input("Enter sales model: ").strip()
            scale = input("Enter the scale of the business (local, regional, national, global): ").strip()
            if businesstype == "" or salesmodel == "" or scale =="":
                print("There are empty fields. Invalid\n")
            else:
                save_business_data(businesstype, salesmodel, scale)   
        elif choice == "2":
            load_business_data()
        elif choice == "3":
            print('Exiting Business Planner')
            break
        else:
            print('Not a valid choice\n')

main()




