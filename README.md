# Fast API with locust and k8s autoscaling
## Run api as is
- install requirements, prefereably in venv
```
 uvicorn svc.main:app --host 0.0.0.0 --port 8080 --reload
 ```

## Docker
- dd build -t prime_factor_fastapi:1.0.0
- dd run -p 8080:8080 --name fastapi -d prime_factor_fastapi:1.0.0
- curl -X POST "http://localhost:8080/api/v1/hello" -H  "accept: application/json" -H  "Content-Type: application/json" -d {}

## Load test
- pip install locust as needed
- locust
- use `http://localhost:8080`


## K8s
- kk apply -f api.yml (ensure u have the image in minikube runtime)

- minikube tunnel or (prefered) minikube service XYZ

- go to that "new" ip ip:8080/docs

- kk apply -f autoscale.yml (to load test later in cloud)

### Inspired by iwpnd blog and R.Thomas article