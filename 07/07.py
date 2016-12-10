import re

def test_tls(s):
    for i in range(0, len(s) - 3):
        if s[i] != s[i+1] and s[i] == s[i+3] and s[i+1] == s[i+2]:
            return True          
    return False    

def test_ip_tls(ip):
    found = False
    for i in range(0, len(ip)):
        if i % 2 and test_tls(ip[i]):
            return False
        elif not i % 2 and test_tls(ip[i]):
            found = True
    return found

def find_abas(s):
    abas = []
    for i in range(0, len(s) - 2):
        if s[i] != s[i+1] and s[i] == s[i+2]:
            abas.append(''.join([s[i], s[i+1], s[i+2]]))       
    return abas

def find_bab(s, aba):
    for i in range(0, len(s) - 2):
        if ''.join([s[i], s[i+1], s[i+2]]) == ''.join([aba[1], aba[0], aba[1]]):
            return True
    return False

def test_ip_ssl(ip):
    for i in range(0, len(ip) / 2 + 1):
        abas = find_abas(ip[2*i])
        if not len(abas):
            continue
        for j in range(0, (len(ip) - 2) / 2 + 1):
            for aba in abas:
                if find_bab(ip[2*j+1], aba):
                    return True
    return False

ips = []
with open('input.txt', 'r') as f:
    ips = map(lambda x: re.split('\[|\]', x), f.read().splitlines())

print 'Number of TLS IPs: ' + str(len(filter(lambda x: test_ip_tls(x), ips)))
print 'Number of SSL IPs: ' + str(len(filter(lambda x: test_ip_ssl(x), ips)))