from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

username = 
password =

ip = "10.70.0.1"
ip2 = "10.70.0.11"
ios_device = {
  'device_type': 'cisco_ios',
  'ip': ip,
  'username': username,
  'password': password
}

ios_device2 = {
  'device_type': 'cisco_ios',
  'ip': ip2,
  'username': username,
  'password': password
}

net_connect = ConnectHandler(**ios_device)
net_connect2 = ConnectHandler(**ios_device2)

swCmd = net_connect.send_command('show switch | beg 1')
swCmd2 = net_connect2.send_command('show switch | beg 1')

swCnt = swCmd.splitlines()

swCntClean = swCnt.remove(' ')
