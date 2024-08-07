import nmap

def scan_ports(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1024')  # Pindai port 1-1024
    open_ports = []
    for proto in nm[ip].all_protocols():
        ports = nm[ip][proto].keys()
        for port in ports:
            if nm[ip][proto][port]['state'] == 'open':
                open_ports.append(port)
    return open_ports
