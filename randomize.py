import random

hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def randomMACAddress():
    macAddress = ""
    for i in range(1, 18):
        if i%3 == 0:
            macAddress += ":"
        else:
            macAddress += random.choice(hex)
    return macAddress

print(randomMACAddress())
