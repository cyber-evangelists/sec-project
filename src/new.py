from fastapi import FastAPI, HTTPException
import nmap

app = FastAPI()
nmScan = nmap.PortScanner()

@app.get("/nmap-scan/")
async def nmap_scan(ip: str, start_port: int = 21, end_port: int = 443):
    if not (0 < start_port <= 65535 and 0 < end_port <= 65535):
        raise HTTPException(status_code=400, detail="Invalid port range")

    result = nmScan.scan(ip, f"{start_port}-{end_port}")
    
    return result

    # scanned_ports = {}
    # for protocol in result['scan'][ip]:
    #     scanned_ports[protocol] = []
    #     for port in result['scan'][ip][protocol]:
    #         scanned_ports[protocol].append({
    #             "port": port,
    #             "state": result['scan'][ip][protocol][port]['state'],
    #             "name": result['scan'][ip][protocol][port]['name'],
    #             "product_version": f"{result['scan'][ip][protocol][port]['product']} {result['scan'][ip][protocol][port]['version']}"
    #         })

    # return scanned_ports
