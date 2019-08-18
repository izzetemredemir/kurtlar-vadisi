from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from wtforms import Form,StringField,TextAreaField,PasswordField,validators

import nmap

app = Flask(__name__)
app.secret_key="İstanbul'un son sefiri Süleyman Çakır."

class NmForm(Form):
    host = StringField('host')
    port = StringField('port')


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

if __name__ == "__main__":
    app.run(debug=True)
