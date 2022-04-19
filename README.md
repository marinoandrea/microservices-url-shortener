# Web Services and Cloud-Based Systems - Group 4

This project contains 3 sub-projects: `auth-service`, `front-service` and `url-shortener`.

The `url-shortener` is a Flask web service that exposes RESTful interfaces. Similarly, the `auth-service` is a Flask web service dedicated to user authentication and JWT generation. The `front-service` is a simple React.js single-page application which is used for testing API consumption on a GUI.

## Local Development/Deployment

In order to run the services locally (this does not include the `front-service` which is just meant for testing), run the following scripts:

```bash
./setup.dev.sh
./run.dev.sh
```

This will generate a pair of RSA keys and setup the necessary env variables for the services.
Alternatively, you can generate the key pair manually and simply use `docker-compose`. Note that you will still need to specify the `PASSWORD_SALT`, `RSA_PUBLIC_PATH`, and `RSA_PRIVATE_PATH` env variables for password encryption and JWT signing on the auth service. For example you could run:

```bash
export PASSWORD_SALT=<YOUR_SECRET_SALT_STRING>
export RSA_PUBLIC_PATH=<PATH_TO_PUBLIC_PEM_FILE>
export RSA_PRIVATE_PATH=<PATH_TO_PRIVATE_PEM_FILE>

docker-compose up
```

## Production Deployment

In order to run our services in a production environment, there are some few extra steps that must be taken. Most importantly, the Flask-based services should be deployed on a WSGI capable web server (e.g. Apache, Unicorn etc.). We do not provide instruction for this as we do not expect the reader to deploy these services on a remote machine.
