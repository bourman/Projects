#!/bin/bash
#targil ansible
echo "[Gui]" | sudo tee -a /etc/ansible/hosts
echo "193.168.1.1 ansible_user=Victor" | sudo tee -a /etc/ansible/hosts
ansible -m ping all
ansible all -b -m apt 'name=apache2 state=latest'
ansible all -b -m apt 'name=net-tools state=latest'
ansible -m shell -a 'touch 1.txt 2.txt 3.txt 4.txt 5.txt' all
ansible -m shell -a 'tar -zcbf victor.tgz 1.txt 2.txt 3.txt 4.txt 5.txt' all
ansible -m shell -a 'rm *tgz' all
ansible all -b -m a[t 'name=tcdump state=latest'
ansible -m -a shell 'sudo reboot' all
