import argparse
import platform
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    """Execute system command and handle errors."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        logging.info(result.stdout)
    if result.stderr:
        logging.error(result.stderr)

def block_ip(ip):
    """Block a specific IP address."""
    if platform.system() == "Linux":
        run_command(f"sudo iptables -A INPUT -s {ip} -j DROP")
        run_command(f"sudo iptables -A OUTPUT -d {ip} -j DROP")
    elif platform.system() == "Windows":
        run_command(f"netsh advfirewall firewall add rule name=\"Block IP {ip}\" dir=both action=block remoteip={ip}")
    logging.info(f"Blocked IP: {ip}")

def unblock_ip(ip):
    """Unblock a specific IP address."""
    if platform.system() == "Linux":
        run_command(f"sudo iptables -D INPUT -s {ip} -j DROP")
        run_command(f"sudo iptables -D OUTPUT -d {ip} -j DROP")
    elif platform.system() == "Windows":
        run_command(f"netsh advfirewall firewall delete rule name=\"Block IP {ip}\" remoteip={ip}")
    logging.info(f"Unblocked IP: {ip}")

def block_port(port, protocol="tcp"):
    """Block a specific port with optional protocol."""
    if platform.system() == "Linux":
        run_command(f"sudo iptables -A INPUT -p {protocol} --dport {port} -j DROP")
        run_command(f"sudo iptables -A OUTPUT -p {protocol} --sport {port} -j DROP")
    elif platform.system() == "Windows":
        run_command(f"netsh advfirewall firewall add rule name=\"Block Port {port}\" dir=both action=block protocol={protocol.upper()} localport={port}")
    logging.info(f"Blocked Port: {port} ({protocol})")

def unblock_port(port, protocol="tcp"):
    """Unblock a specific port with optional protocol."""
    if platform.system() == "Linux":
        run_command(f"sudo iptables -D INPUT -p {protocol} --dport {port} -j DROP")
        run_command(f"sudo iptables -D OUTPUT -p {protocol} --sport {port} -j DROP")
    elif platform.system() == "Windows":
        run_command(f"netsh advfirewall firewall delete rule name=\"Block Port {port}\" protocol={protocol.upper()} localport={port}")
    logging.info(f"Unblocked Port: {port} ({protocol})")

def list_rules():
    """List current firewall rules."""
    if platform.system() == "Linux":
        run_command("sudo iptables -L --line-numbers")
    elif platform.system() == "Windows":
        run_command("netsh advfirewall firewall show rule name=all")

def reset_firewall():
    """Reset firewall rules to default."""
    if platform.system() == "Linux":
        run_command("sudo iptables --flush")
        run_command("sudo iptables --delete-chain")
    elif platform.system() == "Windows":
        run_command("netsh advfirewall reset")
    logging.info("Firewall rules reset to default.")

def main():
    parser = argparse.ArgumentParser(description="Advanced Firewall to Block IPs and Ports")
    parser.add_argument("--block-ip", help="Block a specific IP address")
    parser.add_argument("--unblock-ip", help="Unblock a specific IP address")
    parser.add_argument("--block-port", help="Block a specific port")
    parser.add_argument("--unblock-port", help="Unblock a specific port")
    parser.add_argument("--protocol", choices=["tcp", "udp"], default="tcp", help="Specify protocol for port blocking (default: tcp)")
    parser.add_argument("--list", action="store_true", help="List firewall rules")
    parser.add_argument("--reset", action="store_true", help="Reset firewall rules to default")
    
    args = parser.parse_args()
    
    if args.block_ip:
        block_ip(args.block_ip)
    elif args.unblock_ip:
        unblock_ip(args.unblock_ip)
    elif args.block_port:
        block_port(args.block_port, args.protocol)
    elif args.unblock_port:
        unblock_port(args.unblock_port, args.protocol)
    elif args.list:
        list_rules()
    elif args.reset:
        reset_firewall()
    else:
        print("Use --help for available options.")

if __name__ == "__main__":
    main()
