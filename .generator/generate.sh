#!/usr/bin/env bash
checkStatus () {
retVal=$?
if [[ ${retVal} -ne 0 ]]; then
    exit ${retVal}
fi
}

echo API_VERSION=${API_VERSION}${API_SUBVERSION}
PACKAGE_VERSION=${API_VERSION}.${PACKAGE_BUILD}

if [[ ! -z $1 ]]
then
    SPEC_FILE=$1
else
    SPEC_FILE=/build/firefly-iii.yaml
    curl https://api-docs.firefly-iii.org/firefly-iii-${API_VERSION}${API_SUBVERSION}.yaml -o ${SPEC_FILE}
fi
checkStatus

python3 /generator/preprocess.py ${SPEC_FILE} /build/firefly-iii-processed.yaml
checkStatus


java -jar /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar validate \
-i /build/firefly-iii-processed.yaml

java -jar /opt/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar generate \
-i /build/firefly-iii-processed.yaml \
-o /stage \
-g python \
--git-user-id ms32035 \
--git-repo-id firefly-iii-client \
--reserved-words-mappings self=self \
--enable-post-process-file \
--additional-properties=\
packageName=firefly_iii_client,\
projectName="Firefly III API Client",\
packageVersion=${PACKAGE_VERSION},\
packageUrl=https://github.com/ms32035/firefly-iii-client
checkStatus

python3 /generator/postprocess.py /stage

USER=$(stat -c '%u' /build/src/docker-compose.yml)
GROUP=$(stat -c '%g' /build/src/docker-compose.yml)


cd /build/target && ls -A1 /build/target | xargs rm -rf
echo 'Copy stage to target'
cp -r /stage/{.[!.],}* /build/target/
chown -R $USER:$GROUP /build/target
