build-client:
	cd client && npm install && npm run build && pwd && rm -r ../static && cp -r dist/ ../static/
build-client-dev:
	cd client && npm install && NODE_ENV=development  npm run build && pwd && rm -r ../static/* && cp -r dist/ ../static/
dev:
	cd client && npm run dev
run:
	FLASK_ENV=development python app.py
build-all: install-node build-client run
