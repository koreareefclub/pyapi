#!/usr/bin/env python3
from subprocess import call ## <-------- changed
call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
call(["ip", "addr", "show", "dev", interface])  ## <--- changed
call(["ip", "route", "show", "dev", interface]) ## <--- changed

