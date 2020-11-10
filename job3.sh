#!/bin/bash
#job_3
#Got docker
echo "Install Docker....!"
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh -y
echo "You have docker now!"
#part1
echo -e "How many Containers do you want to create?\n"
read CONTAINERS
for i in $( eval echo {1..$CONTAINERS} )
do
    echo -e "which root do you want to use?\n"
    read root
    echo -e "which type of container do you want to create?\n"
    read machine
    if [ $machine == "dockerui" ]
    then
        sudo docker pull abh1nav/dockerui:latest
        sudo docker run -d -p $root:9000 -v /var/run/docker.sock:/docker.sock --name dockerui abh1nav/dockerui:latest -e="/docker.sock"
        echo "Done!\n"

    else
        sudo docker run -d -p $root:8080 $machine
        echo "Done!\n"
    fi
done
sudo docker ps
echo -e "Which kind of image do you want to Download?\n"
read IMAGE_get
echo "This is the available Images:"
sudo docker search $IMAGE_get
echo -e "Which Image's ID do you want to Download?\n"
read download_im
sudo docker pull $download_im
echo "Done!\n"
sudo docker images
echo -e "Do you want to remove container or image?\n"
read REMOVE
if [ $REMOVE == "container" ]
then
    echo "There are the existing containers:"
	echo "--------------------"
    sudo docker ps -a
	echo "--------------------"
    echo -e "Enter the container's id you want to remove:"
    read id_name
    sudo docker stop $id_name
    sudo docker rm $id_name
    echo "Done!"
    sudo docker ps -a
elif [ $REMOVE == "image" ]
then
    echo "There are the existing images:"
    sudo docker images
    echo -e "Enter the image's id you want to remove:\n"
    read id_z
    sudo docker rmi $id_z
    echo "Done!"
    sudo docker images
fi
