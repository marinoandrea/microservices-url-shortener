# [Web Services and Cloud-Based Systems] Assigment 1 - Group 4

This project contains two sub-projects: `front-service` and `url-shortener`. The `url-shortener` is a Flask web service that exposes RESTful interfaces. The `front-service` is a simple React.js single-page application which implements a UI that allows to interact with the API graphically.

## Local Development/Deployment

In order to run the core application locally, we offer two different methods: using docker or running the development servers. As setting up an nginx image locally just for development wouldn't make much sense, if you want to run the frontend, we suggest to use the development server. Anyway we also include an nginx-based image for the React app for completion.

### Docker

If you have **docker** installed, you can use the image we provided to run our `url-shortener` service. In order to do so, run the following commands:

```bash
cd services/url-shortener

docker build . -t url-shortener

docker run -p 5000:5000 url-shortener
```

Beware that this is just meant for local and development deployment. There is no DNS logic for the services, and since the React app is client-side rendered, we simply hard-code the API address to be `http://localhost:5000`. Any modification to the container address/port would break the UI if you do not update the source.

### Development Servers

You can also run each application in their development mode:

#### front-service

Install Node.js first, then under the front-service directory, run the following commands.

```bash
npm install

npm start

# Alternatively, you can also use yarn
yarn install

yarn start
```

**_NOTE:_** if the URL of url-shortener is not running on "http://localhost:5000", please modify URL_SHORTENER_API_BASE_URL value in ./front-service/src/services/UrlShortenerService.js.

#### url-shortener

The workflow for running the project is:

1. install `pipenv` globally on the machine
2. go to the `url-shortener` folder of the project and run `pipenv install` to install all dependencies (the url-shortener folder is the one where there is a Pipenv file)
3. run the development server with `pipenv run flask run`

## Production Deployment

In order to run our services in a production environment, there are some few extra steps that must be taken. First of all the Flask API should be served by a WSGI capable web server (e.g. Apache, Unicorn etc.), then the right domain for the API should be updated in the UI code. Finally, the UI should be deployed either via the docker image or with any other static web service (e.g. Nginx).

We do not provide instruction for this as we do not expect the reader to deploy these services on a remote machine.
