# DOCKER-VERSION 1.7.0 PUBLISHER
FROM aem_6-2_base
LABEL version="1.0"
LABEL description="AEM publisher docker image"
MAINTAINER dbenge

#Copies required build media
ADD resources/*.jar /aem/cq-publish-4503.jar
ADD resources/license.properties /aem/license.properties
ADD resources/postInstallHook.py /aem/postInstallHook.py
ADD resources/packagelist.txt /aem/packagelist.txt
ADD resources/packages/*.zip /aem/packages/

# Extracts AEM
WORKDIR /aem
RUN java -Djava.awt.headless=true -XX:MaxPermSize=256m -Xmx1280m -jar cq-publish-4503.jar -unpack -r nosamplecontent

# Add customised log file, to print the logging to standard out.
ADD resources/org.apache.sling.commons.log.LogManager.config /aem/crx-quickstart/install/org.apache.sling.commons.log.LogManager.config
ADD resources/org.apache.jackrabbit.oak.plugins.segment.SegmentNodeStoreService.cfg /aem/crx-quickstart/install/org.apache.jackrabbit.oak.plugins.segment.SegmentNodeStoreService.cfg

# Installs AEM
WORKDIR /aem
RUN ["python","aemInstaller.py","-i","cq-publish-4503.jar","-r","publish","-p","4503"]

WORKDIR /aem/crx-quickstart/bin
RUN mv quickstart quickstart.original
ADD resources/quickstart /aem/crx-quickstart/bin/quickstart
RUN chmod +x /aem/crx-quickstart/bin/quickstart
RUN chmod +x /aem/compaction.sh

EXPOSE 4503
#ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]
ENTRYPOINT ["/aem/compaction.sh"]
