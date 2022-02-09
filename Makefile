build:
	docker build -t asteroid_strikes .

run:
	docker run -dp 5000:5000 asteroid_strikes