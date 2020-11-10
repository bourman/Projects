#!/bin/bash
#ansible
echo -e "Enter the master's IP:\n"
read IP
echo -e "how many clients do you want to create?\n"
read clients
for i in $( eval echo {1..$clients} )
do
    echo -e "Enter the client's IP:\n"
    read client
    echo -e "Enter your username:\n"
    read username
    scp install_all.sh $username@$client:/home/$username
    echo "Run install_all.sh!"
    ssh $username@$client
    echo "done!"
done
echo -e "installing ansible server..."
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
echo "done!"
