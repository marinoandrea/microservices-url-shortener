#!/usr/bin/sh

RSA_PUBLIC_PATH=services/auth-service/jwt_public.pem
RSA_PRIVATE_PATH=services/auth-service/jwt_private.pem

openssl genrsa -out $RSA_PRIVATE_PATH 2048 > /dev/null
openssl rsa -in $RSA_PRIVATE_PATH -out $RSA_PUBLIC_PATH -pubout -outform PEM > /dev/null
