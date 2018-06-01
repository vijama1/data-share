#!/usr/bin/python3
import subprocess as sp


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
