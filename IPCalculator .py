x=input('Write IP: ')
ip=x.split('.')
bitip=[]
if len(ip) > 4 or (int(ip[0]) > 255 or int(ip[1]) > 255 or int(ip[2]) > 255 or int(ip[3]) > 255) or (int(ip[0]) < 0 or int(ip[1]) < 0 or int(ip[2]) < 0 or int(ip[3]) < 0):
    print("This is Not An IP Address")
else:
    for ipitem in ip:
        ipitem=int(ipitem)
        # print(ipitem)
        ip2=['0','0','0','0','0','0','0','0']
        while ipitem > 0:
            if ipitem >= 128:
                ipitem=ipitem-128
                ip2[0]="1"
            elif ipitem >= 64 and ipitem < 128:
                ipitem=ipitem-64
                ip2[1]="1"
            elif ipitem >= 32 and ipitem < 64:
                ipitem=ipitem-32
                ip2[2]="1"
            elif ipitem >= 16 and ipitem < 32:
                ipitem=ipitem-16
                ip2[3]="1"
            elif ipitem >= 8 and ipitem < 16:
                ipitem=ipitem-8
                ip2[4]="1"
            elif ipitem >= 4 and ipitem < 8:
                ipitem=ipitem-4
                ip2[5]="1"
            elif ipitem >= 2 and ipitem < 4:
                ipitem=ipitem-2
                ip2[6]="1"
            elif ipitem >= 1 and ipitem < 2:
                ipitem=ipitem-1
                ip2[7]="1"
        # bitip=bitip.join(ip2)+'.'
        # ip2.clear()
        # print(bitip)
        # print(ip2)
        s=''.join(ip2)
        bitip.append(s)
        # print(bitip)
        # print(ipitem)
    print('.'.join(bitip))