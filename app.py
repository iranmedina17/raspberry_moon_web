from datetime import datetime, timezone, timedelta
from math import cos, fmod, pi

from flask import Flask, jsonify, render_template


app = Flask(__name__)

PHASE_NAMES = [
    "NEW MOON",
    "WAXING CRESCENT",
    "FIRST QUARTER",
    "WAXING GIBBOUS",
    "FULL MOON",
    "WANING GIBBOUS",
    "LAST QUARTER",
    "WANING CRESCENT",
]

SYNODIC_MONTH = 29.53058867
KNOWN_NEW_MOON_JD = 2451549.26  # Jan 6 2000 18:14 UTC


def unix_to_jd(timestamp):
    return 2440587.5 + timestamp / 86400.0


def moon_age_from_jd(jd):
    age = fmod(jd - KNOWN_NEW_MOON_JD, SYNODIC_MONTH)
    if age < 0:
        age += SYNODIC_MONTH
    return age


def moon_distance_km(jd):
    deg_to_rad = pi / 180.0
    t = (jd - 2451545.0) / 36525.0
    m = (357.52911 + 35999.05029 * t) * deg_to_rad
    mm = (134.9634 + 477198.8676 * t) * deg_to_rad
    d = (297.8502 + 445267.1115 * t) * deg_to_rad
    return (
        385000.56
        - 20905.355 * cos(mm)
        - 3699.111 * cos(2 * d - mm)
        - 2955.968 * cos(2 * d)
        - 569.925 * cos(2 * mm)
        + 246.158 * cos(2 * d - 2 * mm)
        - 204.586 * cos(m)
        - 170.733 * cos(2 * d + mm)
        - 152.138 * cos(2 * d - m - mm)
    )


def moon_data():
    now = datetime.now(timezone.utc)
    jd = unix_to_jd(now.timestamp())
    age = moon_age_from_jd(jd)
    illumination = 0.5 * (1.0 - cos(age / SYNODIC_MONTH * 2.0 * pi))
    phase_index = int((age / SYNODIC_MONTH) * 8.0 + 0.5) % 8

    to_full = SYNODIC_MONTH * 0.5 - age
    if to_full < 0:
        to_full += SYNODIC_MONTH

    days_to_full = int(to_full)
    hours_to_full = int((to_full - days_to_full) * 24.0)
    next_full = now + timedelta(days=to_full)

    return {
        "phaseName": PHASE_NAMES[phase_index],
        "phaseIndex": phase_index,
        "age": round(age, 2),
        "illumination": round(illumination, 4),
        "illuminationPercent": round(illumination * 100),
        "nextFullDate": next_full.strftime("%b %-d, %Y"),
        "daysToFull": days_to_full,
        "hoursToFull": hours_to_full,
        "distance": round(moon_distance_km(jd)),
        "date": now.strftime("%m/%d/%Y"),
    }


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/moon")
def api_moon():
    return jsonify(moon_data())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
