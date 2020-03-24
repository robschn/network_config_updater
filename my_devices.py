import yaml
# from getpass import getpass

# with open('devices.yaml', 'r') as f:
#     doc = yaml.safe_load(f)

# switches = doc['switch']

device_ips = input('Current IP of the switch: ')

# for i in switches.keys():
#     device_ips.append(switches[i])

username = input('Enter standard username: ')
password = getpass('Enter standard password: ')

device_list = []

for ip_address in device_ips:
    curr_device = {
        "device_type": "cisco_ios",
        "ip": ip_address,
        "username": username,
        "password": password,
    }
    device_list.append(curr_device)
