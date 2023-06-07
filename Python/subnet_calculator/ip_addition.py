from ip_conversions import ip_to_bin, bin_to_ip

def ip_addition(ip, addition):
    """
    This function takes 

    Parameters:
    -----------
    ip:
        dec IP-address
    addition:
        needed addition (can be negative)
    
    Returns:
    --------
    new_ip:
        dec IP-address after the addition
    """
    ipaddr = ip_to_bin(ip)
    ip_int = int(ipaddr, 2)
    ip_int += addition
    ip_bin = bin(ip_int)[2:].zfill(32)
    new_ip = bin_to_ip(ip_bin)     
    return new_ip


