import { sveltekit } from '@sveltejs/kit/vite';
import adapter from '@sveltejs/adapter-static';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [
		sveltekit({
			adapter: adapter({
				pages: 'docs',
				assets: 'docs'
			}),
			paths: {
				// repo name (GitHub Pages project site)
				base: '/eddit',
				// absolute URLs, so redirects and links work from any URL depth
				relative: false
			}
		})
	],
	optimizeDeps: {
	    exclude: ['maplibre-gl']
	  }
});
