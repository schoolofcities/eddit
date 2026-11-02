// map helpers for the Story 2 locator map

// equirectangular projection for a [lonMin, latMin, lonMax, latMax] window drawn cw px wide;
// longitude is stretched by cos(latitude) so the map is not squashed
export function projector(win, cw) {
	const [x0, y0, x1, y1] = win;
	const kx = Math.cos((((y0 + y1) / 2) * Math.PI) / 180);
	const k = cw / ((x1 - x0) * kx);
	return {
		height: Math.round((y1 - y0) * k),
		px: ([lon, lat]) => [(lon - x0) * kx * k, (y1 - lat) * k]
	};
}

export const ringsPath = (rings, px) => rings.map((r) => "M" + r.map((c) => px(c).map((v) => v.toFixed(1)).join(",")).join("L") + "Z").join("");
