#!/bin/bash
#install_all.sh
sudo apt-get update -y
sudo apt install openssh-server -y
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7
sudo python ––version
echo "Change your hostname: "
sudo apt-get install systemd -y
echo -e "Your new hostname: "
read hostname
sudo hostnamectl set-hostname $hostname
hostnamectl
echo "Your new hostname: "
hostname
sudo visudo
sudo nano /etc/hosts
ssh-keygen -t rsa
echo -e "Enter your key name: "
read key_name
echo -e "Enter your user: "
read user
echo -e "Enter your host: "
read host
ssh-copy-id -i $key_name $user@$host
echo "Done"
