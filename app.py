import os
import requests
from flask import Flask, render_template, abort, request, jsonify

app = Flask(__name__)

ALLOWED_GEO = {"US", "CA", "DE", "FR", "IT", "AU", "GB"}

def get_country(ip):
    try:
        r = requests.get(
            f"http://ip-api.com/json/{ip}?fields=countryCode",
            timeout=3
        )
        return r.json().get("countryCode", "")
    except:
        return ""

def get_client_ip():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if ip:
        ip = ip.split(",")[0].strip()
    return ip

def get_socials():
    """Собирает соцсети из env — только заполненные"""
    all_socials = [
        {"key": "INSTAGRAM",  "title": "Instagram",  "icon": "instagram",  "url": os.environ.get("INSTAGRAM_URL", "")},
        {"key": "TIKTOK",     "title": "TikTok",     "icon": "tiktok",     "url": os.environ.get("TIKTOK_URL", "")},
        {"key": "TWITTER",    "title": "Twitter / X", "icon": "twitter",   "url": os.environ.get("TWITTER_URL", "")},
        {"key": "YOUTUBE",    "title": "YouTube",    "icon": "youtube",    "url": os.environ.get("YOUTUBE_URL", "")},
        {"key": "ONLYFANS",   "title": "OnlyFans",   "icon": "onlyfans",   "url": os.environ.get("ONLYFANS_URL", "")},
        {"key": "PATREON",    "title": "Patreon",    "icon": "patreon",    "url": os.environ.get("PATREON_URL", "")},
        {"key": "WEBSITE",    "title": "Website",    "icon": "website",    "url": os.environ.get("WEBSITE_URL", "")},
    ]
    return [s for s in all_socials if s["url"].strip()]

@app.route("/")
def index():
    ip = get_client_ip()
    country = get_country(ip)
    if country not in ALLOWED_GEO:
        abort(404)

    context = {
        "tg_link":    os.environ.get("TG_LINK", ""),
        "name":       os.environ.get("SITE_NAME", "Your Name"),
        "bio":        os.environ.get("SITE_BIO", ""),
        "avatar_url": os.environ.get("AVATAR_URL", ""),
        "photo1":     os.environ.get("PHOTO1_URL", ""),
        "photo2":     os.environ.get("PHOTO2_URL", ""),
        "photo3":     os.environ.get("PHOTO3_URL", ""),
        "socials":    get_socials(),
    }
    return render_template("index.html", **context)

@app.route("/check")
def check():
    ip = get_client_ip()
    country = get_country(ip)
    return jsonify({"ip": ip, "country": country, "allowed": country in ALLOWED_GEO})

@app.errorhandler(404)
def not_found(e):
    return "", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
