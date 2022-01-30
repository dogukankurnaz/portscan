from logging import exception
import socket

site = input("Hedef: ")
target = socket.gethostbyname(site)

print("-"*50)
print("Tarama baslatildi." + target)
print("-"*50)

try:
    for port in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} Açık".format(port))
        s.close()
except Exception as e:
    print("HATA!", e)
