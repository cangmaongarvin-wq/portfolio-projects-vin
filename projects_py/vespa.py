
import os

def clear_screen():
    # 'nt' is the internal Python name of Windows, 'posix' covers Linux
    os.system('cls' if os.name == 'nt' else 'clear')

import sys
import copy


# 1. MAIN SYSTEM DATABASE (Hidden from view)
bookings_db = {
    "K45LMN": {
        "ref": "K45LMN", "bkr": "WILSON/MARK", "agt": "TRAIN1", "tkt": "12MAY26/1045Z/WEB",
        "segments": [
            {"num": "01", "flight": "U28643", "route": "LGWGVA", "date": "091026", "time": "0845-1125", "stops": "0", "status": "HK2", "price": 198.00},
            {"num": "02", "flight": "U28648", "route": "GVALGW", "date": "091726", "time": "1315-1355", "stops": "0", "status": "HK2", "price": 180.00}
        ],
        "svc_indicator": "0", "svc_msg": "NONE", "dep_term": "LGW-N", "arr_term": "GVA-T1", "aircraft": "A321", "operator": "U2-EZY",
        "pax": [
            {"id": "PAX1", "name": "WILSON/MARK[ADT]", "seat": "14B", "bag": "23KG", "se": "0SE", "fee": "GBP24.00"},
            {"id": "PAX2", "name": "WILSON/LISA[ADT]", "seat": "14C", "bag": "NONE", "se": "0SE", "fee": "NONE"}
        ],
        "fee_flt": 326.00, "fee_apd": 52.00, "fee_chg": 0.00, 
        "ctc_type": "MOB", "ctc_num": "+442079460555", "eml": "M.WILSON@EMAIL.COM", "bal": 0.00
    },
    "K77ABC": {
        "ref": "K77ABC", "bkr": "THOMPSON/ALEX", "agt": "TRAIN1", "tkt": "14MAY26/1620Z/APP",
        "segments": [
            {"num": "01", "flight": "U22103", "route": "LTNAGP", "date": "061526", "time": "0600-0945", "stops": "0", "status": "HK2", "price": 210.00},
            {"num": "02", "flight": "U22104", "route": "AGPLTN", "date": "062226", "time": "1030-1220", "stops": "0", "status": "HK2", "price": 195.00}
        ],
        "svc_indicator": "0", "svc_msg": "NONE", "dep_term": "LTN-MAIN", "arr_term": "AGP-T3", "aircraft": "A320", "operator": "U2-EZY",
        "pax": [
            {"id": "PAX1", "name": "THOMPSON/ALEX[ADT]", "seat": "06A", "bag": "15KG", "se": "0SE", "fee": "GBP18.00"},
            {"id": "PAX2", "name": "MILLER/SARAHMS[ADT]", "seat": "06B", "bag": "23KG", "se": "0SE", "fee": "GBP24.00"}
        ],
        "fee_flt": 351.00, "fee_apd": 54.00, "fee_chg": 0.00, 
        "ctc_type": "PHN", "ctc_num": "+441619460111", "eml": "ALEX.T@EMAIL.CO.UK", "bal": 0.00
    },
    "K12XYZ": {
        "ref": "K12XYZ", "bkr": "HARRIS/DAVID", "agt": "TRAIN1", "tkt": "18MAY26/0815Z/WEB",
        "segments": [
            {"num": "01", "flight": "U28401", "route": "LGWCDG", "date": "070426", "time": "1420-1535", "stops": "0", "status": "HK1", "price": 89.00}
        ],
        "svc_indicator": "0", "svc_msg": "NONE", "dep_term": "LGW-N", "arr_term": "CDG-T2B", "aircraft": "A320", "operator": "U2-EZY",
        "pax": [
            {"id": "PAX1", "name": "HARRIS/DAVIDMR[ADT]", "seat": "22C", "bag": "NONE", "se": "0SE", "fee": "NONE"}
        ],
        "fee_flt": 76.00, "fee_apd": 13.00, "fee_chg": 0.00, 
        "ctc_type": "MOB", "ctc_num": "+442079460999", "eml": "DAVID.HARRIS@CORPORATE.COM", "bal": 0.00
    },
    "K88MNO": {
        "ref": "K88MNO", "bkr": "OLESEN/NIELS", "agt": "TRAIN1", "tkt": "10MAY26/1100Z/APP",
        "segments": [
            {"num": "01", "flight": "U28261", "route": "LGWCPH", "date": "081226", "time": "1115-1410", "stops": "0", "status": "HK3", "price": 315.00},
            {"num": "02", "flight": "U28266", "route": "CPHLGW", "date": "081926", "time": "1550-1650", "stops": "0", "status": "HK3", "price": 290.00}
        ],
        "svc_indicator": "0", "svc_msg": "NONE", "dep_term": "LGW-N", "arr_term": "CPH-T3", "aircraft": "A321", "operator": "U2-EZY",
        "pax": [
            {"id": "PAX1", "name": "OLESEN/NIELS[ADT]", "seat": "10D", "bag": "23KG", "se": "0SE", "fee": "GBP24.00"},
            {"id": "PAX2", "name": "OLESEN/ANNA[ADT]", "seat": "10E", "bag": "23KG", "se": "0SE", "fee": "GBP24.00"},
            {"id": "PAX3", "name": "OLESEN/EMMA[CHD]", "seat": "10F", "bag": "NONE", "se": "0SE", "fee": "NONE"}
        ],
        "fee_flt": 526.00, "fee_apd": 79.00, "fee_chg": 0.00, 
        "ctc_type": "PHN", "ctc_num": "+4535321122", "eml": "NIELS.O@MAIL.DK", "bal": 0.00
    },
    "K99ERR": {
        "ref": "K99ERR", "bkr": "BROOKS/JANE", "agt": "TRAIN1", "tkt": "05MAY26/0930Z/WEB",
        "segments": [
            {"num": "01", "flight": "U28105", "route": "LGWAMS", "date": "060126", "time": "1745-1900", "stops": "0", "status": "HK1", "price": 112.00}
        ],
        "svc_indicator": "1", "svc_msg": "PENALTY CHG FEE - GBP45.00 OUTSTANDING",
        "dep_term": "LGW-N", "arr_term": "AMS-M", "aircraft": "A320", "operator": "U2-EZY",
        "pax": [
            {"id": "PAX1", "name": "BROOKS/JANE[ADT]", "seat": "18A", "bag": "NONE", "se": "0SE", "fee": "NONE"}
        ],
        "fee_flt": 99.00, "fee_apd": 13.00, "fee_chg": 45.00, 
        "ctc_type": "MOB", "ctc_num": "+442079460222", "eml": "J.BROOKS@EMAIL.COM", "bal": 45.00
    }
}

