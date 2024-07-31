// config.js
const config = {
	apiUrl: import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000' // default for development
};
export default config;