#!/usr/bin/sh

MODE=$1
FILE=docker-compose.dev.yaml

if [ $MODE = "dev" ]; then
    FILE=docker-compose.dev.yaml
elif [ $MODE = "prod" ]; then
    FILE=docker-compose.prod.yaml
fi

# these paths are relative to the auth-service root folder
export RSA_PUBLIC_PATH=jwt_public.pem
export RSA_PRIVATE_PATH=jwt_private.pem

docker-compose -f $FILE up --remove-orphans