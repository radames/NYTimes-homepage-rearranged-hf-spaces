build-client:
	cd frontend && npm install && npm run build && cp -r dist/ ../dist
run:
	FLASK_ENV=development python app.py
build-all: build-client run
