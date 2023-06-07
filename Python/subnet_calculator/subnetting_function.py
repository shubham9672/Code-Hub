from ip_addition import ip_addition
from network_functions import broadcast
from ip_conversions import slash_mask_to_ip

def subnetting(ipaddr, mask, host_count, file_name):
    """
    Function creates a markdown table from given values and adds them to a file

    Parameters:
    -----------
    ipaddr:
        dec IP-address
    mask:
        subnet mask
    host_count:
        amount of useable hosts
    file_name:
        name of the file where tables are saved
    
    Returns:
    --------
    """
    mask_slash = "/" + str(mask)
    bc = broadcast(ipaddr, mask)  
    start = ip_addition(ipaddr, 1)
    stop = ip_addition(bc, -1)
    mask_ip = slash_mask_to_ip(mask)

    filename = "{}.txt".format(file_name)
    file = open(filename, "a")
    file.write("| Specification                             | Subnet info        |\n")
    file.write("|-------------------------------------------|--------------------|\n")
    file.write("| New subnet mask                           | {0: <18} |\n".format(mask_ip + mask_slash))
    file.write("| Number of usable hosts in the subnet      | {0: <18} |\n".format(host_count))
    file.write("| Network address                           | {0: <18} |\n".format(ipaddr + mask_slash))
    file.write("| First IP Host address                     | {0: <18} |\n".format(start))
    file.write("| Last IP Host address                      | {0: <18} |\n".format(stop))
    file.write("| Broadcast address                         | {0: <18} |\n".format(bc))
    file.write("\n")
    file.close()




