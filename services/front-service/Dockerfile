FROM node:16 as frontend-build-container
# using node LTS

WORKDIR /tmp/frontend

COPY . /tmp/frontend/

RUN npm install -g npm@latest && npm install && npm run build

FROM nginx

COPY --from=frontend-build-container /tmp/frontend/build/ /usr/share/nginx/html

COPY /nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80