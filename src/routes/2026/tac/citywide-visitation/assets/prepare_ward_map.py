"""Builds ward_map.json for the Scarborough flow map (Figure 5).

Reads the ward polygons from the analysis repo, keeps the wards that fall inside the map window,
simplifies them and stores rings plus one point guaranteed to lie inside each ward.
Run from anywhere:  python3 prepare_ward_map.py <city-wards.geo.json> <ward_reach.json> <out ward_map.json>
"""
import json, sys
import geopandas as gpd

src, reach, out = sys.argv[1:4]
BBOX = (-79.50, 43.58, -79.05, 43.90)  # lon min, lat min, lon max, lat max
TOL = 0.0004                            # simplification tolerance in degrees (~35 m)

region = {w["ward_name"]: w["region"] for w in json.load(open(reach))["wards"]}
g = gpd.read_file(src).to_crs(4326)
g = g[g.geom_type.isin(["Polygon", "MultiPolygon"])]  # the file also holds boundary lines
g["region"] = g["ward_name"].map(region)
assert g["region"].notna().all(), g[g["region"].isna()]["ward_name"].tolist()
g = g.cx[BBOX[0]:BBOX[2], BBOX[1]:BBOX[3]]

wards = []
for _, r in g.iterrows():
    pt = r.geometry.representative_point()
    geom = r.geometry.simplify(TOL, preserve_topology=True)
    polys = [geom] if geom.geom_type == "Polygon" else list(geom.geoms)
    rings = [[[round(x, 4), round(y, 4)] for x, y in p.exterior.coords] for p in polys if p.area > 1e-6]
    wards.append({"name": r["ward_name"], "region": r["region"], "point": [round(pt.x, 4), round(pt.y, 4)], "rings": rings})

json.dump({"bbox": BBOX, "wards": wards}, open(out, "w"), separators=(",", ":"))
print(len(wards), "wards written")
