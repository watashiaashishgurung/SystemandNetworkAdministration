#!/usr/bin/env python3
import CoreWLAN

SECURITY_TYPES = {
    0: "None",
    1: "WEP",
    2: "WPA Personal",
    3: "WPA/WPA2 Personal",
    4: "WPA2/WPA3 Personal",
    5: "WPA2 Enterprise",
    6: "WPA3 Enterprise",
    7: "WPA3 Personal",
    8: "WPA3 Enterprise Transition",
}

iface = CoreWLAN.CWInterface.interface()
networks, error = iface.scanForNetworksWithName_error_(None, None)

if error:
    raise SystemExit(f"Scan failed: {error}")
if not networks:
    print("No networks found.")
    raise SystemExit

print(f"{'SSID':30} {'BSSID':17}  RSSI   Ch  Security")
print("-" * 75)
for net in networks:
    ssid     = net.ssid() or "<hidden>"
    bssid    = net.bssid() or "N/A"
    rssi     = net.rssiValue() if net.rssiValue() is not None else 0
    chnum    = net.wlanChannel().channelNumber() if net.wlanChannel() else 0
    sec_type = net.securityType()  # Updated to use securityType()
    sec      = SECURITY_TYPES.get(sec_type, f"Unknown ({sec_type})")  # Show raw value if unknown
    print(f"{ssid:30} {bssid:17}  {rssi:4d}dBm  {chnum:2d}   {sec}")