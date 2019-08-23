from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,SelectField
import nmap
import os
import domain

app = Flask(__name__)
app.secret_key="İstanbul'un son sefiri Süleyman Çakır."

class NmForm(Form):
    host = StringField('host')
    port = StringField('port')

class DomainForm(Form):
    host = StringField('host')
    select = SelectField('select')

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

@app.route("/",methods=["GET","POST"])
def index():
    nm = nmap.PortScanner()
    NmVersion = nm.nmap_version()
    form = NmForm(request.form)
    if request.method == "POST":
        host = form.host.data
        port = form.port.data
        ScanReport = nmapScan(host, port)
        return render_template("index.html", versiyon=NmVersion, form=form,report=ScanReport)
    else:
        return render_template("index.html", versiyon=NmVersion, form=form)

@app.route("/domain",methods=["GET","POST"])
def DomainModule():
    form = DomainForm(request.form)
    if request.method == "POST":
        host = form.host.data
        select = form.select.data
        if select == "Whois":
             ScanReport = domain.Whois(host)
        elif select == "Traceroute":
            ScanReport = domain.Traceroute(host)
        elif select == "DnsLookup":
            ScanReport = domain.DnsLookup(host)
        elif select == "ReverseDnsLookup":
            ScanReport = domain.ReverseDnsLookup(host)
        elif select == "GeoIPLookup":
            ScanReport = domain.GeoIPLookup(host)
        elif select == "PortScan":
            ScanReport = domain.PortScan(host)
        elif select == "ReverseIpLookup":
            ScanReport = domain.ReverseIpLookup(host)
        else:
            pass
        ScanReport = ScanReport.replace("\n", "<br> ")
        return render_template("domain.html", form=form, report=ScanReport,host=host,select=select)
    else:
        return render_template("domain.html" , form=form)


if __name__ == "__main__":
    app.run(debug=True)


