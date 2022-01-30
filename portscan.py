from logging import exception
import socket

site = input("Hedef: ")
target = socket.gethostbyname(site)

print("-"*50)
print("Tarama baslatildi: " + target)
print("-"*50)
1024
try:
    x = []
    for port in range(1,54):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            a =("Port {} Açık".format(port))
            x.append(str(a) + "\n")
            print(a)
        s.close()
    with open("openports.txt","w",encoding="utf-8") as saved:
        saved.writelines(site + "\n"+"Açık Portlar:"+ "\n")
        saved.writelines(x)
except Exception as e:
    print("HATA!", e)
