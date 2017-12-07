devices=[]
file=open("devices.txt", "a")

while True:
    deviceInput = input("Add in a new Cisco Device ")

    if deviceInput == 'exit' or deviceInput == 'Exit':
        file.close()
        break

    file.write(deviceInput + "\n")


file=open("devices.txt","r")

for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)
