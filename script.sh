#/bin/sh

# set minikube docker-env
eval $(minikube docker-env)

# docker build app1 and app2
(cd app1 && docker build -t app1 .)
(cd app2 && docker build -t app2 .)

# minikube deployment
(cd app1 && kubectl delete -f app1-microservice.yaml  --ignore-not-found=true)
(cd app1 && kubectl apply -f app1-microservice.yaml)

(cd app2 && kubectl delete -f app2-microservice.yaml  --ignore-not-found=true)
(cd app2 && kubectl apply -f app2-microservice.yaml)

# sleeping 40 seconds
echo "\nSleeping 40 seconds until pods ready"
sleep 40

# port forwarding for app2
app2_pod=$(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep app2)
(kubectl port-forward $app2_pod 5001:5000)

