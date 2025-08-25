```markdown
# 🌍 OpenGeo Project

An interactive **Geocoding + Mapping** project built in Python & Leaflet.js.  
It reads addresses, geocodes them, stores results in SQLite, exports data into **GeoJSON**, and visualizes locations on a web-based interactive map.  

This project is adapted and extended from **Dr. Charles Severance (“Dr. Chuck”) Python for Everybody course**.

---

## ⚡ Features
- 🗺️ Convert addresses into geographic coordinates
- 📦 Store results in SQLite for persistence
- 🌐 Export location data as GeoJSON (compatible with QGIS, Mapbox, Leaflet)
- 📍 Visualize results with **Leaflet.js** & **Marker Clustering**
- 🔎 Search functionality for easy navigation
- 🔒 Clean separation of **data processing (Python)** and **map visualization (HTML/JS)**

---

## 📂 Project Structure

```

opengeo-project/
│── geoload.py        # Load & geocode addresses, save results in SQLite
│── geodump.py        # Export geocoded data from SQLite to GeoJSON
│── index.html        # Interactive map (Leaflet.js)
│── where.data        # Sample input file containing addresses
│── where.geojson     # Exported GeoJSON (generated file)
│── opengeo.sqlite    # SQLite database (generated file)
│── README.md         # Documentation
│── requirements.txt  # Python dependencies
│── .gitignore        # Ignore DB & generated files

````

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/opengeo-project.git
cd opengeo-project
````

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Load Addresses into SQLite

Read addresses from `where.data` and fetch geocoded data:

```bash
python geoload.py --input where.data --db opengeo.sqlite --limit 200
```

* `--input` : Input file containing addresses
* `--db` : SQLite database file
* `--limit` : Max records to fetch

---

### 2. Export Data to GeoJSON

Convert database data into a `.geojson` file:

```bash
python geodump.py --db opengeo.sqlite --output where.geojson
```

---

### 3. Visualize on Map

Open **index.html** in your browser to explore the map.

* Zoom & pan across locations
* Markers are clustered for readability
* Click markers to view details

---

## 📦 Requirements

* Python 3.8
* `requests` (for geocoding API calls)

Install via:

```bash
pip install requests
```

Or from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 📌 Example Workflow

1. Add a list of addresses in `where.data`
2. Run `geoload.py` to fetch coordinates & save in `opengeo.sqlite`
3. Run `geodump.py` to export data into `where.geojson`
4. Open `index.html` to see results on an interactive map 🎉

---

## 🙏 Credits

This project is based on and inspired by **Dr. Charles Severance (“Dr. Chuck”)** from his *Python for Everybody* course.
Extended with additional features like marker clustering and cleaner map visualization.

---

## 🌐 License

MIT License — free to use, modify, and share.

```

---

