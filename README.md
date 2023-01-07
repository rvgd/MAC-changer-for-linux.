# MAC-changer-for-linux.
Automated tool to change MAC Address with error handling.

# What is MAC Address
A MAC address (media access control address) is a 12-digit hexadecimal number assigned to each device connected to the network. Primarily specified as a unique identifier during device manufacturing, the MAC address is often found on a device's network interface card (NIC).

# Purpose of a MAC Address modifier
Changing the assigned MAC address may allow the user to bypass access control lists on servers or routers, either hiding a computer on a network or allowing it to impersonate another network device. It may also allow the user to bypass MAC address blacklisting to regain access to a Wi-Fi network.

# Features
1. Handled every possible errors to non-programmer readable information.
2. Flexiblity of input.
3. Input handling to prevent COMMAND INJUCTION.


# How to run 
For help
```
$ python3 macchanger.py --help
```
TO run 
```
$ sudo python macchanger.py -i [Interface] -m [New mac]
```
