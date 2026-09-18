
# Cybersecurity Asset Inventory System

## 📌 Project Description

The **Cybersecurity Asset Inventory System** is a Python-based application designed to help organizations manage and monitor their IT assets.

It allows users to add, view, search, update, and delete asset information. Each asset contains details such as asset ID, name, type, IP address, and security risk level.

The system helps organize cybersecurity asset information and supports basic asset management.

## ✨ Features

- ➕ Add new IT assets
- 📋 Display all assets
- 🔍 Search assets by ID
- ✏️ Update asset information
- 🗑️ Delete assets
- 💻 Classify assets by type
- ⚠️ Track security risk levels
- 🖥️ Console-based user interface

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Structure:** List
- **Interface:** Command Line Interface (CLI)
- **Development Environment:** VS Code / PyCharm / IDLE

## 📂 Asset Information

| Field | Description |
|---|---|
| Asset ID | Unique identification number |
| Asset Name | Name of the IT asset |
| Asset Type | Computer, Server, Router, Switch, or Software |
| IP Address | Network address of the asset |
| Risk Level | Low, Medium, or High |

## 📊 Risk Levels

- **Low:** Asset has a lower assessed security risk.
- **Medium:** Asset requires regular security monitoring.
- **High:** Asset requires prioritized security review.

> Risk levels are manually entered and do not represent an automated security assessment.

## 📁 Project Structure

```text
Cybersecurity-Asset-Inventory/
│
├── cybersecurity_asset_inventory.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cybersecurity-asset-inventory.git
```

### 2. Navigate to the Project Directory

```bash
cd cybersecurity-asset-inventory
```

### 3. Run the Python Program

```bash
python cybersecurity_asset_inventory.py
```

For some systems, use:

```bash
python3 cybersecurity_asset_inventory.py
```

## 🖥️ Application Menu

```text
===== CYBERSECURITY ASSET INVENTORY SYSTEM =====

1. Add Asset
2. Display Assets
3. Search Asset
4. Update Asset
5. Delete Asset
6. Exit

Enter your choice:
```

## 📸 Sample Output

```text
Enter your choice: 1

Enter Asset ID: 101
Enter Asset Name: Main Server
Enter Asset Type: Server
Enter IP Address: 192.168.1.10
Enter Risk Level: High

Asset added successfully!
```

## 🎯 Project Objectives

1. Maintain an organized inventory of IT assets.
2. Simplify asset management using Python.
3. Store essential information about each asset.
4. Track manually assigned security risk levels.
5. Implement basic CRUD operations.

## 🔮 Future Enhancements

- Add a graphical user interface (GUI).
- Integrate a database for persistent storage.
- Implement user authentication.
- Add asset filtering and reporting.
- Add automated asset discovery.
- Integrate vulnerability management.
- Add security audit logs.

## ⚠️ Limitations

- Asset data is stored in memory during program execution.
- Data is lost when the program exits unless persistent storage is added.
- Risk levels are entered manually.
- The system does not perform real-time network monitoring or vulnerability scanning.

## 👨‍💻 Author

**Your Name**

## 📄 License

This project is developed for educational purposes.
