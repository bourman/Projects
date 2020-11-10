#!/bin/python3
#Menu_controller:
from time import sleep
import os
#start-
def menu():
	while(True):
		choice = input('\n-------\nMenu:\n------\n1)Discover all Ips in network\n2)Install full packages CentOs\n3)Install full packages Ubuntu\n4)Install Jenkins Master\n--------------------\nEnter your choice: ')
		if (choice == "1"):
			N_map()
		elif (choice == "2"):
			CentOS()
		elif (choice == "3"):
			Ubuntu()
		elif (choice == "4"):
			set_jenkins()
		else:
			print("----------\nEnter please only 1-4 !! \n----------\n")
			continue
		if (input("Do you want to quit?  yes/no\n") == "yes"):
			break
	sleep(2)
	print('Thanks and good bye!!')
#---------------1
def N_map():
	os.system('sudo apt-get install nmap')
	ip_add = input('Enter your Ip Address + SM :')
	print('Checking which Ip Address is connected to the system....')
	sleep(2)
	os.system('nmap -v -sn'+ip_add)
#---------------2
def CentOS():
	os.system('sudo yum install gcc openssl-devel bzip2-devel libffi-devel ;sudo cd /usr/src ; sudo wget https://www.python.org/ftp/python/3.7.9/Python-3.7.8.tgz')
	os.system('tar xzf Python-3.7.9 ; cd Python-3.7.9 ; ./configure --enable-optimizatiobs ; make altinstall ; rm /user/src/Python-3.7.9.tgz ; python3.7 -V')
	os.system('sudo yum check-update ; curl -fsSL https://get.docker.com/ | sh ; sudo systemctl start docker ; sudo systemctl status docker ; sudo systemctl enable docker')
	os.system('sudo yum install epel-relese ; sudo yum install ansible')
	os.system('yum install -y net-tools')
	name_new = input('Enter new hostname: ')
	os.system('hostnamectl set-hostname' +name_new)
	print("Your new hostname is:")
	os.system('hostnamectl')
	passrootz = input('Are you sure u want to chagne password?  yes/no')
	if (passrootz == "yes"):
		print("Ok, lets change!\nEnter you new password:\n")
		os.system('sudo passwd root')
		print("Done!")
	else:
		print("Ok...")

#---------------3
def Ubuntu():
	os.system('sudo apt update')
	os.system('sudo apt install software-properties-common')
	os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
	os.system('sudo apt update')
	os.system('sudo apt install python3.7')
	print("Got python!")
	os.system('sudo python --version')
	os.system('sudo curl -fsSL https://get.docker.com -o get-docker.sh')
	os.system('sudo sh get-docker.sh')
	print("Got docker system")
	os.system('sudo apt update')
	os.system('sudo apt install software-properties-common')
	os.system('sudo apt-add-repository --yes --update ppa:ansible/ansible')
	os.system('sudo apt install ansible')
	print("Got Ansible")
	os.system('sudo apt-get update -y')
	os.system('sudo apt-get install -y net-tools')
	print("Got net-tools")
	host = input("Enter your new host: ")
	remote_ip = input("Enter your new Ip address: ")
	SetHostAt(remote_ip)
	print("Done!")
	os.system('sudo apt-get install systemd -y')
	new_hostname = input("Enter your new hostname: ")
	os.system('sudo hostnamectl set-hostname ' + new_hostname)
	os.system('hostnamectl')
	print("Your hostname is:")
	os.system('hostname')
	print("Change password")
	question = input("Are you sure you want to change password?  yes/no")
	if (question == "yes"):
		os.system('sudo passwd root')
		print("Your password has been changed")
	elif (question == "no"):
		print("Ok...")
#---------------4
def set_jenkins():
	print("test")
	install = input("Do you want install jenkins to another machine?  yes/no\n")
	if install == "yes":
		username = input("Enter you username: ")
		ip = input("Enter you ip address: ")
		os.system('scp victor.sh ' + username + '@' + ip + ':/home/bourman1')
		os.system('ssh ' + username + '@' + ip)
		print("done!")
	else:
		print("ok")






menu()
