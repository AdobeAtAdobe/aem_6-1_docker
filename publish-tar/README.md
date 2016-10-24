# aem-6_2-publish

# AdobeAtAdobe's docker AEM 6.1 Publish image
This is based on this repo example https://github.com/sergeimuller/aem-publisher and also https://hub.docker.com/u/ggotti/

Building image localy from the project directory
put your AEM jar in the resources directory
put your AEM license file in the resources directory.  The file should be named license.properties
run this command to build image
```
docker build -t aem_6-2_publish .
```
run the image with this command
```
docker run --name AEM_PUB -p 4503:4503 -d aem_6-2_publish
```

The AEM quickstart configuration is in the resources directory.  If you need to change JVM options or other parameters you can do it in that file and rebuild the image.

This is working but I still want to do a lot more tuning to it.
