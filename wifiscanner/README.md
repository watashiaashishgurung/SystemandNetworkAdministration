# Wi-Fi Scanner Script

This script allows you to scan Wi-Fi networks in your area using Python. Since macOS removed CLI Wi-Fi scanning options, this script provides an alternative solution.

## Prerequisites

- Ensure you have Python 3 installed on your system.
- It is recommended to run this script in a virtual machine (VM) for security and isolation purposes.

## How to Run

Execute the script using the following command:

```bash
python3 scan_wifi.py
```

## Output Explanation

The script outputs a table with the following details:

| Header   | Stands For                     | Description                                                                 |
|----------|--------------------------------|-----------------------------------------------------------------------------|
| **SSID** | Service Set Identifier         | The human-readable name of the Wi-Fi network (its “SSID”).                 |
| **BSSID**| Basic Service Set Identifier   | The MAC address of the specific access point you’re seeing.                |
| **RSSI** | Received Signal Strength Indicator | A measure of signal strength (higher = better).                            |
| **Ch**   | Channel                        | The radio channel (frequency band) the network is using.                   |
| **Security** | —                          | The authentication/encryption protocol (e.g., WPA2, WPA3, Open, etc.).     |

Use this script to analyze nearby Wi-Fi networks and gather useful information about their configurations.