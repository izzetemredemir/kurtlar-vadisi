import os
import sys
import subprocess
import requests

def Whois(url):
    return requests.get("http://api.hackertarget.com/whois/?q=" + url).text

def Traceroute(url):
    return requests.get("https://api.hackertarget.com/mtr/?q= "+ url).text

def DnsLookup(url):
   return requests.get("http://api.hackertarget.com/dnslookup/?q=" + url).text

def ReverseDnsLookup(url):
    return requests.get("https://api.hackertarget.com/reversedns/?q=" + url).text

def GeoIPLookup(url):
    return requests.get("http://api.hackertarget.com/geoip/?q=" + url).text

def PortScan(url):
    return requests.get("http://api.hackertarget.com/nmap/?q=" + url).text

def ReverseIpLookup(url):
    return requests.get("http://api.hackertarget.com/reverseiplookup/?q=" + url).text


test= Whois(r"haber18.com")
a = test.replace("\n", "<br> ")
print(a)
