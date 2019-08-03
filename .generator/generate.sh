#!/usr/bin/env bash
checkStatus () {
retVal=$?
if [[ ${retVal} -ne 0 ]]; then
    exit ${retVal}
fi
}

if [[ ! -z $1 ]]
then
    SPEC_FILE=$1
else
    SPEC_FILE=/build/firefly-iii.yaml
    wget https://api-docs.firefly-iii.org/firefly-iii-${API_VERSION}.yaml -O ${SPEC_FILE}
fi
checkStatus

python3 /generator/preprocess.py ${SPEC_FILE} /build/firefly-iii-processed.yaml
checkStatus

java -jar /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
-i /build/firefly-iii-processed.yaml \
-o /build/target \
-g python \
--git-user-id ms32035 \
--git-repo-id firefly-iii-client \
--enable-post-process-file \
-DpackageName=firefly_iii_client \
-DprojectName="Firefly III API Client" \
-DpackageVersion=${API_VERSION} \
-DpackageUrl=https://github.com/ms32035/firefly-iii-client
checkStatus

python3 /generator/postprocess.py /build/target

USER=$(stat -c '%u' /docker-compose.yml)
GROUP=$(stat -c '%g' /docker-compose.yml)
chown -R $USER:$GROUP /build/target