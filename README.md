# Simple Firewall

A Python script to block specific IPs or ports using `iptables` (Linux) or Windows Firewall API.

## Features

- Block an IP address
- Block a specific port
- Works on both Linux and Windows

## Requirements

- Python 3
- Administrator/root privileges

## Usage

Run the script with the following options:

```bash
python simple_firewall.py -ip <IP_ADDRESS>
```

To block a port:

```bash
python simple_firewall.py -p <PORT_NUMBER>
```

### Examples

- Block IP `192.168.1.100`:
  ```bash
  python simple_firewall.py -ip 192.168.1.100
  ```
- Block port `80`:
  ```bash
  python simple_firewall.py -p 80
  ```

## Notes

- On Linux, this uses `iptables`, so you need `sudo` privileges.
- On Windows, this uses `netsh advfirewall`, so you must run the script as Administrator.
- To unblock an IP or port, use:
  - Linux: `sudo iptables -D INPUT -s <IP> -j DROP` or `sudo iptables -D INPUT -p tcp --dport <PORT> -j DROP`
  - Windows: `netsh advfirewall firewall delete rule name='Block <IP>'` or `netsh advfirewall firewall delete rule name='Block Port <PORT>'`

## License

This project is licensed under the MIT License.
