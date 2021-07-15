import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name":"junk","views":420,"likes":10},
        {"name":"stuff","views":69,"likes":420},
        {"name":"X-mas20","views":12,"likes":25}
        ]

for i in range(len(data)):
    respI= requests.put(BASE + "video/" + str(i), data[i])
    print(respI.json())

#response = requests.get(BASE + "helloworld/David")
#print(response.json())

# put data to memory
#resp2 = requests.put(BASE + "video/1", {"name":"junk","views":420,"likes":10})
#print(resp2.json())
input()

respD = requests.delete(BASE + "video/0")
print(respD)

input()
# get last id
respN = requests.get(BASE + "video/" + str(i))
print(respN.json())

input()
respU = requests.patch(BASE + "video/" + str(i-1), {"views":7600}, {"likes":101})
print(requests.get(BASE + "video/" + str(i-1)).json())

input()
# get non-exsistant id
respI1 = requests.get(BASE + "video/" + str(i+1))
print(respI1.json())