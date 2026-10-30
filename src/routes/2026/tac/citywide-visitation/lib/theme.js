// shared colours, region lookups and formatters for the citywide-visitation graphics.
// colours are the site's brand colours (src/assets/global-styles.css)

export const INK = "#191919"; // brandGray90
export const MUTED = "#727272"; // brandGray60
export const GRID = "#E3E4DF"; // lighter tint of brandGray
export const WITHIN = "#D0D1C9"; // brandGray: activity inside the home ward
export const OUTSIDE = "#007FA3"; // brandMedBlue: activity outside the home ward
export const VISITORS = "#DC4633"; // brandRed: venue activity arriving from outside

// one colour per Community Council region (used in tooltips and on the Figure 5 map)
export const REGIONS = [
	{ name: "Toronto and East York", short: "Toronto and East York", colour: "#6FC7EA" }, // brandLightBlue
	{ name: "Etobicoke York", short: "Etobicoke York", colour: "#EBA00F" }, // brandOrange
	{ name: "North York", short: "North York", colour: "#00A189" }, // brandMedGreen
	{ name: "Scarborough", short: "Scarborough", colour: "#AB1368" } // brandPink
];

// faint wash of a hex colour (map ward fills)
export const tint = (hex, alpha = 0.16) => hex + Math.round(alpha * 255).toString(16).padStart(2, "0");

export const regionOf = (name) => REGIONS.find((r) => r.name === name);

// anything that would round to 100% reads ">99%" so a share is never claimed to be exactly all of the activity
export const pct = (v, digits = 0) => (v >= 0.995 && v < 1.0000001 ? ">99%" : `${(v * 100).toFixed(digits)}%`);


// tooltip position (px) relative to the figure body, from a mouse or focus event on a chart element
export function tipPos(e) {
	const body = e.currentTarget.closest(".body").getBoundingClientRect();
	if (e.type === "focus") {
		const r = e.currentTarget.getBoundingClientRect();
		return { x: r.left + r.width / 2 - body.left, y: r.top + r.height / 2 - body.top };
	}
	return { x: e.clientX - body.left, y: e.clientY - body.top };
}

// split a label onto two lines at the last space or hyphen that fits within n characters
export function wrapLabel(text, n) {
	if (text.length <= n) return [text];
	const cut = Math.max(text.lastIndexOf(" ", n), text.lastIndexOf("-", n - 1));
	if (cut < 1) return [text];
	return text[cut] === " " ? [text.slice(0, cut), text.slice(cut + 1)] : [text.slice(0, cut + 1), text.slice(cut + 1)];
}

// axis tick label, where 1 really is 100%
export const tick = (t) => `${Math.round(t * 100)}%`;
