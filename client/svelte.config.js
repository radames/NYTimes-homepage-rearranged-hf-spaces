import adapter from '@sveltejs/adapter-static'
const dev = process.env.NODE_ENV === 'development';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		vite: {
			server: { fs: "allow" },
		},
		paths: {
			base: '/static'
		},
		appDir: '_app',
		adapter: adapter({
			pages: 'dist',
			assets: 'dist',
			fallback: null,
			precompress: false
		})
	}
};

export default config;
