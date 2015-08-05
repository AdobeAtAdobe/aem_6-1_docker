# Docker AEM 

This project holds all our 6.1 AEM docker images we have built so far.  At this time we have only completed and tested the standard tar MK based images.  We will be working to include more as time goes on.  

The easiest way to get start would be to clone this repo then from the cloned root directory run the following command
```
./composedev-tar/makeLocalImages.sh
```
note: you may need to allow execution on this script (chmod +x ./composedev-tar/makeLocalImages.sh)

This command will build the base, publisher and author image locally and will prompt you to supply your AEM jar and license file.  Then it will build out the dispatcher image for you.

After that is done running the next step would be to change to the composedev-tar directory and run the compose to bring up all three containers for you.


You will need to build the following images locally first before running the docker-compse command from the projects directory
```
docker-compose up -d
```

How are the AEM instances configured?  Each of the AEM images (author, publish) are configured via quickstart properties.  The quickstart file that is responsible for the configuration can be found under each images resources subdirectory.  


I need to find the right command to show the local VM's ip address so you can connect to the new environment.  Today I am using Kitematic on my mac to show me the access urls.

This has only been tested on a Mac system at this point.  

Another note:  If your running these images on your MAC you will need to adjust your Virtual Box memory settings.  The default boot2docker vm image only has 2 gigs alocated for memory and these images need 2 gigs each.  I think I need to come up with a better solution so its easier to use on smaller dev machines.  To alter your Virtal Box memory settings find the Virtual Box app and run it and then select the boot2docker vm and adjust its settings and add memory. 
In some of the beta versions of Kitematic it will use a VM named dev and not the boot2docker vm image.

