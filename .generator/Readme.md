# Using the generator

Generate the new python package

```
docker-compose run firefly_iii_client_generator
```

This should generate a new package in `target` directory

You can next sync only needed files back to he root of the repo dir
with `.generator/postgenerate.sh`