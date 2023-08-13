import requests
import json

def paloL3Interface(interface, ipAddr):
    # XPath for configuring and interface
    url = "https://192.168.1.2/restapi/v10.2/Network/EthernetInterfaces?name=" + interface
    payload = {
            "entry": [
                {
                    "@name": interface,
                    "layer3": {
                        "ndp-proxy": {
                            "enabled": "no"
                        },
                        "ip": {
                            "entry": [
                                {
                                    "@name": ipAddr
                                }
                            ]
                        }
                    }
                }
            ]
        }
    print(url)
    print(payload)
    # encode payload as JSON
    body = json.dumps(payload)
    # Hard coded token
    headers = {
    'X-PAN-KEY': 'LUFRPT11Nm1EMXEvQTRSMDNVVHU1Zm5xOVJOWlJnN1k9TkJUTEgxbTVlSzkyaTN4S1EvWmcvWlJZMEw0aDVtQk83SzQyWXI5VHJXcW5XUXZKMVplNnNZWFFsTlVXNzU1Yw==',
    'Content-Type': 'application/json',
    }
    # POST Request to our firewall
    response = requests.request("POST", url, headers=headers, data=body, verify=False)
    print(response.json())

# Strings as variables
interface = 'ethernet1/5'
ipAddr = '192.168.105.1/24'
# Call our Function using Strings
paloL3Interface(interface, ipAddr)


# Lists containg variables, 1 to 1 mapping between interface and IP address
interfaceList = ['ethernet1/1', 'ethernet1/2', 'ethernet1/3', 'ethernet1/4', 'ethernet1/5']
ipAddrList = ['192.168.101.1/24', '192.168.102.1/24', '192.168.103.1/24', '192.168.104.1/24', '192.168.105.1/24']

# Call our Function using the first value [0] in our Lists
paloL3Interface(interfaceList[0], ipAddrList[0])

# Dictionary Containg our varialbes
interfaceData = {'ethernet1/1': '192.168.101.1', 'ethernet1/2': '192.168.102.1', 'ethernet1/3': '192.168.103.1', 'ethernet1/4': '192.168.104.1', 'ethernet1/5': '192.168.105.1'}


# For look to cycle through our Dictionary
for key in interfaceData:
    print(key, interfaceData[key])
    paloL3Interface(key, interfaceData[key])


