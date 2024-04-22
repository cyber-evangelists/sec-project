import argparse
import nmap
import docker
import re

def scan(ip: str, start_port: int = 1, end_port: int = 1024):
    if not (0 < start_port <= 65535 and 0 < end_port <= 65535):
        raise ValueError("Invalid port range")

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
    product_versions = ", ".join(port["product_version"] for port in filtered_ports)
    container_name = 'quirky_khorana'
    half_command = 'searchsploit'
    full_command = f"{half_command} {product_versions}"

    output = run_command_in_container(container_name, full_command)
    return output

def run_command_in_container(container_name, command):
    client = docker.from_env()
    container = client.containers.get(container_name)
    exec_command = f"bash -c '{command}'"
    exec_response = container.exec_run(exec_command)
    return exec_response.output.decode('utf-8')

def extract_py_files(output):
    py_files = []
    lines = output.split('\n')
    for line in lines:
        if '.py' in line:
            match = re.search(r'\| (.+\.py)', line)
            if match:
                py_files.append(match.group(1))
    return py_files

def main():
    parser = argparse.ArgumentParser(description="Scan for open FTP ports and search for exploits in a Docker container.")
    parser.add_argument("ip", type=str, help="IP address to scan")
    parser.add_argument("--start-port", type=int, default=1, help="Start port for scanning (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="End port for scanning (default: 1024)")
    args = parser.parse_args()

    try:
        output = scan(args.ip, args.start_port, args.end_port)
        py_files = extract_py_files(output)
        if py_files:
            print("Found Python exploit files:")
            for file in py_files:
                print(file)
        else:
            print("No Python exploit files found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
