FROM openapitools/openapi-generator-cli:v5.1.1

RUN apt update && \ 
   apt install -yqq ca-certificates openssl python3 git curl python3-pip && \
   pip3 install pyyaml && \
   mkdir /build && \
   chmod 777 /build

COPY .generator/ /generator/

ENTRYPOINT [ "/generator/generate.sh" ]