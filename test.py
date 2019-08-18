import nmap

def nmapScan(host,port):
    nm = nmap.PortScanner()
    nm.scan(host)
    nm.scaninfo()
    liste=[]

    for host in nm.all_hosts():
        liste.append('Host : %s (%s)' % (host, nm[host].hostname()))
        liste.append('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            liste.append('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            for port in lport:
                liste.append('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    return liste

print(nmapScan('192.168.1.1','80'))

