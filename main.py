import socket

try:

    times= int(input("Enter the number of times to resolve the IP address: "))
    attempt=1
    while times>0:
        print("Attempt", attempt)
        url=input("Enter Website (eg. www.example.com): ")
        ip=socket.gethostbyname(url)
        print("The IP address of",url, "is:",ip)
        times-=1
        attempt+=1

except Exception as e:
    print("Error:", e)