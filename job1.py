#!/bin/python3
#Job_1
#-Start-
import os
import boto3
from time import sleep
#Part-1
client = boto3.client('ec2')
response = client.describe_instances()
for r in response['Reservations']:
    for i in r['Instances']:
        print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PublicIpAddress'] + "\n---------------------------------------")
#Part-2
print("Install the packages!")
os.system('scp -i ./net4u_new.pem ./victor.sh ubuntu@---ipadd---:/home/ubuntu')
os.system('ssh -i "net4u_new.pem" ubuntu@--------.us-east-2.compute.amazonaws.com')
print('Run victor.sh')
os.system('scp -i ./net4u_new.pem ./victor.sh ubuntu@3.14.70.202:/home/ubuntu')
os.system('ssh -i "net4u_new.pem" ubuntu@--------.us-east-2.compute.amazonaws.com')
print('Run victor.sh')
