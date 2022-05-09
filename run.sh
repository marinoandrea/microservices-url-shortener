#!/usr/bin/sh
# these paths are relative to the auth-service root folder
export RSA_PUBLIC_PATH=jwt_public.pem
export RSA_PRIVATE_PATH=jwt_private.pem
export AUTH_MONGODB_USER=test
export AUTH_MONGODB_PASS=test
export AUTH_MONGODB_NAME=test
export SHORTENER_MONGODB_USER=test
export SHORTENER_MONGODB_PASS=test
export SHORTENER_MONGODB_NAME=test

docker-compose up --remove-orphans