"""
Cybersecurity Asset Inventory System
-------------------------------------
Weekly Mini Project - 01

A simple command-line tool that lets a security administrator
add, search, update, delete, and display an organization's IT
assets, and get a quick security summary of the whole inventory.

Data is persisted to data/assets.json so the inventory survives
between runs.
"""

import json
import os

# ---------------------------------------------------------------
# Constants / allowed values
# ---------------------------------------------------------------

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                          "data", "assets.json")


# ---------------------------------------------------------------
# Storage helpers
# ---------------------------------------------------------------

def load_assets():
    """Load the asset list from the JSON data file, if present."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []


def save_assets(assets):
    """Persist the current asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------------
# Input validation helpers
# ---------------------------------------------------------------

def get_choice(prompt, options):
    """Keep asking until the user enters one of the allowed options
    (case-insensitive), then return it in its canonical form."""
    options_map = {opt.lower(): opt for opt in options}
    while True:
        value = input(f"{prompt} ({'/'.join(options)}): ").strip()
        if value.lower() in options_map:
            return options_map[value.lower()]
        print(f"  Invalid input. Please choose one of: {', '.join(options)}")


def get_non_empty(prompt):
    """Keep asking until the user enters a non-blank value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This field cannot be empty. Please try again.")


def asset_id_exists(assets, asset_id):
    return any(a["Asset ID"].lower() == asset_id.lower() for a in assets)


# ---------------------------------------------------------------
# Core features
# ---------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")

    while True:
        asset_id = get_non_empty("Asset ID: ")
        if asset_id_exists(assets, asset_id):
            print("  An asset with this ID already exists. Please use a different ID.")
        else:
            break

    asset_name = get_non_empty("Asset Name: ")
    asset_type = get_choice("Asset Type", ASSET_TYPES)
    ip_address = get_non_empty("IP Address: ")
    operating_system = get_non_empty("Operating System: ")
    department = get_non_empty("Owner/Department: ")
    risk_level = get_choice("Risk Level", RISK_LEVELS)
    security_status = get_choice("Security Status", SECURITY_STATUSES)

    asset = {
        "Asset ID": asset_id,
        "Asset Name": asset_name,
        "Asset Type": asset_type,
        "IP Address": ip_address,
        "Operating System": operating_system,
        "Department": department,
        "Risk Level": risk_level,
        "Security Status": security_status,
    }
    assets.append(asset)
    save_assets(assets)
    print(f"\nAsset '{asset_id}' added successfully.")


def print_asset(asset):
    print(f"Asset ID       : {asset['Asset ID']}")
    print(f"Asset Name     : {asset['Asset Name']}")
    print(f"Asset Type     : {asset['Asset Type']}")
    print(f"IP Address     : {asset['IP Address']}")
    print(f"OS             : {asset['Operating System']}")
    print(f"Department     : {asset['Department']}")
    print(f"Risk Level     : {asset['Risk Level']}")
    print(f"Status         : {asset['Security Status']}")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")
    if not assets:
        print("No assets found in the inventory.")
    else:
        for i, asset in enumerate(assets):
            print_asset(asset)
            if i != len(assets) - 1:
                print("-----------------------------------------")
    print("=========================================")


def search_asset(assets):
    print("\n--- Search Asset ---")
    term = get_non_empty("Enter Asset ID or Asset Name to search: ").lower()
    results = [a for a in assets
               if term in a["Asset ID"].lower() or term in a["Asset Name"].lower()]

    if not results:
        print(f"No asset found matching '{term}'.")
        return

    print(f"\nFound {len(results)} matching asset(s):\n")
    for i, asset in enumerate(results):
        print_asset(asset)
        if i != len(results) - 1:
            print("-----------------------------------------")


def find_asset_index(assets, asset_id):
    for i, a in enumerate(assets):
        if a["Asset ID"].lower() == asset_id.lower():
            return i
    return -1


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset_id = get_non_empty("Enter Asset ID to update: ")
    idx = find_asset_index(assets, asset_id)

    if idx == -1:
        print(f"No asset found with ID '{asset_id}'.")
        return

    asset = assets[idx]
    print("\nLeave a field blank to keep its current value.\n")

    new_name = input(f"Asset Name [{asset['Asset Name']}]: ").strip()
    if new_name:
        asset["Asset Name"] = new_name

    new_type = input(f"Asset Type [{asset['Asset Type']}] ({'/'.join(ASSET_TYPES)}): ").strip()
    if new_type:
        while new_type.title() not in ASSET_TYPES and new_type.capitalize() not in ASSET_TYPES \
                and new_type not in ASSET_TYPES:
            new_type = input(f"  Invalid. Asset Type ({'/'.join(ASSET_TYPES)}): ").strip()
            if not new_type:
                break
        if new_type:
            for opt in ASSET_TYPES:
                if new_type.lower() == opt.lower():
                    asset["Asset Type"] = opt
                    break

    new_ip = input(f"IP Address [{asset['IP Address']}]: ").strip()
    if new_ip:
        asset["IP Address"] = new_ip

    new_os = input(f"Operating System [{asset['Operating System']}]: ").strip()
    if new_os:
        asset["Operating System"] = new_os

    new_dept = input(f"Owner/Department [{asset['Department']}]: ").strip()
    if new_dept:
        asset["Department"] = new_dept

    new_risk = input(f"Risk Level [{asset['Risk Level']}] ({'/'.join(RISK_LEVELS)}): ").strip()
    if new_risk:
        for opt in RISK_LEVELS:
            if new_risk.lower() == opt.lower():
                asset["Risk Level"] = opt
                break

    new_status = input(f"Security Status [{asset['Security Status']}] ({'/'.join(SECURITY_STATUSES)}): ").strip()
    if new_status:
        for opt in SECURITY_STATUSES:
            if new_status.lower() == opt.lower():
                asset["Security Status"] = opt
                break

    assets[idx] = asset
    save_assets(assets)
    print(f"\nAsset '{asset_id}' updated successfully.")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = get_non_empty("Enter Asset ID to delete: ")
    idx = find_asset_index(assets, asset_id)

    if idx == -1:
        print(f"No asset found with ID '{asset_id}'.")
        return

    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        removed = assets.pop(idx)
        save_assets(assets)
        print(f"Asset '{removed['Asset ID']}' deleted successfully.")
    else:
        print("Deletion cancelled.")


def security_summary(assets):
    print("\n=========================================")
    print(" SECURITY SUMMARY")
    print("=========================================")
    total = len(assets)
    critical = sum(1 for a in assets if a["Risk Level"] == "Critical")
    high = sum(1 for a in assets if a["Risk Level"] == "High")
    medium = sum(1 for a in assets if a["Risk Level"] == "Medium")
    low = sum(1 for a in assets if a["Risk Level"] == "Low")
    vulnerable = sum(1 for a in assets if a["Security Status"] == "Vulnerable")
    warning = sum(1 for a in assets if a["Security Status"] == "Warning")
    secure = sum(1 for a in assets if a["Security Status"] == "Secure")

    print(f"Total Assets          : {total}")
    print(f"Critical Assets       : {critical}")
    print(f"High Risk Assets      : {high}")
    print(f"Medium Risk Assets    : {medium}")
    print(f"Low Risk Assets       : {low}")
    print(f"Vulnerable Assets     : {vulnerable}")
    print(f"Warning Assets        : {warning}")
    print(f"Secure Assets         : {secure}")
    print("=========================================")


# ---------------------------------------------------------------
# Menu / entry point
# ---------------------------------------------------------------

MENU = """
=========================================
 CYBERSECURITY ASSET INVENTORY SYSTEM
=========================================
1. Add Asset
2. Display All Assets
3. Search Asset
4. Update Asset
5. Delete Asset
6. Security Summary
7. Exit
=========================================
"""


def main():
    assets = load_assets()
    print("Welcome to the Cybersecurity Asset Inventory System.")

    while True:
        print(MENU)
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            display_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            security_summary(assets)
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
