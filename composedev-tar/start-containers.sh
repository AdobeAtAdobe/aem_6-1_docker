#!/bin/bash 
docker-compose up -d;
HTTP=$(docker-machine ls | egrep -o 'tcp://[^:]*' | sed 's/tcp:/http:/');
echo "AEM Author URL: $HTTP:4502";
echo "AEM Publish URL: $HTTP:4503";
echo "Dispatcher URL: $HTTP";