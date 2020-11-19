import telnetlib
import getpass

HOST = input("Enter the ip add : ")
User = input("Enter the username : ")
psw = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(User.encode('ascii') + b"\n")

if psw:
    tn.read_until(b"Password: ")
    tn.write(psw.encode('ascii') +b"\n")

tn.write(b"enable\n")


if HOST == "192.168.122.130":
    print("Entre the switch ")
    pssw = getpass.getpass()
    tn.write(pssw.encode('ascii') +b"\n")
    tn.write(b"conf t\n")
    tn.write(b"hostname Tanisha\n")
    for x in range(2,6):
        tn.write(b"vlan " + str(x).encode('ascii') +b"\n")
        tn.write(b"name python_vlan_" + str(x).encode('ascii') +b"\n")
        
else:
    print("Entre the Router ")
    psswr = getpass.getpass()
    tn.write(psswr.encode('ascii') +b"\n")
    tn.write(b"conf t\n")
    tn.write(b"hostname Robin\n")
    tn.write(b"do sh ip int br\n")
    
tn.write(b"end\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

    
