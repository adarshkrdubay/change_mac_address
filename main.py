import os
if not 'SUDO_UID' in os.environ.keys():
    print("Run this program with sudo.")
    exit()
print("\n*****************************************************************")
print("\n* Copyright of AKD, 2022                                        *")
print("\n* https://www.adarshkrdubay.github.io                           *")
print("\n*****************************************************************")
os.system("ls /sys/class/net/ > .intfear.lis")
intf_list=[]
listfile=open(".intfear.lis","r")
for fill in listfile:
        intf_list.append(fill.replace("\n",""))
for div in intf_list:
               os.system(f"cat /sys/class/net/{div}/address > .{div}.mac")
               macid=open(f".{div}.mac","r")
               macid=macid.read()
               print(f"{div} : {macid}")
interface_name=input("Enter the interface for which you want to change the MAC ID:\n")
if interface_name in intf_list:
	print(f"{interface_name} selected")
	new_mac_id=input(f"""Enter the new MAC ID for {interface_name} (Example : 12:34:56:78:90:01):\n""")
	if new_mac_id == "":
		Print("No MAC ID provided .")
	else:
		print(f"Changing {interface_name} MAC ID to {new_mac_id}.")
		print("Your system will disconected from the network during this process.")
		os.system(f"sudo ifconfig {interface_name} down")
		os.system(f"sudo ifconfig {interface_name} hw ether {new_mac_id}")
		os.system(f"sudo ifconfig {interface_name} up")
		print(f"Your MAC ID is changed to {new_mac_id}")

else:
	print("No such interface")
back_to_same=input(f"Press Enter to change MAC ID back to normel:\n")
if back_to_same=="":
    old_mac_id=open(f".{interface_name}.mac","r")
    old_mac_id=old_mac_id.read()
    print(f"Changing {interface_name} MAC ID to {old_mac_id}")
    print("Your system will disconected from the network during this process.")
    os.system(f"sudo ifconfig {interface_name} down")
    os.system(f"sudo ifconfig {interface_name} hw ether {old_mac_id}")
    os.system(f"sudo ifconfig {interface_name} up")
    print(f"Your MAC ID is changed to {old_mac_id}")
else:
    print("Bye ")
exit()

