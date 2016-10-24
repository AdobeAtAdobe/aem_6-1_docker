# DOCKER-VERSION 1.7.0
FROM aem_6-2_base
LABEL version="1.0"
LABEL description="AEM publish dispatcher.  Uses Apache and Google Pagespeed"
MAINTAINER dbenge

RUN apt-get -y install apache2 apache2-utils libssl1.0.0 libssl-dev

# Configure timezone and locale
RUN echo "US/Pacific" > /etc/timezone && \
	dpkg-reconfigure -f noninteractive tzdata
RUN export LANGUAGE=en_US.UTF-8 && \
	export LANG=en_US.UTF-8 && \
	export LC_ALL=en_US.UTF-8 && \
	locale-gen en_US.UTF-8 && \
	DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

# Install pagespeed
ADD https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_amd64.deb /aem/dispatcher/pagespeed/module/
WORKDIR /aem/dispatcher/pagespeed/module
RUN dpkg -i mod-pagespeed-*.deb
RUN apt-get -y -f install

# Install dispatcher mod - Linux x86 64bit OpenSSL 1.0
#ADD https://www.adobeaemcloud.com/content/companies/public/adobe/dispatcher/dispatcher/_jcr_content/top/download_10/file.res/dispatcher-apache2.4-linux-x86-64-ssl10-4.1.9.tar.gz /aem/dispatcher/module/
# Install dispatcher mod - Linux x86 64bit OpenSSL 1.0
#ADD https://www.adobeaemcloud.com/content/companies/public/adobe/dispatcher/dispatcher/_jcr_content/top/download_8/file.res/dispatcher-apache2.4-linux-x86-64-4.1.9.tar.gz /aem/dispatcher/module/
ADD https://www.adobeaemcloud.com/content/companies/public/adobe/dispatcher/dispatcher/_jcr_content/top/download_10/file.res/dispatcher-apache2.4-linux-x86-64-4.1.11.tar.gz /aem/dispatcher/module/
WORKDIR /aem/dispatcher/module/
RUN tar -zxvf *.gz
RUN chown -R www-data:www-data *
WORKDIR /aem/dispatcher/
RUN mkdir logs
COPY resources/dispatcher.any dispatcher.any
WORKDIR /lib/x86_64-linux-gnu/
RUN ln -s libssl.so.1.0.0 libssl.so.10
RUN ln -s libcrypto.so.1.0.0 libcrypto.so.10

#Copies required mods
WORKDIR /etc/apache2/mods-available/
COPY resources/mods-available/* ./
WORKDIR /etc/apache2/sites-available/
COPY resources/sites-available/* ./

#enable mods and site
RUN a2enmod rewrite dispatcher ssl pagespeed expires headers
RUN a2dissite 000-default
RUN a2ensite aemsite

ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80 443
