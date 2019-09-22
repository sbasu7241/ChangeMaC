
#!/usr/bin/env/python
import subprocess
from optparse import OptionParser

def change_mac(interface,new_mac):
	print("[+] Changing MAC address for "+interface+" to "+ new_mac)

	subprocess.call(["sudo","ifconfig",interface,"down"])
	subprocess.call(["sudo","ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["sudo","ifconfig",interface,"up"])


def get_arguments():
	parser = OptionParser()

	parser.add_option("-i","--interface",dest="interface",help="Inteface to change MAC Address")
	parser.add_option("-m","--mac",dest="new_mac",help="New MAC Address")

	return parser.parse_args()

(options,arguments) = get_arguments()
change_mac(options.interface,options.new_mac)

