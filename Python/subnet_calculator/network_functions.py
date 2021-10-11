from ip_conversions import *

def network(ipaddr, mask):
    """
    Functio takes IP-address and mask to calculate the network base address

    Parameters:
    -----------
    ipaddr:
        dec IP-address
    mask:
        subnet mask
    
    Returns:
    --------
    new_ip:
        network base IP
    """

    mask_ip = slash_mask_to_ip(mask)
    mask_bin = ip_to_bin(mask_ip)
    ipaddr = ip_to_bin(ipaddr)

    network_ipaddr = ""
    j = 0
    for i in ipaddr:
        if i == "1" and mask_bin[j] == "1":
            j += 1    
            network_ipaddr += "1"
        else:
            j += 1
            network_ipaddr += "0"

    new_ip = bin_to_ip(network_ipaddr)

    return new_ip

def broadcast(ipaddr, mask):
    """
    Functio takes IP-address and mask to calculate the broadcast address

    Parameters:
    -----------
    ipaddr:
        dec IP
    mask:
        subnet mask
    
    Returns:
    --------
    new_broadcast:
        network broadcast IP
    """
    ipaddr = ip_to_bin(ipaddr)
    broadcast = ""
    for i in range(mask):
        broadcast += ipaddr[i]
    while len(broadcast) < 32:
        broadcast += "1"
    new_broadcast = bin_to_ip(broadcast)
    
    return new_broadcast