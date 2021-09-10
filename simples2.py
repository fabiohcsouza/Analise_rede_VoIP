import os

portal1 = 
portal2 = 













ipl = input('Informe os IP separado por : ')
ipl_split = (ipl.split())




for ip in ipl_split:

    response = os.popen('ping /l 160 ' + ip).read()

    if 'TTL' in response:
        print(response)
