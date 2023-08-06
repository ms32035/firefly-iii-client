# Important information

1) The code is generated automatically, using OpenAPI docker image.
Any bugs in the generator are later fixed by `postprocess.py`.
2) Pypi package versioning follows Firefly III API versions, with an additional build number.
PRs directly to the code or docs will most likely be overwritten
    during next generation

## Using the generator

Generate the new python package

```
docker-compose build
docker-compose run firefly_iii_client_generator
```

This should generate a new package in `target` directory

You can next sync only needed files back to the root of the repo dir
with `.generator/postgenerate.sh`