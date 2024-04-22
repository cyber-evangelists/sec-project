import argparse
import nmap

def scan(ip, start_port=1, end_port=1024):
    if not (0 < start_port <= 65535 and 0 < end_port <= 65535):
        print("Invalid port range")
        return

    nmScan = nmap.PortScanner()
    result = nmScan.scan(ip, f"{start_port}-{end_port}")

    filtered_ports = []

    for port, details in result["scan"][ip]["tcp"].items():
        product_version = f"{details['product']} {details['version']}"
        if details["state"] == "open" and details["name"] == "ftp":
            filtered_ports.append({
                "port": port,
                "state": details["state"],
                "name": details["name"],
                "product_version": product_version
            })
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Nmap scanner for FTP ports")
    parser.add_argument("ip", help="IP address to scan")
    parser.add_argument("--start-port", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="End port (default: 1024)")
    args = parser.parse_args()

    result = scan(args.ip, args.start_port, args.end_port)
    print(result)
