from scapy.all import *
#from scapy import *

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      #print "ARP Probe from: " + pkt[ARP].hwsrc
      if pkt[ARP].hwsrc == '10:ae:60:77:f4:8e': # Tide
        print "Pushed Tide Dash Button, with a MAC Address of: " + pkt[ARP].hwsrc
      else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)