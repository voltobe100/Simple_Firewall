import os
import platform
import argparse

def block_ip(ip):
    if platform.system() == "Linux":
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
        print(f"Blocked IP: {ip} using iptables.")
    elif platform.system() == "Windows":
        os.system(f'netsh advfirewall firewall add rule name="Block {ip}" dir=in action=block remoteip={ip}')
        print(f"Blocked IP: {ip} using Windows Firewall.")
    else:
        print("Unsupported OS.")

def block_port(port):
    if platform.system() == "Linux":
        os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")
        print(f"Blocked Port: {port} using iptables.")
    elif platform.system() == "Windows":
        os.system(f'netsh advfirewall firewall add rule name="Block Port {port}" dir=in action=block protocol=TCP localport={port}')
        print(f"Blocked Port: {port} using Windows Firewall.")
    else:
        print("Unsupported OS.")

def main():
    parser = argparse.ArgumentParser(description="Simple Firewall Script")
    parser.add_argument("-ip", "--block-ip", help="IP address to block")
    parser.add_argument("-p", "--block-port", type=int, help="Port number to block")
    
    args = parser.parse_args()

    if args.block_ip:
        block_ip(args.block_ip)
    if args.block_port:
        block_port(args.block_port)

if __name__ == "__main__":
    main()
