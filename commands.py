from netmiko import ConnectHandler
from my_devices import device_list


def issue_command(a_device, config_commands):
    
    net_connect = ConnectHandler(**a_device)
    
    # Grab hostname
    find_hostname = net_connect.find_prompt()
    hostname = find_hostname.replace("#","")
    print(f'\nConnected to {hostname}..')

    # Send commands
    print(f'Sending commands... {config_commands}')
    show_inventory = net_connect.send_command(config_commands)

    # Output to file
    f = open(f'{hostname}.txt', 'w')
    f.write(show_inventory)
    f.close()
    

def main():

    commands = 'show inventory'

    for device in device_list:
        issue_command(device, commands)

if __name__ == "__main__":
    main()
