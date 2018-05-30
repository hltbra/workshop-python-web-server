## Run docker

```
docker run --rm -it -v $PWD:/app -p 8888:8888 python:2.7-jessie bash
```


## Run ab

```
ab -c 1 -n 10000 http://127.0.0.1:9999/
```