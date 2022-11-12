#/bin/sh

# set minikube docker-env
eval $(minikube docker-env)

# docker build app1 and app2
(cd app1 && docker build -t app1 .)
(cd app2 && docker build -t app2 .)

# minikube deployment
(cd app1 && kubectl apply -f app1-microservice.yaml)
(cd app2 && kubectl apply -f app2-microservice.yaml)
