# DOCKER-VERSION 1.7.0 AUTHOR
FROM aem_6-1_base
LABEL version="1.0"
LABEL description="AEM author docker image"
MAINTAINER dbenge

#Copies required build media
ADD resources/*.jar /aem/cq-author-4502.jar
ADD resources/license.properties /aem/license.properties

# Extracts AEM
WORKDIR /aem
RUN java -Djava.awt.headless=true -XX:MaxPermSize=256m -Xmx1280m -jar cq-author-4502.jar -unpack -r nosamplecontent

# Add customised log file, to print the logging to standard out.
ADD resources/org.apache.sling.commons.log.LogManager.config /aem/crx-quickstart/install

# Installs AEM
WORKDIR /aem
RUN ["python","aemInstaller.py","-i","cq-author-4502.jar","-r","author","-p","4502"]

WORKDIR /aem/crx-quickstart/bin
RUN mv quickstart quickstart.original
ADD resources/quickstart /aem/crx-quickstart/bin/quickstart
RUN chmod +x /aem/crx-quickstart/bin/quickstart

EXPOSE 4502
ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]