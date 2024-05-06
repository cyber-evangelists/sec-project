import subprocess
import os
from remove import remove_from_html
# from removeone import remove_tags

def run_scan(report_file="Report.html"):
    
    
   
    url=input("--> Please enter your url: ")
    print('Advance Scan has started..')
    print('The results will be saved in Report.html in this folder..')
   
    host_directory = os.getcwd()
    
    
    command = [
        "docker",
        "run",
        "-t",
        "-v", f"{host_directory}:/zap/wrk",
        "ghcr.io/zaproxy/zaproxy:stable",
        "zap-full-scan.py",
        "-t",
        url,
        "-r",
        f"/zap/wrk/{report_file}"
    ]
    try:
        subprocess.run(command, check=True)
        remove_from_html('Report.html')
        # remove_tags('Report.html')
        
        print('The report of these vulnerabilities has been created in the folder')
    except subprocess.CalledProcessError as e:
        pass
