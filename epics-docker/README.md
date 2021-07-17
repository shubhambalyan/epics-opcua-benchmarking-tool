# Deploy EPICS in a Docker Container

### To build the image from Dockerfile:
```
$ docker build -t <repository_name>:<tag> .
```

For example,
```
$ docker build -t epicsimage:latest .
```

### To run the image with a shell prompt:
```
$ docker run -i -t <repository_name>:<tag> /bin/bash
```

For example,
```
$ docker run -i -t epicsimage:latest /bin/bash
# ./st.cmd
# exit
```
