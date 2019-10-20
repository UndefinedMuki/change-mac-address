import os

#ipconfig_output = os.system('ipconfig /all')
ipconfig_output = os.popen('ipconfig /all').read()
innerResult = {}
result = []

for row in ipconfig_output.split('\n'):
    if row and row[0] != ' ':
        result.append(row.strip(':'))
#        key, value = row.split(': ')
#        result[key.strip(' .')] = value.strip()
    else:
        if ': ' in row:
            key, value = row.split(': ')
            #innerResult

print(result)

#print(type(t))
#CloseKey(hkey) - closes a previously opened

#import subprocess
#output = subprocess.check_output("ipconfig /displaydns", shell=True)
#result = {}
#for row in output.split('\n'):
#    if ': ' in row:
#        key, value = row.split(': ')
#        result[key.strip(' .')] = value.strip()
#
#print(result)
#print(result['A (Host) Record'])
