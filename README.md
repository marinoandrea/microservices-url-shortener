# Web Services and Cloud-Based Systems - Group 4

This project contains 4 sub-projects: `nginx-entrypoint`, `auth-service`, `front-service` and `url-shortener`.

The `url-shortener` is a Flask web service that exposes RESTful interfaces. Similarly, the `auth-service` is a Flask web service dedicated to user authentication and JWT generation. The `front-service` is a simple React.js single-page application used to test API consumption on a GUI. The `nginx-entrypoint` is a simple gateway that provides one entry point for all our microservices.

## Running the services

In order to run the services locally (this does not include the `front-service`, which is just meant for testing), run the following scripts:

```bash
./setup.sh

```

This will generate a pair of RSA keys and set up the necessary env variables for the services.
Alternatively, you can generate the key pair manually and simply use `docker-compose`. Note that you will still need to specify the several env variables for password encryption and JWT signing on the auth service and configuration about MongoDB. For example, you could run:

```bash
export PASSWORD_SALT=<YOUR_SECRET_SALT_STRING>
export RSA_PUBLIC_PATH=<PATH_TO_PUBLIC_PEM_FILE>
export RSA_PRIVATE_PATH=<PATH_TO_PRIVATE_PEM_FILE>
export AUTH_MONGODB_USER=<YOUR_AUTH_MONGODB_USERNAME>
export AUTH_MONGODB_PASS=<YOUR_AUTH_MONGODB_PASSWORD>
export AUTH_MONGODB_NAME=<YOUR_AUTH_MONGODB_NAME>
export SHORTENER_MONGODB_USER=<YOUR_SHORTENER_MONGODB_USERNAME>
export SHORTENER_MONGODB_PASS=<YOUR_SHORTENER_MONGODB_PASSWORD>
export SHORTENER_MONGODB_NAME=<YOUR_SHORTENER_MONGODB_NAME>

docker-compose up
```

Otherwise, you can store the above env variables in the .env file and then run:

```bash
docker-compose up
```

After services startup, you can optionally use our `nginx` API Gateway with the following URL prefixes: `localhost:3000/api/v1/auth/users/` to request the auth endpoints and `localhost:3000/api/v1/shortener/` to request url-shortener endpoints.

## Kubernetes Setup

In the Kubernetes, we implemented six parts:shortener-service,shortener-database,auth-service,auth-database,front-service,ingress.

- business logic: shortener-service, auth-service, front-service
- persistence layer: shortener-database,auth-database
- load balance: ingress

We use the helm chart to deploy our project. All the configuration files can be found in the url-shortener-chart directory. For security reasons, we also defined network policy for each database.

**_Note:_** we push the shortener-service,auth-service, and front-service images to our private docker hub repository. If you want to change anything in the source code, you may need to push it to your own repository and change the image configuration in the deployment.
For deploying our project, you can run:

```bash
helm install url-shortener-chart url-shortener-chart/
```

To uninstall it, you can run:

```bash
helm uninstall url-shortener-chart
```
