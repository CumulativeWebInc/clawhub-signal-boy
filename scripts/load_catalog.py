#!/usr/bin/env python3
"""Signal Boy quickstart: load the 24-track CWI-1 Walkman cartridge.

Free lane, no credentials. Stdlib only. Exit 0 + "CARTRIDGE OK" on success.
"""
import json
import sys
import urllib.request

CARTRIDGE_URL = "https://cumulativewebinc.github.io/cwi-learn/walkman/cartridge.json"


SELF_SCAN = {
    "skill": "cwi/signal-boy",
    "version": "1.1.0",
    "network": ["https://cumulativewebinc.github.io/cwi-learn/walkman/cartridge.json"],
    "files_written": [],
    "env_read": [],
    "secrets_requested": [],
    "subprocess": ["curl (only when installed; stdlib urllib fallback otherwise)"],
}


def self_scan():
    """RoleCraft-style install-time self-declaration. Static: it names what the
    script does, so installers don't have to read every line to trust it."""
    print("SELF-SCAN: install-time self-declaration")
    for key, value in SELF_SCAN.items():
        print(f"  {key}: {value if value else 'none'}")
    return 0


def fetch(url, retries=2):
    """Fetch JSON. curl-first: this VM's Fastly path truncates Python-urllib
    bodies (IncompleteRead) while curl receives full bodies with
    Accept-Encoding: identity. urllib is the fallback."""
    import subprocess, shutil
    if shutil.which("curl"):
        last = None
        for _ in range(retries + 1):
            try:
                p = subprocess.run(
                    ["curl", "-sS", "--fail", "--max-time", "30",
                     "-H", "Accept-Encoding: identity",
                     "-A", "clawhub-skill/1.1.0", url],
                    capture_output=True, text=True, timeout=40)
                if p.returncode == 0:
                    return json.loads(p.stdout)
                last = RuntimeError(p.stderr.strip() or f"curl rc={p.returncode}")
            except Exception as e:
                last = e
        raise last
    last = None
    for _ in range(retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"Accept-Encoding": "identity",
                         "User-Agent": "clawhub-skill/1.1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            last = e
    raise last

def main():
    try:
        cart = fetch(CARTRIDGE_URL)
    except Exception as e:
        print(f"CARTRIDGE FAIL: could not fetch cartridge.json ({e})", file=sys.stderr)
        return 1
    tc = cart.get("track_count")
    tracks = cart.get("tracks", [])
    if tc != 24 or len(tracks) != 24:
        print(
            f"CARTRIDGE FAIL: track_count={tc}, len(tracks)={len(tracks)} "
            "(expected 24/24 — re-fetch once; if still mismatched, stop and report)",
            file=sys.stderr,
        )
        return 1
    artist = cart.get("artist", {}).get("name", "That Boy Hi Hat")
    t0 = tracks[0]
    zt = next((t for t in tracks if t.get("title") == "Zooted Zone"), None)
    zt_prod = (zt or {}).get("verified_credits", {}).get("producer", "undocumented")
    print(f"CARTRIDGE OK: {tc}/{len(tracks)} tracks · artist: {artist}")
    print(f"Track 1: {t0.get('title')}")
    print(f"Zooted Zone — producer (verified_credits): {zt_prod}")
    print("Rule armed: cite only fields present in the manifest.")
    return 0


if __name__ == "__main__":
    if "--self-scan" in sys.argv:
        sys.exit(self_scan())
    sys.exit(main())
