#!/usr/bin/sh
# these paths are relative to the auth-service root folder
export RSA_PUBLIC_PATH=jwt_public.pem
export RSA_PRIVATE_PATH=jwt_private.pem

docker-compose up --remove-orphans