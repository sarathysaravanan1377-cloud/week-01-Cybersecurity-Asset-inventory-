
# ==========================================
# CYBERSECURITY ASSET INVENTORY SYSTEM
# ==========================================

class Asset:
    def __init__(self, asset_id, name, asset_type, ip_address, risk_level):
        self.asset_id = asset_id
        self.name = name
        self.asset_type = asset_type
        self.ip_address = ip_address
        self.risk_level = risk_level

    def display(self):
        print("\n-----------------------------")
        print(f"Asset ID    : {self.asset_id}")
        print(f"Name        : {self.name}")
        print(f"Type        : {self.asset_type}")
        print(f"IP Address  : {self.ip_address}")
        print(f"Risk Level  : {self.risk_level}")
        print("-----------------------------")


# Store all assets
assets = []


# ==========================================
# ADD ASSET
# ==========================================

def add_asset():
    print("\n===== ADD NEW ASSET =====")

    try:
        asset_id = int(input("Enter Asset ID: "))

        # Prevent duplicate IDs
        for asset in assets:
            if asset.asset_id == asset_id:
                print("Asset ID already exists!")
                return

        name = input("Enter Asset Name: ")
        asset_type = input(
            "Enter Asset Type (Computer/Server/Router/Switch/Software): "
        )
        ip_address = input("Enter IP Address: ")
        risk_level = input("Enter Risk Level (Low/Medium/High): ")

        # Validate risk level
        if risk_level.lower() not in ["low", "medium", "high"]:
            print("Invalid risk level!")
            return

        new_asset = Asset(
            asset_id,
            name,
            asset_type,
            ip_address,
            risk_level.capitalize()
        )

        assets.append(new_asset)

        print("\nAsset added successfully!")

    except ValueError:
        print("Please enter a valid numeric Asset ID!")


# ==========================================
# DISPLAY ALL ASSETS
# ==========================================

def display_assets():
    print("\n===== ALL CYBERSECURITY ASSETS =====")

    if not assets:
        print("No assets found.")
        return

    for asset in assets:
        asset.display()


# ==========================================
# SEARCH ASSET
# ==========================================

def search_asset():
    print("\n===== SEARCH ASSET =====")

    try:
        asset_id = int(input("Enter Asset ID to search: "))

        for asset in assets:
            if asset.asset_id == asset_id:
                print("\nAsset Found!")
                asset.display()
                return

        print("Asset not found.")

    except ValueError:
        print("Please enter a valid Asset ID!")


# ==========================================
# UPDATE ASSET
# ==========================================

def update_asset():
    print("\n===== UPDATE ASSET =====")

    try:
        asset_id = int(input("Enter Asset ID to update: "))

        for asset in assets:
            if asset.asset_id == asset_id:

                print("\nEnter New Details")

                asset.name = input("Enter New Asset Name: ")
                asset.asset_type = input("Enter New Asset Type: ")
                asset.ip_address = input("Enter New IP Address: ")

                risk_level = input(
                    "Enter New Risk Level (Low/Medium/High): "
                )

                if risk_level.lower() not in ["low", "medium", "high"]:
                    print("Invalid risk level! Update cancelled.")
                    return

                asset.risk_level = risk_level.capitalize()

                print("\nAsset updated successfully!")
                return

        print("Asset not found.")

    except ValueError:
        print("Please enter a valid Asset ID!")


# ==========================================
# DELETE ASSET
# ==========================================

def delete_asset():
    print("\n===== DELETE ASSET =====")

    try:
        asset_id = int(input("Enter Asset ID to delete: "))

        for asset in assets:
            if asset.asset_id == asset_id:

                assets.remove(asset)

                print("\nAsset deleted successfully!")
                return

        print("Asset not found.")

    except ValueError:
        print("Please enter a valid Asset ID!")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n==========================================")
        print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
        print("==========================================")

        print("1. Add Asset")
        print("2. Display All Assets")
        print("3. Search Asset")
        print("4. Update Asset")
        print("5. Delete Asset")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_asset()

        elif choice == "2":
            display_assets()

        elif choice == "3":
            search_asset()

        elif choice == "4":
            update_asset()

        elif choice == "5":
            delete_asset()

        elif choice == "6":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
