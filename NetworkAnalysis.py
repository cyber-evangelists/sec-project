import nmap
import subprocess
import docker
from decouple import config

container_Name = config("CONTAINER_NAME")
from tabulate import tabulate
def networkDiscovery():
    ip=input('-> Please Enter Ip Address or URL: ')
    command = f"nmap -sn {ip}"
    output=subprocess.run(command, shell=True)
    print(output)
    

def portAnalysis():
    ip=input('-> Please Enter Ip Address or URL: ')
    startPort=input("-> Please enter start port: ")
    endPort=input("-> Please enter start port: ")
    nmScan = nmap.PortScanner()
    result = nmScan.scan(ip, f"{startPort}-{endPort}")
    table_data = json_to_table(result)
    headers = ["IP Address", "Port", "Service Name", "State", "Product", "Version", "Extra Info", "Conf", "CPE"]
    print(tabulate(table_data, headers=headers))
    
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
        print("Scan could not be perfomred as FTP port is closed")
        return False
    half_command = 'searchsploit'
    full_command = f"{half_command} {product_versions}"
    print("\nThe vulnerability identified in the Scan is: ",product_versions)
    client = docker.from_env()
   
    container = client.containers.get(container_Name)
    exec_command = f"bash -c '{full_command}'"
    exec_response = container.exec_run(exec_command)
    print(exec_response.output.decode('utf-8'))
    print('-> If you want to exploit the vulnerability \t Press 1')
    exploit=input('-> Enter Input1>>')
    if exploit=='1':
       
        filename='49757.py'
        try:
            subprocess.run(['python3', filename, ip], check=True)
        except subprocess.CalledProcessError as e:
            pass
    else:
       pass
    
    
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

def Detection():
    ip=input('-> Please Enter Ip Address or URL: ')
    command = f"nmap -sP {ip}/24" 
   
    output=subprocess.run(command, shell=True)
    print(output)
  
    