
import pandas as pd    

def get_attack_labels():
    return {'normal': 0, 'generic': 1, 'exploits': 2, 'fuzzers': 3, 'dos': 4, 'reconnaissance': 5, 'analysis': 6, 'backdoors': 7, 'shellcode': 8, 'worms': 9}
    
def get_common_services():
    return ['FIN', 'CON', 'INT', 'REQ', 'RST', 'ECO', 'CLO']
    
def get_common_protos():
    return ['tcp', 'udp', 'unas', 'arp', 'ospf']

def get_common_states():
    return ['FIN', 'CON', 'INT', 'REQ']
    