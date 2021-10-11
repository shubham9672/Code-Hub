"""
This program creates subnets from given IP-address and needed host-count and 
creates markdown tables with the needed information
"""


import os.path
import os
from os import path
from subnetting_function import subnetting
from network_functions import network
from ip_addition import ip_addition

valid_network = False
valid_hosts = False

while not valid_network:
    try:
        starting_network = input("What network do you want to subnet? (format ex. 192.168.0.1/24): ")
        splitted_network = starting_network.split("/")
        network_mask = int(splitted_network[1])
        #check that mask is big enough
        if network_mask >= 31:
            print("Please enter a correct mask")
            continue
        #check that ip is correctly input
        ipaddr = splitted_network[0]
        ipaddr_validation_test = ipaddr.split(".")
        if len(ipaddr_validation_test) > 4:
            print("Incorrect IP-address for network, try again")
            continue 
        for i in range(4):
            int(ipaddr_validation_test[i])
        #check that IP-address values are between 0-255
        ip_value_too_high = False
        for ip_segment in ipaddr_validation_test:
            if int(ip_segment) > 255 or int(ip_segment) < 0:
                print("Not a valid IP-address, try again")
                ip_value_too_high = True
                break
        if ip_value_too_high:
            continue
        valid_network = True
    except ValueError:
        print("Please enter only numbers")
    except IndexError:
        print("Incorrect input, try again")

while not valid_hosts:    
    try:
        hosts = int(input("How many hosts you need to have?: "))
        if hosts > 0:
            valid_subnet_mask = False
            for i in range(1,33):
                    if hosts <= 2 ** i - 2:
                        subnet_mask = 32 - i
                        host_count = 2 ** i - 2
                        valid_subnet_mask = True
                        break
            if valid_subnet_mask:
                if network_mask <= subnet_mask:
                    valid_hosts = True
                else:
                    print("Error: Network too small for subnetting")
                    continue
            else:
                print("Error: Too many hosts, please enter a smaller number.")
                continue
        else:
            print("Please enter a positive number")
            continue
    except ValueError:
        print("Please enter a number")

interval = host_count + 2
amount_of_subnets = 2 ** (subnet_mask - network_mask)
network_base = network(ipaddr, network_mask)
file_name = network_base
working_dir = os.getcwd()
i = 1
while True:
    if path.exists("{}.txt".format(file_name)):
        file_name = network_base + "({})".format(i)
        i += 1
    else:
        break

for i in range(amount_of_subnets):
    subnet_ip = ip_addition(network_base, interval * i)
    subnetting(subnet_ip, subnet_mask, host_count, file_name)
print("Tables are ready in {}/{}.txt".format(working_dir, file_name))

