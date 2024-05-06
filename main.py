from tabulate import tabulate
from NetworkAnalysis import networkDiscovery, portAnalysis, Detection
from VulnerabilityAnalysis import vulnerabilityScanner
from Scan import run_scan

def main_menu():
    print("\nMenu:")
    print("1. Network Analysis")
    print("2. Vulnerability Analysis")
    print("3. Password Security Analysis")
    print("4. Exit")

def network_analysis_menu():
    print("\nNetwork Discovery Menu:")
    print("1. Network Discovery")
    print("2. Port Scanning")
    print("3. Detect Connected Devices")
    print("4. Back to Main Menu")

def vulnerability_analysis_menu():
    print("\nVulnerability Analysis Menu:")
    print("1. Vulnerability Scanner")
    print("2. Advance Scan")
    print("3. Back to Main Menu")
    
def password_security_menu():
    print("1.  Brute Force Attack Resistance Tests")
    print("2.  Back to Main Menu")
    


def main():
    while True:
        main_menu()
        choice = input("-> Enter your choice: ")

        if choice == '1':
            while True:
                network_analysis_menu()
                sub_choice = input("-> Enter your choice: ")
                if sub_choice == '1':
                    networkDiscovery()
                elif sub_choice == '2':
                    portAnalysis()
                elif sub_choice == '3':
                     Detection()
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid choice. Please choose again.")
        elif choice == '2':
            while True:
                vulnerability_analysis_menu()
                sub_choice = input("-> Enter your choice: ")
                if sub_choice == '1':
                    vulnerabilityScanner()
                elif sub_choice == '2':
                    run_scan()
                else:
                    print("-> Invalid choice. Please choose again.")
        elif choice == '3':
            while True:
                password_security_menu()
                sub_choice = input("-> Enter your choice: ")
                if sub_choice == '1':
                    pass
                elif sub_choice == '2':
                    break
                else:
                    print("-> Invalid choice. Please choose again.")
        elif choice == '4':
            print("Exiting [+]")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
