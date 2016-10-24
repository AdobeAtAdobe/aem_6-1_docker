# aem-6_2-author

# AdobeAtAdobe's docker AEM 6.2 Author image
This is based on this repo example https://github.com/sergeimuller/ and also https://hub.docker.com/u/ggotti/

Building image localy from the project directory
put your AEM jar in the resources directory
put your AEM license file in the resources directory.  The file should be named license.properties
run this command to build image
```
docker build -t aem_6-2_author .
```
run the image with this command
```
docker run --name AEM_AUTHOR -p 4502:4502 -d aem_6-2_author
```

Still a work in progress.  It works now but its still a work in progress and needs more tuning.
