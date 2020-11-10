#!/bin/python3
#Job_2
import boto3
import os
#------------------run

print("creating 2 instances!")
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
ImageId='ami-0e82959d4ed12de3f',
MinCount=1,
MaxCount=2,
InstanceType='t2.micro',
KeyName='net4u_new'
)

print("Done")
print("Installing all packages!\n")

print("Install python3.7")
os.system('sudo apt update -y')
os.system('sudo apt install software-properties-common')
os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
os.system('sudo apt update -y')
os.system('sudo apt install python3.7')
os.system('sudo python --version')
print("Done")
print("install Docker!")
os.system('sudo curl -fsSL https://get.docker.com -o get-docker.sh')
os.system('sudo sh get-docker.sh')
print("Done")
print("Install Ansible!")
os.system('sudo apt update -y')
os.system('sudo apt install software-properties-common')
os.system('sudo apt-add-repository --yes --update ppa:ansible/ansible')
os.system('sudo apt install ansible')
print("Done")
print("Install Net-tools")
os.system('sudo apt-get update -y')
os.system('sudo apt-get install -y net-tools')
print("Done")
print("Change etc/host---\n")
host=input("Enter hostname:")
remote_ip=input("Enter your ip:")
SetHostAt(remote_ip)
print("Done")
print("Change your Hostname!\n")
os.system('apt-get install systemd -y')
new_hostname=("New_Machine")
os.system('sudo hostnamectl set-hostname ' + new_hostname)
os.system('hostnamectl')
print("Your new host name is::\n")
os.system('hostname')
print("Change Root Password ! !!")
os.system('sudo passwd root')
print("Done")
print("Installing NetPerf!")
os.system('sudo apt-get update -y')
os.system('sudo apt-get install -y netperf')
print("Done!")
