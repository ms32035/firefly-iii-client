#!/usr/bin/env bash

GENERATORDIR=$(dirname "$0")
REPODIR=${GENERATORDIR}/..

xargs -I % --arg-file=${GENERATORDIR}/overwritelist rm -rf ${REPODIR}/%

xargs -I % --arg-file=${GENERATORDIR}/overwritelist cp -r ${REPODIR}/target/% ${REPODIR}/