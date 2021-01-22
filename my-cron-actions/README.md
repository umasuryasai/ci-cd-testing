# Daily cron on Sample Java Application
Here we will be running the java application and push the java logs to some storage using cron job on daily basis

### Build
Build the docker image uisng the 

```sh
$ docker build -t java-cron:v1 .
$ docker run -itd -p 8080:8080 java-cron:v1
```

### Testing
Hit the application url in the browser:
```
127.0.0.1:8080
```
