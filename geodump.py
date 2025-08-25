import argparse
import json
import logging
import sqlite3
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def export_geojson(db_file: str, output_file: str, table: str = "Locations"):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute(f"SELECT geodata FROM {table}")
    features = []

    for row in cur:
        try:
            js = json.loads(row[0])
        except Exception as e:
            logging.warning(f"Failed to parse JSON row: {e}")
            continue

        if "features" not in js or len(js["features"]) == 0:
            continue
        
        feat = js["features"][0]
        features.append(feat)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=2)

    cur.close()
    conn.close()

    logging.info(f"{len(features)} features written to {output_file}")
    logging.info("You can now load this file into Leaflet.js, Mapbox, or QGIS.")

def main():
    parser = argparse.ArgumentParser(description="Export geocoded data from SQLite to GeoJSON")
    parser.add_argument("--db", default="opengeo.sqlite", help="SQLite database file")
    parser.add_argument("--output", default="where.geojson", help="Output GeoJSON file")
    parser.add_argument("--table", default="Locations", help="Table name containing geodata")

    args = parser.parse_args()
    export_geojson(args.db, args.output, args.table)

if __name__ == "__main__":
    main()
