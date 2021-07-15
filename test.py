import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name":"junk","views":420,"likes":10},
        {"name":"stuff","views":69,"likes":420},
        {"name":"X-mas20","views":12,"likes":25}
        ]

''' loop to load data '''
for i in range(len(data)):
    respI= requests.put(BASE + "video/" + str(i), data[i])
    print(respI.json())

#response = requests.get(BASE + "helloworld/David")
#print(response.json())

# put data to memory
#resp2 = requests.put(BASE + "video/1", {"name":"junk","views":420,"likes":10})
#print(resp2.json())
input()

''' prove delete works '''
respD = requests.delete(BASE + "video/0")
print(respD)

input()

''' prove get works '''
# get last id
respN = requests.get(BASE + "video/" + str(i))
print(respN.json())

input()

''' prove update works; need to modify values manually'''
respU = requests.patch(BASE + "video/" + str(i-1), {"views":7600,"likes":101})
print(requests.get(BASE + "video/" + str(i-1)).json())

input()

''' prove non-existant id error works '''
respI1 = requests.get(BASE + "video/" + str(i+1))
print(respI1.json())