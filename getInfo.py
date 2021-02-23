#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from net_models import getHostname, getModel, getSerial, getVersion

username = input('Enter your SSH username: ')
password = getpass()

serialNumbers = []
modelNumbers = []

with open('devices_file') as f:
  devices_list = f.read().splitlines()

for devices in devices_list:
  print ('Connecting to device" ' + devices)
  ip_address_of_device = devices
  ios_device = {
      'device_type': 'cisco_ios',
      'ip': ip_address_of_device,
      'username': username,
      'password': password
  }

  try:
      net_connect = ConnectHandler(**ios_device)
  except (AuthenticationException):
      print ('Authentication failure: ' + ip_address_of_device)
      continue
  except (NetMikoTimeoutException):
      print ('Timeout to device: ' + ip_address_of_device)
      continue
  except (EOFError):
      print ('End of file while attempting device ' + ip_address_of_device)
      continue
  except (SSHException):
      print ('SSH Issue. Are you sure SSH is enabled? ' + ip_address_of_device)
      continue
  except Exception as unknown_error:
      print ('Some other error: ' + str(unknown_error))
      continue

    nameOut = net_connect.send_command('show run | i hostname')

    verOut = net_connect.send_command('show run | i version')

    modOut = net_connect.send_command('show version | i Model Number')

    serOut = net_connect.send_command('show ver | i Motherboard Serial Number')
    serSp = serOut.splitlines()
    for ser in serSp:
        getSerial(ser)
