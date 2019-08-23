import nmap
import os
import sys
import domain

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

def Whois(url):
    return os.system("curl http://api.hackertarget.com/whois/?q=" + url)

def Traceroute(url):
    return os.system("curl https://api.hackertarget.com/mtr/?q=" + url)

def DnsLookup(url):
   return os.system("curl http://api.hackertarget.com/dnslookup/?q=" + url)

def ReverseDnsLookup(url):
    return os.system("curl https://api.hackertarget.com/reversedns/?q=" + url )

def GeoIPLookup(url):
    return os.system("curl http://api.hackertarget.com/geoip/?q=" + url )

def PortScan(url):
    return  os.system("curl http://api.hackertarget.com/nmap/?q=" + url )

def ReverseIpLookup(url):
    return os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + url)



print(type(domain))