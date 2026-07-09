import os
import requests
from flask import Flask, render_template, request, jsonify, redirect

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

    main_link    = os.environ.get("MAIN_LINK", "")      # разрешённое гео
    fallback_link = os.environ.get("FALLBACK_LINK", "") # всё остальное

    if country in ALLOWED_GEO:
        cta_link = main_link
    else:
        cta_link = fallback_link

    context = {
        "name":     os.environ.get("SITE_NAME", "Lily"),
        "subtitle": os.environ.get("SITE_SUBTITLE", "Check my exclusive content ❤️"),
        "hero_url": os.environ.get("HERO_URL", ""),
        "cta_text": os.environ.get("CTA_TEXT", "Exclusive content here"),
        "cta_link": cta_link,
        "ga_id":    os.environ.get("GA_ID", ""),
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
