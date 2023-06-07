def ip_to_bin(ipaddr):
    """
    This function changes dec IP-address to binary

    Parameters:
    -----------
    ipaddr:
        dec IP-address
    
    Returns:
    --------
    ipaddr:
        binary IP-address
    """
    ipaddr = ipaddr.split(".")
    ipaddr = "{:08b}{:08b}{:08b}{:08b}".format(int(ipaddr[0]), int(ipaddr[1]), int(ipaddr[2]), int(ipaddr[3]))

    return ipaddr

def bin_to_ip(ip_bin):
    """
    This function converts binary IP-address to dec

    Parameters:
    -----------
    ip_bin:
        binary IP-address
    
    Returns:
    --------
    ipaddr:
        dec IP-address
    """

    ipaddr = ""
    j = 0
    for i in ip_bin:
        j += 1
        if j <= 8:
            ipaddr += i
        else:
            j = 1
            ipaddr += "."
            ipaddr += i

    ip_list = ipaddr.split(".")

    ipaddr = ""
    j = 0
    for i in ip_list:
        ipaddr += str(int(i, 2))
        j += 1
        if j <= 3:
            ipaddr += "."

    return ipaddr

def slash_mask_to_ip(mask):
    """
    Takes a mask in slash-form and returns mask in dec
    """
    mask_bin = ""
    for i in range(int(mask)):
        mask_bin += "1" 
    while len(mask_bin) < 32:
        mask_bin += "0"
    mask = bin_to_ip(mask_bin)
    return mask

