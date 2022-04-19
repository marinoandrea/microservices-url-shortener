#!/usr/bin/sh

# these paths are relative to the auth-service root folder
export RSA_PUBLIC_PATH=jwt_public.pem
export RSA_PRIVATE_PATH=jwt_private.pem

# random UUID used for password encryption salt rounds
export PASSWORD_SALT=$(cat /proc/sys/kernel/random/uuid | sed 's/[-]//g' | head -c 42; echo;)

docker-compose up --remove-orphans