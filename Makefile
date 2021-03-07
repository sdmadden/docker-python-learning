start-dev:
	sudo docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d
stop:
	sudo docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
start:
	sudo docker-compose up -d
rebuild-web:
	sudo docker-compose up -d --build web