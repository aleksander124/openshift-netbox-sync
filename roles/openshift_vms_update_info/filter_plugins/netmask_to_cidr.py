# netmask_to_cidr.py

def netmask_to_cidr(netmask):
    octets = netmask.split('.')
    cidr = sum(bin(int(octet)).count('1') for octet in octets)
    return "/" + str(cidr)

class FilterModule:
    def filters(self):
        return {
            'netmask_to_cidr': netmask_to_cidr,
        }