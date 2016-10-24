# Docker Compose a simple AEM dev environment

You will need to build the following images localy first before running the docker-compse command from the projects directory
```
docker-compose up -d
```
Step 1
Build the publisher image locally
Make sure to follow the README and put the aem source jar and the license files in the resource directory.  Since it requires your install media you have to build this locally.
```
cd ../publish-tar
docker build -t aem_6-2_publish .
```

Step 2
Build the author image locally
Make sure to follow the README and put the aem source jar and the license files in the resource directory.  Since it requires your install media you have to build this locally.
```
cd ../author-tar
docker build -t aem_6-2_author .
```

Step 3
Build the dispatcher image.
```
cd ../dispatcher-ps
docker build -t aem_6-2_dispatcher  .
```
now if you run
```
docker images
```
you should see all the images listed and ready for use.  Now you can go into the composedev-tar directory and run the compose command

```
docker-compose up -d
```

I included a simple script to help build the whole setup out.  It must be run from the root clone directory IG one level below composedev-tar
```
makeLocalImages.sh
```
put it in root directory where you want all the build scripts and git clones to happen and it will build run the docker commands.  At the end you will need to change to the directory composedev-tar (again) and run
```
docker-compose up -d
```
to bring it all up

I need to find the right command to show the local VM's ip address so you can connect to the new enviroment.  Today I am using Kitematic on my mac to show me the access urls.

