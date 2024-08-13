import nmap
import argparse

nm = nmap.PortScanner()

def scan_hosts(target, ports, output):
    nm.scan(target, ports)
    with open(output, 'w') as o:
        for host in nm.all_hosts():
            o.write(f'Host: {host} ({nm[host].hostname()})')
            o.write(f'State: {nm[host].state()}')
            for proto in nm[host].all_protocols():
                o.write(f'----------\nProtocol: {proto}')
                lport = nm[host][proto].keys()
                for port in lport:
                    o.write(f'port : {port}\tstate : {nm[host][proto][port]["state"]}')
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate Nmap Scans with Python")
    parser.add_argument("target", help="Target IP address or range")
    parser.add_argument("ports", help="Port or range of ports to scan", nargs='?', default="1-65535")
    args = parser.parse_args()

    scan_hosts(args.target, args.ports, )
