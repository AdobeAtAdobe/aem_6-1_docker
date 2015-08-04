# DOCKER-VERSION 1.0.1
FROM ubuntu-upstart
LABEL version="1.0"
LABEL description="AEM base image"
MAINTAINER dbenge

ENV DEBIAN_FRONTEND noninteractive

# Install utility for AEM
ADD aemInstaller.py /aem/aemInstaller.py

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN apt-get -y install ipython ipython3
RUN apt-get -y install python-psutil
RUN apt-get -y install python-pycurl

RUN apt-add-repository -y ppa:webupd8team/java
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y 

# Enable silent install
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections

RUN apt-get install -y --force-yes oracle-java7-installer

ENV JAVA_HOME=/usr/lib/jvm/java-7-oracle/jre/bin/java
ENV PATH $PATH:/usr/lib/jvm/java-7-oracle/jre/bin/java

