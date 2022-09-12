# sre-interview

Mini project - run a small web server that returns a value from redis


## Installation (using Docker and Flask to handle HTTP requests)

1. Install [Docker](https://docs.docker.com/engine/install/) locally
2. Verify docker is running after the installation. You can try the below commands and you should get an error free response
```
docker version
docker info
docker ps
docker run hello-world
```


## Next steps - setup
1. Clone this git repo in the command line using
```https://github.com/natarajanct/sre-interview.git```
2. Go to the directory sre-interview`cd sre-interview`
3. Run the following steps using the makefile in the same directory
```
# To create a docker network
make create-network

# to start the redis docker container
make start-redis

# to build the web-server
make build-web-server

# to run the web-server
make run-web-server
```
4. Verify there are 2 docker containers up and running
```
$ docker ps
CONTAINER ID   IMAGE                COMMAND                  CREATED         STATUS         PORTS                    NAMES
xxxxxxxxxxxx   kochava_web_server   "/bin/sh -c 'flask r…"   4 minutes ago   Up 4 minutes   0.0.0.0:9001->9001/tcp   kochava_web_server
yyyyyyyyyyyy   redis                "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes   0.0.0.0:6379->6379/tcp   redis-1
```

## How to use the service
1. Open a web browser and enter the URL `localhost:9001` and you should see the following in the web page. When the flask app is run the below key values are set to redis
```
Initial set key on redis : Hello
Value retrieved from redis: World!
```
2. To set a key in redis the URL should have both a key and a value eg: `localhost:9001/set_key/foo/bar`. If the URL is clean, the key - value pair will be added to redis and you will see the below message on the web page
```
foo is set to bar
```
3. To get a key from redis the URL should have a valid key eg: `localhost:9001/get_key/foo`. If the URL is clean, and if the key exists in redis, the value for the corresponding key will be displayed on the web page
```
bar
```
4. To add more values to redis, the above set_key method in the URL can be used

## Clean up - steps
To clean up the docker setup used for this service, run the following steps using the makefile in the same directory
```
# to top and remove the web server docker container
make destroy-web-server

# to stop and remove the redis docker container
make destroy-redis

# to remove the docker network
make remove-network

# to remove exited docker containers and reclaim space
make prune
```

# Implementation
Things used
1. Docker based implementation for the project
2. Code repo - Github
3. Redis - official docker image for redis
4. Python runtime 
5. Flask framework to handle HTTP requests. No dedicated web server

Project flow
1. Create a docker network for communication between the 2 containers that are going to be used -> redis and the flask app
2. Add any dependencies in the Dockerfile (requirements.txt) to build the web-server in the same docker network as the redis docker container
3. Steps for building and deploying the service (including the port forwarding to 9001) is given in the makefile
4. The initial key, value pair to redis is set in the home page function in the flask app and the key-value pair is displayed on the webpage. 
5. Additional key-values can be set and retrieved using this service as well.

Improvement
1. This is just a basic implementation of the requirement. The front end aspect of it could have been a lot better.
2. The make steps to build and deploy the service could have been better automated with a docker-compose tool
