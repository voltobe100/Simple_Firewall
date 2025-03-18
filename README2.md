# 🔥 Advanced Firewall

A Python-based firewall management tool to **block/unblock IPs and ports** on both **Linux (iptables)** and **Windows (netsh)** systems.

## 🚀 Features

✅ Block/unblock **specific IP addresses**  
✅ Block/unblock **specific ports (TCP/UDP)**  
✅ **List** active firewall rules  
✅ **Reset** firewall rules to default  
✅ **Cross-platform support** (Linux & Windows)  
✅ **Logging support** for debugging

## 🛠️ Installation

Ensure you have **Python 3.x** installed.  
Clone the repository and navigate into it:

```bash
git clone https://github.com/yourusername/advanced-firewall.git
cd advanced-firewall
```

## 📌 Usage

Run the script with administrative privileges:

```bash
python firewall.py --help
```

### Block an IP

```bash
python firewall.py --block-ip 192.168.1.100
```

### Unblock an IP

```bash
python firewall.py --unblock-ip 192.168.1.100
```

### Block a Port (TCP)

```bash
python firewall.py --block-port 8080 --protocol tcp
```

### Unblock a Port (UDP)

```bash
python firewall.py --unblock-port 53 --protocol udp
```

### List Firewall Rules

```bash
python firewall.py --list
```

### Reset Firewall Rules

```bash
python firewall.py --reset
```

## ⚠️ Requirements

- **Linux:** Requires `iptables` (pre-installed on most distros).
- **Windows:** Requires administrative privileges to use `netsh`.

## 📝 License

This project is licensed under the **MIT License**.