active_ref = None
session_booking = None  
staged_changes = []     

# 2. SCREEN GENERATOR BLOCK (Tweaked Minimalist Layout)
def display_vespa_screen():
    clear_screen()

    # Uniform header width matching the bottom (80 columns)
    print("\n" + "="*80)
    print(f"RECORD LOCATOR: {active_ref}   STATUS: ACTIVE")
    print("="*80)
    
    # Direct extraction prevents future IndexError crashes if slashes vary
    tkt_time = session_booking['tkt']
    
    # 1. Header values
    print(f"{session_booking['ref']}   {session_booking['bkr']}   {session_booking['agt']}   {tkt_time}")
    print("-"*80) # Subtle internal divider line
    
    # 2. Segment values (Kept concise to avoid layout overflow)
    for seg in session_booking['segments']:
        print(f"{seg['num']} {seg['flight']} {seg['route']} {seg['date']} {seg['time']} "
              f"{seg['stops']} {seg['status']} {seg['price']:.2f} GBP")
    
    # 3. SVC Line Tweak: Show indicator, drop 'NONE' if 0
    if session_booking['svc_indicator'] == "0":
        print(f"SVC-0")
    else:
        print(f"SVC-{session_booking['svc_indicator']} - {session_booking['svc_msg']}")
        
    # 4. Departs/Arrives Tweak: Keys stay, replace colon with a space
    print(f"departs {session_booking['dep_term']} arrives {session_booking['arr_term']} "
          f"{session_booking['aircraft']} {session_booking['operator']}")
    print("-"*80)
    
    # 5. Passenger Manifest Tweak: Replace 'NONE' string with '0'
    for p in session_booking['pax']:
        bag_val = "0KG" if p['bag'] == "NONE" else p['bag']
        fee_val = "0" if p['fee'] == "NONE" else p['fee']
        print(f"{p['id']}   {p['name']}   {p['seat']}   {bag_val}   {p['se']}   {fee_val}")
    print("-"*80)
    
    # 6. Financial and Contact values
    print(f"{session_booking['ctc_type']}   {session_booking['ctc_num']}   {session_booking['eml']}")
    print(f"FLT {session_booking['fee_flt']:.2f}   APD {session_booking['fee_apd']:.2f}   FEES {session_booking['fee_chg']:.2f}")

    # Dynamic Calculation & Card Presentation (assuming cc data fields exist)
    total_cost = session_booking['fee_flt'] + session_booking['fee_apd'] + session_booking['fee_chg']
    cc_type = session_booking.get('cc_type', 'AX')
    cc_mask = session_booking.get('cc_mask', 'XXXXXXXXXXXX4433')
    
    print(f"CC {cc_type} {cc_mask}   {total_cost:.2f}   {session_booking['bal']:.2f} GBP")
    print("="*80)

    # Staging Memory Buffer Window
    if staged_changes:
        print("\n*** UNCOMMITTED CHANGES IN SESSION BUFFER ***")
        for change in staged_changes:
            print(f"-> {change}")
        print("*********************************************")

