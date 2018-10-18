
import subprocess as sp
import os

print("Choose wether you want to send or recive ")
print("send || recive ")
in=input()
if in =='send':
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


elif in=='recive':
	service_check=os.system("service --status-all | grep nfs-common")
	if service_check!=0:
	    os.system("sudo apt-get install nfs-common")

	inp = input('Enter the ip address of the server : ')
	host = inp+':/shome'
	dir = input('Enter the path where server files accses : ')
	arr=['sudo','mount',host,dir]
	proc = sp.Popen(arr,stdout=sp.PIPE,stderr=sp.PIPE)
	(out,err) = proc.communicate()
	print(out)
	print(err)
	f = open('/etc/fstab','a+')
	f.read()
	f.write('\n')
	f.write(host+' '+dir+' nfs,rw,sync,hard,intr 0 0')
	proc1 = sp.Popen(['mount'],stdout=sp.PIPE,stderr=sp.PIPE)

else :
	print("Error")
	
