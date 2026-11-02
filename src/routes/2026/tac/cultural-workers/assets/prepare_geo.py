"""Builds ward_geo.json for the Story 2 locator map: all 25 wards as simplified rings, plus a point guaranteed to lie inside each ward.

Usage: python3 prepare_geo.py <city-wards.geo.json> <ward_stats.json> <out dir>
"""
import json, sys
from pathlib import Path
import geopandas as gpd

wards_path, stats_path, out = sys.argv[1:4]
out = Path(out)
TOL = 0.0003                              # simplification tolerance in degrees (~25 m)

region = {w["ward_name"]: w["region"] for w in json.load(open(stats_path))["wards"]}
g = gpd.read_file(wards_path).to_crs(4326)
g = g[g.geom_type.isin(["Polygon", "MultiPolygon"])]  # the file also holds boundary lines
g["region"] = g["ward_name"].map(region)
assert g["region"].notna().all()

wards = []
for _, r in g.iterrows():
    pt = r.geometry.representative_point()
    geom = r.geometry.simplify(TOL, preserve_topology=True)
    polys = [geom] if geom.geom_type == "Polygon" else list(geom.geoms)
    rings = [[[round(x, 4), round(y, 4)] for x, y in p.exterior.coords] for p in polys if p.area > 1e-7]
    wards.append({"name": r["ward_name"], "region": r["region"], "point": [round(pt.x, 4), round(pt.y, 4)], "rings": rings})
json.dump({"wards": wards}, open(out / "ward_geo.json", "w"), separators=(",", ":"))

print(len(wards), "wards written")
