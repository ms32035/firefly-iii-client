FROM openapitools/openapi-generator-cli:v5.3.0

RUN apt update && \ 
   apt install -yqq ca-certificates openssl python3 git curl python3-pip && \
   pip3 install pyyaml && \
   mkdir /build && \
   chmod 777 /build

ENTRYPOINT ["/generator/generate.sh" ]