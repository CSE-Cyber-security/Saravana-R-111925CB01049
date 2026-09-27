# Week 01 — Cybersecurity Asset Inventory System

A command-line Python program that lets a security administrator **add,
search, update, delete, and display** an organization's IT assets, and get a
quick **security summary** across the whole inventory.

## Problem Statement

An organization maintains several IT assets such as computers, servers,
routers, switches, and software applications. Managing these assets
manually makes it difficult to identify the assets, track their security
status, and determine which assets require immediate attention. This
program solves that by giving the administrator a simple menu-driven tool
to manage the inventory, with each asset classified by **type** and
**risk level**.

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py     # Main program
│
├── data/
│   └── assets.json            # Sample / persisted asset data
│
├── tests/
│   └── test_cases.md          # Manual test cases and results
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md
```

## Asset Fields

| Field | Description |
|---|---|
| Asset ID | Unique identifier for the asset |
| Asset Name | Human-readable name |
| Asset Type | `Workstation`, `Server`, `Router`, `Switch`, or `Application` |
| IP Address | Network address of the asset |
| Operating System | OS or firmware running on the asset |
| Owner/Department | Team responsible for the asset |
| Risk Level | `Low`, `Medium`, `High`, or `Critical` |
| Security Status | `Secure`, `Warning`, or `Vulnerable` |

## Features

1. **Add Asset** — enter details for a new asset; input is validated
   (Asset Type, Risk Level, Security Status must be one of the allowed
   values; required fields cannot be blank; Asset IDs must be unique).
2. **Display All Assets** — prints every asset in a formatted report.
3. **Search Asset** — search by Asset ID or Asset Name (partial match).
4. **Update Asset** — look up an asset by ID and change one or more
   fields; leaving a field blank keeps its current value.
5. **Delete Asset** — remove an asset by ID, with a confirmation prompt.
6. **Security Summary** — counts of total assets, assets at each risk
   level, and assets at each security status.
7. **Exit** — closes the program.

All changes are saved to `data/assets.json`, so the inventory persists
between runs.

## How to Run

```bash
cd src
python3 asset_inventory.py
```

You'll see a menu like this:

```
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
```

Enter a number from 1–7 and follow the prompts.

## Sample Output

```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID       : A101
Asset Name     : HR-PC-01
Asset Type     : Workstation
IP Address     : 192.168.1.10
OS             : Windows 11
Department     : HR
Risk Level     : Medium
Status         : Secure
-----------------------------------------
Asset ID       : A102
Asset Name     : Web-Server
Asset Type     : Server
IP Address     : 192.168.1.20
OS             : Ubuntu
Department     : IT
Risk Level     : Critical
Status         : Vulnerable
-----------------------------------------
Asset ID       : A103
Asset Name     : Core-Router
Asset Type     : Router
IP Address     : 192.168.1.1
OS             : Cisco IOS
Department     : Network
Risk Level     : High
Status         : Warning
=========================================
```

## Testing

See [`tests/test_cases.md`](tests/test_cases.md) for the full list of
manual test cases (adding, searching, updating, deleting, validation
errors, persistence, and the security summary), each with expected vs.
actual results. Matching screenshots for each scenario are in
[`screenshots/`](screenshots/).

## Notes / Design Choices

- Data is stored as a JSON list of objects in `data/assets.json` — simple
  to read, edit, and version-control.
- Field validation for Asset Type, Risk Level, and Security Status is
  case-insensitive but always stores the canonical (title-case) value.
- Update lets any subset of fields change at once; press Enter to skip a
  field and keep its existing value.
- Delete asks for confirmation before removing an asset, to avoid
  accidental data loss.
