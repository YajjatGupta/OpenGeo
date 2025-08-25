import argparse
import logging
import sqlite3
import json
import time
import ssl
import sys
import urllib.request
import urllib.parse

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def fetch_geodata(serviceurl: str, address: str, ctx: ssl.SSLContext) -> dict | None:
    """Fetch geodata from API for a given address."""
    parms = {"q": address}
    url = serviceurl + urllib.parse.urlencode(parms)
    logging.info(f"Retrieving {url}")

    try:
        with urllib.request.urlopen(url, context=ctx) as uh:
            data = uh.read().decode()
            logging.info(f"Retrieved {len(data)} characters")
    except Exception as e:
        logging.error(f"Failed to retrieve {address}: {e}")
        return None

    try:
        js = json.loads(data)
        return js
    except Exception as e:
        logging.error(f"JSON parsing failed for {address}: {e}")
        return None

def load_addresses(input_file: str, db_file: str, serviceurl: str, limit: int):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Locations (
            address TEXT PRIMARY KEY,
            geodata TEXT
        )
    """)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    with open(input_file) as fh:
        count = 0
        nofound = 0

        for line in fh:
            if limit and count >= limit:
                logging.info(f"Reached limit of {limit} records. Stopping.")
                break

            address = line.strip()
            if not address:
                continue

            cur.execute("SELECT geodata FROM Locations WHERE address = ?", (address,))
            row = cur.fetchone()
            if row:
                logging.info(f"Found in database: {address}")
                continue

            js = fetch_geodata(serviceurl, address, ctx)
            if js is None:
                continue

            if not js or "features" not in js:
                logging.warning(f"Download error for {address}")
                continue

            if len(js["features"]) == 0:
                logging.warning(f"No features found for {address}")
                nofound += 1

            cur.execute(
                "INSERT OR REPLACE INTO Locations (address, geodata) VALUES (?, ?)",
                (address, json.dumps(js))
            )
            conn.commit()

            count += 1
            if count % 10 == 0:
                logging.info("Pausing for a bit to respect API limits...")
                time.sleep(5)

        if nofound > 0:
            logging.warning(f"{nofound} addresses could not be geocoded.")

    conn.close()
    logging.info("Finished loading addresses. Run geodump.py to export data for visualization.")

def main():
    parser = argparse.ArgumentParser(description="Load geocoded addresses into SQLite.")
    parser.add_argument("--input", default="where.data", help="Input file with addresses")
    parser.add_argument("--db", default="opengeo.sqlite", help="SQLite database file")
    parser.add_argument("--serviceurl", default="https://py4e-data.dr-chuck.net/opengeo?", help="Geocoding API endpoint")
    parser.add_argument("--limit", type=int, default=100, help="Max number of addresses to process")

    args = parser.parse_args()
    load_addresses(args.input, args.db, args.serviceurl, args.limit)


if __name__ == "__main__":
    main()
