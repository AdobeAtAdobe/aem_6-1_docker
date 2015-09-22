#!/bin/bash
sh -c 'cd base/ && exec docker build -t aem_6-1_base .'
echo "done building Base image"

while true; do
	echo "Put your AEM jar and your license file in publish-tar/resources directory."
    read -p "When ready type y and hit enter? " y
    case $y in
        [Yy]* ) break;;
        * ) echo "Please answer y when your ready to move foward.";;
    esac
done

sh -c 'cd publish-tar/ && exec docker build -t aem_6-1_publish .'
echo "done building Publisher"

while true; do
	echo "Put your AEM jar and your license file in author-tar/resources directory."
    read -p "When ready type y and hit enter? " y
    case $y in
        [Yy]* ) break;;
        * ) echo "Please answer y when your ready to move foward.";;
    esac
done

sh -c 'cd author-tar/ && exec docker build -t aem_6-1_author .'
echo "done building Author"

sh -c 'cd dispatcher-ps/ && exec docker build -t dispatcher_4-1-9 .'
echo "done building Dispatcher"

sh -c 'cd composedev-tar'
echo 'Now go into composedev-tar and run this command:docker-compose up -d'