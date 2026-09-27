# Test Cases — Cybersecurity Asset Inventory System

Manual test cases used to verify `src/asset_inventory.py`. Each test was run
against the program starting from the sample dataset in `data/assets.json`
(A101, A102, A103) unless stated otherwise.

| # | Feature | Input | Expected Output | Actual Output | Result |
|---|---------|-------|------------------|----------------|--------|
| TC01 | Add Asset (valid data) | Menu `1`, Asset ID `A104`, Name `Finance-PC`, Type `Workstation`, IP `192.168.1.15`, OS `Windows 10`, Dept `Finance`, Risk `Low`, Status `Secure` | "Asset 'A104' added successfully." and asset appears on Display | As expected | Pass |
| TC02 | Add Asset (duplicate ID) | Menu `1`, Asset ID `A101` (already exists) | Program rejects the ID and re-prompts: "An asset with this ID already exists." | As expected | Pass |
| TC03 | Add Asset (blank required field) | Menu `1`, Asset ID left blank | "This field cannot be empty. Please try again." then re-prompts | As expected | Pass |
| TC04 | Add Asset (invalid Asset Type) | Type entered as `Desktop` | "Invalid input. Please choose one of: Workstation, Server, Router, Switch, Application" then re-prompts | As expected | Pass |
| TC05 | Add Asset (invalid Risk Level) | Risk entered as `Extreme` | "Invalid input. Please choose one of: Low, Medium, High, Critical" then re-prompts | As expected | Pass |
| TC06 | Add Asset (invalid Security Status) | Status entered as `Unsafe` | "Invalid input. Please choose one of: Secure, Warning, Vulnerable" then re-prompts | As expected | Pass |
| TC07 | Display All Assets | Menu `2` | All 3 assets printed with matching headers/separators, in insertion order | As expected | Pass |
| TC08 | Display All Assets (empty inventory) | Menu `2` on a fresh/empty `assets.json` | "No assets found in the inventory." | As expected | Pass |
| TC09 | Search Asset (match by name substring) | Menu `3`, search term `Web` | Returns `A102 – Web-Server` only | As expected | Pass |
| TC10 | Search Asset (match by ID) | Menu `3`, search term `A103` | Returns `A103 – Core-Router` only | As expected | Pass |
| TC11 | Search Asset (no match) | Menu `3`, search term `zzz` | "No asset found matching 'zzz'." | As expected | Pass |
| TC12 | Update Asset (change some fields) | Menu `4`, ID `A103`, blank for most fields, Risk `Critical`, Status `Vulnerable` | Only Risk Level and Security Status change; rest unchanged; "Asset 'A103' updated successfully." | As expected | Pass |
| TC13 | Update Asset (ID not found) | Menu `4`, ID `A999` | "No asset found with ID 'A999'." | As expected | Pass |
| TC14 | Delete Asset (confirm) | Menu `5`, ID `A103`, confirm `y` | "Asset 'A103' deleted successfully."; asset no longer appears on Display | As expected | Pass |
| TC15 | Delete Asset (cancel) | Menu `5`, ID `A103`, confirm `n` | "Deletion cancelled."; asset still present on Display | As expected | Pass |
| TC16 | Delete Asset (ID not found) | Menu `5`, ID `A999` | "No asset found with ID 'A999'." | As expected | Pass |
| TC17 | Security Summary | Menu `6` (with sample dataset A101–A103) | Total: 3, Critical: 1, High: 1, Medium: 1, Low: 0, Vulnerable: 1, Warning: 1, Secure: 1 | As expected | Pass |
| TC18 | Invalid menu choice | Menu input `9` | "Invalid choice. Please enter a number between 1 and 7." then menu re-displays | As expected | Pass |
| TC19 | Persistence across runs | Add an asset, exit (`7`), relaunch the program | Newly added asset is still present after relaunch (loaded from `data/assets.json`) | As expected | Pass |
| TC20 | Exit | Menu `7` | "Exiting... Goodbye!" and program terminates cleanly | As expected | Pass |

## Notes
- All risk levels (Low/Medium/High/Critical) and security statuses
  (Secure/Warning/Vulnerable) were exercised at least once across TC01–TC17.
- Input validation is case-insensitive (e.g. `workstation` and `Workstation`
  are both accepted) but the value is always stored in its canonical form.
- Corresponding screenshots for each scenario are in `../screenshots/`.
