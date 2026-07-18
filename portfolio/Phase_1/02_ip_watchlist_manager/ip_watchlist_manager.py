
flagged_ips = ["185.220.101.1", "10.0.0.99", "45.33.32.156", "198.51.100.23"]

while True:
    print("="*50)
    print("="*14 + " IP WATCHLIST MANAGER " + "="*14)
    print("="*50)
    print(" [1] View Watchlist\n",
          " [2] Add or Remove IP\n",
          " [3] Replace IP\n",
          " [4] Check if IP is flagged\n",
          " [Q] QUIT\n",
         sep="")

    option = input("Enter choice: ").lower()
    
    if option == "q":
        print("Closing...")
        break

    elif option == "1":
        print(f"Current Watchlist: {sorted(flagged_ips)}")

    elif option == "2":
        new_ip = input("Enter IP: ")
        
        if new_ip not in flagged_ips:
            yes_no = input("IP not found. Add? (Yes/No): ").lower()

            if yes_no == "yes":
                flagged_ips.append(new_ip)
                print(f"\n[IP ADDED] Updated Watchlist: {sorted(flagged_ips)}\n")
                
            else:
                print("NOT ADDED.")
                
        else:
            yes_no = input("IP found. Remove? (Yes/No): ").lower()

            if yes_no == "yes":
                flagged_ips.remove(new_ip)
                print(f"\n[IP REMOVED] Updated Watchlist: {sorted(flagged_ips)}\n")

            else:
                print("NOT REMOVED.")

    elif option == "3":
        old_ip = input("Enter Old IP: ")
       
        try:
            idx = flagged_ips.index(old_ip)
            
            new_ip = input("Enter New IP: ")
            flagged_ips[idx] = new_ip
            print(f"[IP REPLACED] Updated Watchlist: {sorted(flagged_ips)} ")
            
        except ValueError:
            print("\nERROR: IP is not on Watchlist.")

    elif option == "4":
        ip = input("Enter IP: ")

        if ip in flagged_ips:
            print(f"[IP FOUND] Current Watchlist: {sorted(flagged_ips)}")

        else:
            print("Not in Watchlist.\n")

    else:
        print("Invalid option. Please choose 1-4 or Q (for quit).")