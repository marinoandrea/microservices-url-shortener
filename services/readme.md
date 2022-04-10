# Assigment 1

Our project contains two services. The frontend project is front-service and the backend project is url-shortener.

## front-service

Install Node.js first, then under the front-service directory, run the following commands.

```
npm install  

npm start
```

***NOTE:*** if the URL of url-shortener is not "http://localhost:5000", please modify URL_SHORTENER_API_BASE_URL value in ./front-service/src/services/UrlShortenerService.js.

## url-shortener

The workflow for running the project is:
1. install pipenv globally on the machine
2. go to the url-shortener folder of the project and run pipenv install --dev to install all dependencies(the url-shortener folder is the one where there is a Pipenv file)
3. run it with 'pipenv run flask run'


