import { error } from '@sveltejs/kit';
import { resolve } from '$app/paths';

// Every case study that used to live at the site root before moving under /2024/.
// Each one is prerendered as a static redirect page (the site is hosted statically,
// so we can't send a real HTTP 301).
const LEGACY_SLUGS = [
	'albuquerque-nm',
	'bridgeport-ct',
	'champaign-il',
	'cook-county-il',
	'eau-claire-wi',
	'greensboro-nc',
	'halifax-ns',
	'high-point',
	'high-point-nc',
	'wood-buffalo-ab',
	'worcester-ma'
];

export const prerender = true;

export function entries() {
	return LEGACY_SLUGS.map((slug) => ({ slug }));
}

export function load({ params }) {
	if (!LEGACY_SLUGS.includes(params.slug)) {
		error(404, 'Not found');
	}
	return { target: resolve(/** @type {any} */ (`/2024/${params.slug}`)) };
}
