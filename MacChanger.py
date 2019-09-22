#!/usr/bin/env/python
import subprocess

interface = "wlo1"
new_mac = "00:11:22:33:44:55"

interface = input("interface > ")
new_mac = input("new MAC > ")

print(interface)
print(new_mac)

print("[+] Changing MAC address for "+interface+" to "+ new_mac)

subprocess.call("sudo ifconfig "+interface+" down",shell=True)
subprocess.call("sudo ifconfig "+interface+" hw ether "+new_mac,shell=True)
subprocess.call("sudo ifconfig "+interface+" up",shell=True)


