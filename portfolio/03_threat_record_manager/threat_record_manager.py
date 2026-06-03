
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

threat = {
    "ip": "185.220.101.1",
    "country": "RU",
    "severity": "high",
    "alert_count": 5
}

while True:
    clear_screen()
    
    print("\n" + "="*41)
    print("="*9 + " THREAT RECORD MANAGER " + "="*9)
    print("="*41)
    print(" [1] View threat record\n",
          " [2] Update a field\n",
          " [3] Add a new field\n",
          " [4] Delete a field\n",
          " [5] Check if a field exists\n",
          " [Q] Quit\n",
          sep="")
    
    option = input("Enter option: ").lower()

    if option == "q":
        print("\nClosing...")
        break
        
# View fields
    elif option == "1":
        print(f"\n{threat}")
        input("\nPress Enter to return to menu...")
        
# Update a field
    elif option == "2":
        old_key = input("Enter key to update (or 'q' to cancel):").strip().lower()

        if old_key == 'q' or not old_key:
            print("\nAction canceled.")
            continue
            
        elif old_key in threat:
            print(f"Current value for '{old_key}': {threat[old_key]}")
            
            new_value = input("Enter new value (press Enter to keep current, or 'q' to cancel: ").strip()

            if new_value.lower() == 'q':
                print("\nAction canceled.")
                continue

            if new_value:
                threat[old_key] = new_value
                print(f"[Value updated]")
                
            rename_choice = input(f"Rename the old key '{old_key}'? (yes/no, or 'q' to cancel): ").strip().lower()

            if rename_choice == 'q':
                print("\nAction canceled.")
                continue

            elif rename_choice == 'yes':
                new_key = input("\nEnter new key (or 'q' to cancel): ").strip().lower()
                
                if not new_key or new_key == 'q':
                    print("Renaming canceled.")
                    input("\nPress Enter to return to menu...")
                    continue
                    
                elif new_key == old_key:
                    print("New key name matches the old one. No change made.")
                elif new_key in threat:
                    print(f"[ERROR]: The key '{new_key}' already exists. Rename aborted.")
                    input("\nPress Enter to return to menu...")
                    continue
                    
                else:
                    threat[new_key] = threat[old_key]
                    del threat[old_key]
                    print(f"[Key renamed] '{old_key}' changed to '{new_key}' ")
                    
            elif rename_choice == 'no':
                print("\nKey rename skipped")
                
            else:
                print("Invalid input. Key rename skipped.")
                
            print(f"\n[Current Field]: {threat}")

        else:
            print(f"\nField {old_key} not found")

        input("\nPress Enter to return to menu...")

# Add a field
    elif option == "3":
        new_key = input("Enter new key (or 'q' to cancel): ").strip().lower()

        if new_key == 'q' or not new_key:
            print("\nAction canceled.")
            continue
            
        elif new_key not in threat:
            new_value = input("Enter new value (or 'q' to cancel): ").strip()

            if new_value == 'q' or not new_value:
                print("\nAction canceled.")
                continue

            else:
                threat[new_key] = new_value
                print(f"\n[Field added] Updated fields: {threat}")
            
        else:
            print("\nField already exists. Use option 2 to update.")

        input("\nPress Enter to return to menu...")

# Delete a field
    elif option == "4":
        key = input("Enter key: ").strip().lower()

        if key in threat:
            del threat[key]
            print(f"\n[Field deleted] Updated fields: {threat}")
    
        else:
            print("\nField doesn't exist. Use option 3 to add or try again.")
            
        input("\nPress Enter to return to menu...")

# Check a field
    elif option == "5":
        key = input("Enter key: ").strip().lower()

        if key in threat:
            print(f"\nField [{key}] exists.",
                  f"\nCurrent fields: {threat}",
                  sep="")
        else:
            print("\nField doesn't exist. Use option 3 to add or try again.")
            
        input("\nPress Enter to return to menu...")
        
    else:
        print("\nInvalid option. Please choose 1-5 or Q.")
        input("\nPress Enter to return to menu...")