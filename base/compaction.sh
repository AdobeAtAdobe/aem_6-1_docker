#!/bin/bash

#Find old checkpoints
java -Dtar.memoryMapped=true -Xms1g -Xmx1g -jar /aem/oak-run.jar checkpoints /aem/crx-quickstart/repository/segmentstore

#Find unreferenced checkpoints and delete them
java -Dtar.memoryMapped=true -Xms1g -Xmx1g -jar /aem/oak-run.jar checkpoints /aem/crx-quickstart/repository/segmentstore rm-unreferenced

java -Dtar.memoryMapped=true -Xms1g -Xmx1g -jar /aem/oak-run.jar compact /aem/crx-quickstart/repository/segmentstore

#Start AEM
sh -c 'cd /aem/crx-quickstart/bin/ && ./quickstart'