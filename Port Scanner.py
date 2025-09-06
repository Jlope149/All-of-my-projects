import nmap

nm = nmap.PortScanner()

target = "45.33.32.156"
options = "-sV -sC scan_results"    #how we use nmap; sV gives version info; sC = standard nmap script

nm.scan(target, arguments=options) # scans inputted IP and what to look for

for host in nm.all_hosts(): #outer loop    #nested loop; goes through results of nmap scan; print info of each protocol and port
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():   #inter loop
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))
