# Create a docker network for communication between containers and to the outside world
create-network:
	docker network create kochava

# Start redis docker container
start-redis:
	docker run -d -p 6379:6379 -e REDIS_HOST=redis -e REDIS_PORT=6379 --net kochava --name redis-1 redis

# Build the web-server
build-web-server:
	docker build -t kochava_web_server .

# Run the built docker container for web server
run-web-server:
	docker run --net kochava -d -p 9001:9001 -e REDIS_HOST="redis-1" --name kochava_web_server kochava_web_server

# Stop and remove the web server docker container
destroy-web-server:
	docker stop kochava_web_server && docker rm kochava_web_server

# Stop and remove the redis docker container
destroy-redis:
	docker stop redis-1 && docker rm redis-1

# Remove the docker network
remove-network:
	docker network rm kochava

# Remove exited docker containers and reclaim space
prune:
	docker system prune