# Kurtlar Vadisi

A small Flask web app that puts a browser front end on a few network reconnaissance tools: a local Nmap scan and a set of HackerTarget API lookups. It is for running basic recon from a web page instead of the command line. The interface is in Turkish.

> **Status:** archived. Built in 2019. Kept for reference, not maintained.

This is a tool for authorized security testing. Use it only against systems you own or are allowed to test.

![Nmap scan page](https://i.ibb.co/LPsTT8g/kurtlarvadisi.png)

## What it does

- **Nmap page** (`/`): takes a host, runs an Nmap scan through python-nmap and lists each host's state, protocols and port states. The form also has a port field, but its value is not passed to the scan.
- Shows the version of the Nmap binary installed on the machine.
- **Hacker Target API page** (`/domain`): sends a domain or IP to the HackerTarget web API and shows the response for one of 12 lookups: whois, traceroute (MTR), DNS lookup, reverse DNS, GeoIP, port scan, reverse IP, page links, HTTP headers, subnet calculator, zone transfer and host search. These lookups run on HackerTarget's servers, not on your machine.
- Bootstrap 4 interface built with Jinja templates and WTForms.

## Tech stack

- Python 3 (developed on 3.6), Flask, Jinja2, WTForms
- python-nmap (needs the `nmap` binary)
- requests, against the HackerTarget API
- Bootstrap 4, loaded from a CDN

## Running it locally

You need Python 3 and Nmap installed.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Then open http://127.0.0.1:5000.

- The versions pinned in `requirements.txt` date from 2019 and may need updating on newer Python versions.
- The committed `venv/` folder is a leftover Python 3.6 environment from the original machine. Create your own instead of using it.
- The app has no authentication and starts Flask in debug mode, so keep it bound to localhost.

## License

GNU General Public License v3.0, see [LICENSE](LICENSE).
