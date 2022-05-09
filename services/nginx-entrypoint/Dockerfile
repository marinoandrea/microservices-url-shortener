
# as we are not using any experimental features or
# legacy configuration, we can simply rely on the latest image
# for nginx
FROM nginx

# we set our nginx.conf server descriptor as the default nginx configuraton
# for the container
COPY /nginx.conf /etc/nginx/conf.d/default.conf

# we expose port 3000
EXPOSE 3000