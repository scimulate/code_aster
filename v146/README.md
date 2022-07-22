```
xhost +local:docker
docker run --rm -it --env="DISPLAY" --net=host -v "$(pwd)":/analysis scimulate/code_aster:14.6
```
