# run command
Script to run commands on multiple switches.

### Install
Install required packages using the requirements.txt
```
pip install -r requirements.txt
```

### Usage
1. Open the `devices.yaml` and input the IPs of the switches you want to connect to.
```
switches:
    sw1: 192.168.1.2
    sw2: 192.168.1.3
    sw3: 192.168.1.4
```
2. Run the script
```
python commands.py
```
3. The script will ask for a username and password. These will be stored to be used on all the switches.
```
Enter standard username: cisco
Enter standard password: 
```
4. The script will log into as many switches as it can and run the configuration update.
```
Connected to switch1..
```
5. It will then check the config after issuing the command.
```
Config updated for 192.168.1.2!
```
6. Done!
