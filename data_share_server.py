import os
os.system("sudo apt-get install nfs-kernel-server")
path=input("Give the path to share: ")
os.system("sudo /etc/init.d/nfs-kernel-server start")
ip=input("Give the IP to whom you want to share: ")
data_to_write=path+" "+ip+"(rw,sync,no_root_squash,no_subtree_check)"
print(data_to_write)
#os.system("sudo su")
file=open('/etc/exports','a')
#file.read()
file.write("\n")
file.write(data_to_write)
os.system(" sudo exportfs -u")
#file.write(data_to_write)
