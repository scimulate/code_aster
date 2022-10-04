With Docker installed, this container can be setup using the following command.

```
docker pull scimulate/code_aster:XX.Xy
```

Where XX.X(y) is the version number. Currently supported version numbers include:

+ 14.6
+ 14.6p (in progress)
+ 15.2
+ 15.2p (in progress)

Navigate to the host directory which contains code_aster files (mesh, setup, etc.).

```
cd /your_project_path
```

Run the following commands to enable GUI applications and start the container.

```
xhost +local:docker
docker run --rm -it --env="DISPLAY" --net=host -v "$(pwd)":/analysis scimulate/code_aster:XX.X(y)
```

The flag `-v "$(pwd)":/analysis` will mount the present working directory (pwd) to a dedicated folder in the container `/analysis`. This allows for seamless file read/write between the host and container. Next, start ASTK.

```
/opt/aster/bin/astk
```

Navigate to `/analysis` through ASTK and add files to the project. Results computed and saved to `/analysis` may be post-processed on the host after computing the solution. When done using the container, simply exit.

```
exit
```
