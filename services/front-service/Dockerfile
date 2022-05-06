# using Node.js LTS release, this is the first stage container
# used to compile our JSX into static JS + HTML files.
FROM node:16.15.0 as build-container

# we set an appropriate work directory to highlight this is
# just a temporary folder and that this container should not be used as
# the runtime environment
WORKDIR /tmp/react

# we copy over necessary files for the build and we give owner rights to the
# non-privileged (non root) 'node' user for additional security
COPY --chown=node:node package*.json /tmp/react/
COPY --chown=node:node src /tmp/react/src
COPY --chown=node:node public /tmp/react/public

# we give owner rights to the entire folder only to 'node'
RUN chown -R node:node /tmp/react

# we switch user
USER node

# we install dependencies as a normal user and we build the production app
# NOTE: we do not pass the '--production' flag to 'npm install' because the
# dependency trimming is done by 'react-scripts', we need all devDependencies
# during the build step.
RUN npm install && npm run build

###

# we use this second container as the runtime one, based on a very small nginx
# image which runs on alpine (minimal and lightweight linux distro)
FROM nginx:alpine as runtime-container

# we set our nginx.conf server descriptor as the default nginx configuraton
COPY nginx.conf /etc/nginx/conf.d/default.conf
# we copy the build artifacts from the previous container and we put them in the
# root html folder (this is what gets served by nginx on the main domain)
COPY --from=build-container /tmp/react/build /usr/share/nginx/html

ENV PORT 80
# we allow the container to listen on all connections
# so that it can be targeted in the cluster
ENV HOST 0.0.0.0

# we expose port 80
EXPOSE 80