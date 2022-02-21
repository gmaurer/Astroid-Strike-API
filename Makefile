build:
	docker build -t asteroid-strike-api .

run:
	docker run -dp 5000:5000 --name asteroid-strike-api asteroid_strikes\

start:
	docker compose up -d

kill:
	docker-compose kill
	docker-compose rm -f

#Non functional, will be done when shifting from local to storing on dockerhub
composebuild:
	docker-compose build

composebuildfresh: 
	docker-compose build --no-cache



docker-tag:
	docker tag asteroid-strike-api gbmaurer/asteroid-strike-api 

docker-push:
	docker-tag
	docker push gbmaurer/asteroid-strike-api:latest