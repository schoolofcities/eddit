// flattens ward_stats.json into the fields the figures use
import { wards as raw, trend, meta } from "../assets/ward_stats.json";

const M = "labour_cultural_workers"; // headline workforce measure: broader cultural workers (NOC)

export const PRIORITY = meta.priority_wards; // Don Valley North, Willowdale, Eglinton-Lawrence, Don Valley West
export { trend };

export const wards = raw.map((w) => ({
	name: w.ward_name,
	region: w.region,
	priority: w.is_priority_ward,
	workers: w.workforce[M].count,
	locations: w.infrastructure.n_locations,
	per100k: w.infrastructure.locations_per_100k,
	tacFunded: w.infrastructure.n_tac_funded,
	highFreq: w.infrastructure.n_high_funding_freq,
	ratio: w.trend.workers_vs_trend_ratio,
	outsideShare: w.activity.outside_share
}));

export const byName = Object.fromEntries(wards.map((w) => [w.name, w]));

export const fmt = (v) => Math.round(v).toLocaleString("en-CA");

// definition of a cultural worker, used in the captions so a screenshot of a graphic stands on its own
export const DEFINITION =
	"Cultural workers are residents employed in cultural occupations (National Occupational Classification), such as artists, musicians and writers, and related technical, instructional and administrative roles. They are counted by where they live, not where they work.";
