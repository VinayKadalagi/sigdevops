# Containerized microservice challenge

Implement a piece of software exposing a JSON document:

{ "id": "1", "message": "Hello world" } ... when visited with a HTTP client

Dockerize the application

Put the application to Minikube Kubernetes

Create a second application, that utilizes the first and displays a fully reversed message text rendered dynamically

Automate deployment of the 2 applications using a script

As a result of the task, provide us an archive with the deployment script (called script.sh) and all necessary files which we can use to deploy your applications and verify the solution

----------------

# Solution:

### app1: 
Application 1 is a dockerized python application which exposes the JSON document as { "id": "1", "message": "Hello world" }
```
├── Dockerfile
├── api
│   ├── __init__.py
│   └── requirements.txt
└── app1-microservice.yaml
```

- Dockerfile: Pulls python3.7 alpine image, sets the flask environment variables, installs python dependencies, expose 5000 port and execute `flask run` command.
- app1-microservice.yaml: Kubernetes manifest file containing deployment and service specification.
- __init__.py: flask api application which returns json `{ "id": "1", "message": "Hello world" }`.
- requirements.txt: Python dependencies requirement file.


### app2: 
Application 2 is a dockerized python application consumes application using requests by calling the service defined in app1-microservice.yaml
```
├── Dockerfile
├── api
│   ├── __init__.py
│   └── requirements.txt
└── app2-microservice.yaml
```

- Dockerfile: Pulls python3.7 alpine image, sets the flask environment variables, installs python dependencies, expose 5000 port and execute `flask run` command.
- app2-microservice.yaml: Kubernetes manifest file containing deployment and service specification.
- __init__.py: flask api application which calls application 1 and reverses the json message received and displays another json rendered dynamically. Something like `{"id":"1","message":"dlrow olleH"}`
- requirements.txt: Python dependencies requirement file.
