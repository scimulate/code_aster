With Docker installed, this container can be setup using the following commands.

```
docker pull scimulate/code_aster

```
Navigate to your local directory which contains code_aster files (mesh, setup, etc.).

```
cd /your_file_path
```
Run the following commands to enable GUI applications and start the container.

```
xhost +local:docker
docker run --rm -it --env="DISPLAY" --net=host -v "$(pwd)":/analysis scimulate/code_aster:14.6
```

This will attach the current directory of your working

Next, start ASTK 
```
/opt/aster/bin/astk
```
