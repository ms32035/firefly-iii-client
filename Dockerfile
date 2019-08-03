FROM openapitools/openapi-generator-cli:v4.0.3

RUN apk add \
   --update ca-certificates openssl python3 git && \
   update-ca-certificates && \
   pip3 install pyyaml && \
   mkdir /build && \
   chmod 777 /build

COPY .generator/ /generator/

ENTRYPOINT [ "/generator/generate.sh" ]