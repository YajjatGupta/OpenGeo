```markdown
# 🌍 OpenGeo Project  
**Geocoding + Mapping with Python & Leaflet.js**

The **OpenGeo Project** is an interactive geocoding and mapping tool that combines Python for data processing with Leaflet.js for visualization. It allows users to convert addresses into geographic coordinates, store results in an SQLite database, export data into GeoJSON (compatible with GIS tools like QGIS, Mapbox, Leaflet), and visualize results on an interactive web map with marker clustering. This project is adapted and extended from Dr. Charles Severance’s (“Dr. Chuck”) *Python for Everybody* course.

---

## ⚡ Key Features
- 🗺️ Convert addresses into latitude/longitude using geocoding
- 💾 Store results persistently in SQLite
- 🌐 Export results to GeoJSON for GIS compatibility
- 📍 Interactive visualization using Leaflet.js and marker clustering
- 🔎 Search and navigate across mapped locations
- 🔒 Clear separation between Python data processing and HTML/JS visualization

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

## 🛠️ Installation and Requirements
Clone the repository and install the dependencies:  
```bash
git clone https://github.com/<your-username>/opengeo-project.git
cd opengeo-project
pip install -r requirements.txt
````

Requirements:

* Python 3.8+
* `requests` (for geocoding API calls)

You can install manually with:

```bash
pip install requests
```

---

## 🚀 Usage Guide

1. **Load Addresses into SQLite**
   Use `geoload.py` to read addresses from `where.data` and fetch geocoded data:

   ```bash
   python geoload.py --input where.data --db opengeo.sqlite --limit 200
   ```

   Options:

   * `--input` : Input file containing addresses
   * `--db` : SQLite database file
   * `--limit` : Max records to fetch

2. **Export Data to GeoJSON**
   Convert the stored results into a `.geojson` file:

   ```bash
   python geodump.py --db opengeo.sqlite --output where.geojson
   ```

3. **Visualize on Map**
   Open `index.html` in your browser to explore the interactive map.
   Features include zooming and panning, marker clustering for readability, and clickable markers to view details.

---

## 📌 Example Workflow

1. Add addresses to `where.data`
2. Run `geoload.py` → store geocoded results in `opengeo.sqlite`
3. Run `geodump.py` → export to `where.geojson`
4. Open `index.html` → view results interactively 🎉

---

## 🙏 Credits and License

This project is based on and inspired by **Dr. Charles Severance (“Dr. Chuck”)** from his *Python for Everybody* course, and extended with marker clustering and improved visualization.

License: **MIT License** — free to use, modify, and share.

```
