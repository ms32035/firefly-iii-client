FROM openapitools/openapi-generator-cli:v4.0.0

ENV API_VERSION 0.9.2

RUN apk add --update ca-certificates openssl python3 && update-ca-certificates && pip3 install pyyaml

COPY .generator/ /generator/

ENTRYPOINT [ "/generator/generate.sh" ]