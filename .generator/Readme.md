# Using the generator


Build the docker image

```
docker build -t firefly-iii-client-generator .
```

Generate the new python package

```
docker run -v $(pwd)/target:/firefly-iii-client firefly-iii-client-generator 
```

This should generate a new package in `target` directory

If the package generation fails due to yaml specification file issues,
a locally modified copy can be used

```
docker run \
-v $(pwd)/target:/firefly-iii-client \
-v /tmp/firefly-iii.yaml:/firefly-iii.yaml \
firefly-iii-client-generator /firefly-iii.yaml
```