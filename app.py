import os
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ALLOWED_GEO = set(os.environ.get("ALLOWED_GEO", "US,GB,CA,AU,DE,FR,IT,NL,CH,AT,SE,NO,DK,FI").upper().split(","))

def get_country(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode", timeout=3)
        return r.json().get("countryCode", "").upper()
    except:
        return ""

def get_client_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if ip:
        ip = ip.split(",")[0].strip()
    return ip

@app.route("/")
def index():
    ip = get_client_ip()
    country = get_country(ip)
    allowed = country in ALLOWED_GEO

    context = {
        "name":     os.environ.get("SITE_NAME", "Model Name"),
        "subtitle": os.environ.get("SITE_SUBTITLE", ""),
        "hero_url": os.environ.get("HERO_URL", ""),
        "cta_text": os.environ.get("CTA_TEXT", "Exclusive content here"),
        "cta_link": os.environ.get("MAIN_LINK", ""),
        "tg_link":  os.environ.get("TG_LINK", ""),
        "ga_id":    os.environ.get("GA_ID", ""),
        "allowed":  allowed,
    }
    return render_template("index.html", **context)

@app.route("/check")
def check():
    ip = get_client_ip()
    country = get_country(ip)
    return jsonify({"ip": ip, "country": country, "allowed": country in ALLOWED_GEO})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
