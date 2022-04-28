#!/usr/bin/sh

RSA_PUBLIC_PATH=$HOME/jwt_public.pem
RSA_PRIVATE_PATH=$HOME/jwt_private.pem
PASSWORD_SALT=$(cat /proc/sys/kernel/random/uuid | sed 's/[-]//g' | head -c 42; echo;)

openssl genrsa -out $RSA_PRIVATE_PATH 2048 > /dev/null
openssl rsa -in $RSA_PRIVATE_PATH -out $RSA_PUBLIC_PATH -pubout -outform PEM > /dev/null

kubectl create secret generic auth-rsa-keys \
    --from-file=rsa-privatekey=$RSA_PRIVATE_PATH \
    --from-file=rsa-publickey=$RSA_PUBLIC_PATH

kubectl create secret generic auth-password-salt \
    --from-literal=password-salt=$PASSWORD_SALT