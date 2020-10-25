FROM openapitools/openapi-generator-cli:v4.3.1

RUN apk add \
   --update ca-certificates openssl python3 git curl && \
   update-ca-certificates && \
   pip3 install pyyaml && \
   mkdir /build && \
   chmod 777 /build

COPY .generator/ /generator/

ENTRYPOINT [ "/generator/generate.sh" ]