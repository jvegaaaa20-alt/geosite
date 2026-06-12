
import os
import requests
from flask import Flask, render_template, abort, request, jsonify

app = Flask(__name__)

ALLOWED_GEO = {"US", "CA", "DE", "FR", "IT", "AU", "GB"}
PROXYCHECK_KEY = os.environ.get("PROXYCHECK_KEY", "")

def get_country_ipapi(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode", timeout=3)
        return r.json().get("countryCode", "").upper()
    except:
        return ""

def check_ip(ip):
    try:
        key = PROXYCHECK_KEY
        url = f"https://proxycheck.io/v2/{ip}?vpn=1&key={key}" if key else f"https://proxycheck.io/v2/{ip}?vpn=1"
        r = requests.get(url, timeout=4)
        data = r.json()
        if data.get("status") != "ok":
            return get_country_ipapi(ip), False
        ip_data = data.get(ip, {})
        is_vpn = ip_data.get("proxy") == "yes"
        country = ip_data.get("isocode", "").upper()
        if not country:
            country = get_country_ipapi(ip)
        return country, is_vpn
    except:
        return get_country_ipapi(ip), False

def get_client_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if ip:
        ip = ip.split(",")[0].strip()
    return ip

def get_socials():
    all_socials = [
        {"key": "INSTAGRAM", "title": "Instagram", "icon": "instagram", "url": os.environ.get("INSTAGRAM_URL", "")},
        {"key": "TELEGRAM",  "title": "Telegram",  "icon": "telegram",  "url": os.environ.get("TG_LINK", "")},
        {"key": "TIKTOK",    "title": "TikTok",    "icon": "tiktok",    "url": os.environ.get("TIKTOK_URL", "")},
        {"key": "TWITTER",   "title": "Twitter/X", "icon": "twitter",   "url": os.environ.get("TWITTER_URL", "")},
        {"key": "YOUTUBE",   "title": "YouTube",   "icon": "youtube",   "url": os.environ.get("YOUTUBE_URL", "")},
        {"key": "ONLYFANS",  "title": "OnlyFans",  "icon": "onlyfans",  "url": os.environ.get("ONLYFANS_URL", "")},
    ]
    return [s for s in all_socials if s["url"].strip()]

@app.route("/")
def index():
    ip = get_client_ip()
    country, is_vpn = check_ip(ip)
    if is_vpn or country not in ALLOWED_GEO:
        abort(404)
    context = {
        "tg_link":     os.environ.get("TG_LINK", ""),
        "name":        os.environ.get("SITE_NAME", "Your Name"),
        "handle":      os.environ.get("SITE_HANDLE", ""),
        "hero_url":    os.environ.get("HERO_URL", ""),
        "banner_url":  os.environ.get("BANNER_URL", ""),
        "banner_text": os.environ.get("BANNER_TEXT", "Exclusive content here 🤍✨"),
        "photo1":      os.environ.get("PHOTO1_URL", ""),
        "photo2":      os.environ.get("PHOTO2_URL", ""),
        "photo3":      os.environ.get("PHOTO3_URL", ""),
        "socials":     get_socials(),
    }
    return render_template("index.html", **context)

@app.route("/check")
def check():
    ip = get_client_ip()
    country, is_vpn = check_ip(ip)
    return jsonify({"ip": ip, "country": country, "is_vpn": is_vpn, "allowed": country in ALLOWED_GEO and not is_vpn})

@app.errorhandler(404)
def not_found(e):
    return "", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