# 3. RUNTIME APP WINDOW LOOP (Protected from Ctrl+C)
def run_vespa():
    global active_ref, session_booking, staged_changes
    
    while True:
        try:
            # THE CLEAN LANDING PAGE VIEW
            clear_screen()
            print("\n" + "="*50)
            print("             VESPA MOCK TOOL        ")
            print("="*50)
            
            locator_input = input("ENTER 6-CHARACTER REF CODE (or type 'quit'): ").strip().upper()
            
            if locator_input == "QUIT":
                print("Shutting down...")
                sys.exit()
                
            if locator_input in bookings_db:
                active_ref = locator_input
                session_booking = copy.deepcopy(bookings_db[active_ref])
                staged_changes = []
            else:
                print(">> INVALID REFERENCE CODE. TRY AGAIN.")
                continue

            in_booking_session = True
            while in_booking_session:
                try:
                    display_vespa_screen()
                    
                    print("\nCOMMANDS: .n (Name) | .se (Toggle SE Status) | .c (Contact) | .r (Refund)")
                    print("WORKSPACE: .u (Undo) | .io (Commit Changes) | .x (Back to Landing)")
                    command = input("ENTER COMMAND > ").strip().lower()
                    
                    if command == ".x":
                        print(f">> Closing session for {active_ref}. Clearing uncommitted memory.")
                        staged_changes = []
                        session_booking = None
                        active_ref = None
                        in_booking_session = False 
                        continue
                        
                    if session_booking['svc_indicator'] == "1" and command in [".n", ".se", ".c"]:
                        print("\n>> CONTROL BLOCK: UNPAID SVC FILE LINKED. MODIFICATION REJECTED.\n")
                        continue

                    if command == ".u":
                        if not staged_changes:
                            print(">> Buffer already clean.")
                        else:
                            session_booking = copy.deepcopy(bookings_db[active_ref])
                            staged_changes = []
                            print(">> Reverted local workspace to master file state.")
                        
                    elif command == ".io":
                        if not staged_changes:
                            print(">> No pending alterations to commit.")
                        else:
                            bookings_db[active_ref] = copy.deepcopy(session_booking)
                            staged_changes = []
                            print(">> SUCCESS: Changes committed to master file records.")
                        
                    elif command == ".n":
                        pax_id = input("Passenger ID (PAX1, PAX2): ").strip().upper()

                        # INSTANT FAIL-FAST CHECK: Verify ID exists first
                        valid_pax_ids = [p['id'] for p in session_booking['pax']]
                        if pax_id not in valid_pax_ids:
                            print(f"\n>> INVALID PASSENGER ID '{pax_id}'. TRANSACTION ABORTED IMMEDIATELY.")
                            input("Press ENTER to return to screen...")
                            continue
                        
                        # We only ask for the name if the ID is 100% valid
                        new_name = input("Corrected name layout: ").strip().upper()
                        
                        for p in session_booking['pax']:
                            if p['id'] == pax_id:
                                old_name = p['name']
                                p['name'] = new_name
                                staged_changes.append(f"Altered {pax_id} Name: '{old_name}' -> '{new_name}'")
                                print(">> Staged.")
                                input("\nPress ENTER to return to screen...")
                                break
                                
                    elif command == ".se":
                        pax_id = input("Passenger ID (PAX1, PAX2): ").strip().upper()

                        # FAIL_FAST: Block wrong IDs right here!
                        valid_pax_ids = [p['id'] for p in session_booking['pax']]
                        if pax_id not in valid_pax_ids:
                            print(f"\n>> INVALID PASSENGER ID '{pax_id}'. TRANSACTION ABORTED IMMEDIATELY.")
                            input("Press ENTER to return to screen...")
                            continue

                        # Only fires if the passenger actually exists
                        se_input = input("Enter special equipment note description (or 'NONE'): ").strip().upper()
                        
                        for p in session_booking['pax']:
                            if p['id'] == pax_id:
                                old_se = p['se']
                                if se_input == "NONE":
                                    p['se'] = "0SE"
                                else:
                                    paid_check = ["BIKE", "BICYCLE", "GOLF", "SKI", "SNOWBOARD", "SURF", "GUITAR", "CELLO"]
                                    if any(item in se_input for item in paid_check):
                                        print("\n>> STOP: Paid items blocked by your agent pricing profile.\n")
                                        break # Breaks out of the pax loop safely
                                    p['se'] = "1SE"
                                
                                staged_changes.append(f"Altered {pax_id} SE Status: '{old_se}' -> '{p['se']}' ({se_input})")
                                print(">> Staged.")
                                input("\nPress ENTER to return to screen...")
                                break

                    elif command == ".c":
                        while True:
                            c_type = input("Type (PHN or MOB) [Leave blank to keep current]: ").strip().upper()
                            if c_type == "":
                                c_type = session_booking['ctc_type']
                                break
                            if c_type in ["PHN", "MOB"]:
                                break
                            print(">> INVALID TYPE. Input must be exactly 'PHN' or 'MOB'.")
                        
                        c_num_input = input(f"Phone sequence ({session_booking['ctc_num']}) [Enter to keep]: ").strip().upper()
                        c_num = c_num_input if c_num_input != "" else session_booking['ctc_num']
                        
                        c_eml_input = input(f"Email profile ({session_booking['eml']}) [Enter to keep]: ").strip().upper()
                        c_eml = c_eml_input if c_eml_input != "" else session_booking['eml']
                        
                        changes_tracked = []
                        if c_type != session_booking['ctc_type']:
                            changes_tracked.append(f"Type: {session_booking['ctc_type']} -> {c_type}")
                        if c_num != session_booking['ctc_num']:
                            changes_tracked.append(f"Num: {session_booking['ctc_num']} -> {c_num}")
                        if c_eml != session_booking['eml']:
                            changes_tracked.append(f"Eml: {session_booking['eml']} -> {c_eml}")
                        
                        if changes_tracked:
                            session_booking['ctc_type'] = c_type
                            session_booking['ctc_num'] = c_num
                            session_booking['eml'] = c_eml
                            staged_changes.append(f"Altered Contact parameters ({', '.join(changes_tracked)}).")
                            print(">> Staged.")
                        else:
                            print(">> No contact changes detected. Workspace clean.")

                        input("\Press ENTER to return to screen...")
                        
                    elif command == ".r":
                        try:
                            refund_amount = float(input("Refund amount (Max 50): "))
                            if refund_amount <= 0:
                                print(">> Amount must be greater than 0.")
                                continue
                            
                            already_refunded = 0.0
                            for change in staged_changes:
                                if "Staged Cash Refund Allocation" in change:
                                    parts = change.split("GBP ")
                                    if len(parts) > 1:
                                        already_refunded += float(parts[1])
                            
                            if (already_refunded + refund_amount) > 50.00:
                                print(f"\n>> ACCESS DENIED: Aggregate session limit is GBP 50.00. Need TM approval."
                                      f"(Staged so far: GBP {already_refunded:.2f})\n")
                            elif session_booking['fee_flt'] - refund_amount < 0:
                                print(">> ACCESS DENIED: Refund exceeds remaining flight base fee value.")
                            else:
                                session_booking['fee_flt'] -= refund_amount
                                staged_changes.append(f"Staged Cash Refund Allocation: GBP {refund_amount:.2f}")
                                print(">> Staged.")
                        except ValueError:
                            print(">> Numerical format only.")
                    else:
                        print(">> Command unrecognized.")
                        
                except KeyboardInterrupt:
                    # Inner intercept: Prevents losing active booking changes!
                    print("\n\n>> WARNING: Keyboard Interrupt detected. Use '.x' to exit safely without losing session data.")
                    continue # <--- ADD THIS LINE TO SHORT-CIRCUIT THE UNRECOGNIZED DROPDOWN

        except KeyboardInterrupt:
            # Outer intercept: Handles landing page exit cleanly
            print("\n\n>> System termination bypassed. Type 'quit' to shut down safely.")
            continue # <--- ADD THIS LINE TO KEEP THE LANDING PAGE CLEAN

if __name__ == "__main__":
    run_vespa()