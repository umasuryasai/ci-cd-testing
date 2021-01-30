# Deploying Lightweight Nginx Server with Docker Best Practices
Here we will be deploying an nginx application using Docker best practices

### Best practices in Docker

1. Always use specific vesion/tag of base images
2. Use lightweight base images as alpine
3. Run the application as sone specific user, not as root user


### Docker Compose

#### Commands

```
docker-compose config #To validate the the compose yaml file
docker-compose up -d #To run the docker containers/services in detached mode
docker-compose down #To stop the docker containers/services
```