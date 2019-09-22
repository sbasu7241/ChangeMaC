#!/usr/bin/env/python
import subprocess

subprocess.call("sudo ifconfig wlo1 down",shell=True)
subprocess.call("sudo ifconfig wlo1 hw ether 00:11:22:33:44:55",shell=True)
subprocess.call("sudo ifconfig wlo1 up",shell=True)


