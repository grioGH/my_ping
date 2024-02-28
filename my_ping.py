import configparser
import subprocess
import platform
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d.%m.%Y %H:%M:%S")
now=date_time

config = configparser.ConfigParser()
config.read('my_ping.ini')
ip_addr=config['CMPROD']['Ipaddr']
print(ip_addr)
config = configparser.ConfigParser()
config['CMPROD'] = {'Status': 'CONNECTED','Ipaddr':ip_addr,'Date':now}

#ip_addr = '0.0.0.0'
def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]

    result = subprocess.run(command, stdout=subprocess.PIPE)
    output = result.stdout.decode('ANSI')
    if "Request timed out." in output or "100% packet loss" in output:
        return "NOT CONNECTED"
        config['CMPROD'] = {'Status': 'NOT CONNECTED','Ipaddr':ip_addr,'Date':now}
    return "CONNECTED"
    config['CMPROD'] = {'Status': 'CONNECTED','Ipaddr':ip_addr,'Date':now}
with open('my_ping.ini', 'w') as configfile:
  config.write(configfile)

print(ping(ip_addr))
