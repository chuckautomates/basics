import requests
import json

# Generate a token using hardcoded username and password
url = "https://192.168.1.2/api/?type=keygen&user=admin&password=S3cr3tsecret"
response = requests.request("GET", url)
print(response.text)



# Interface configuation path contains interface name
url = "https://192.168.1.2/restapi/v10.2/Network/EthernetInterfaces?name=ethernet1/1"

# Example JSON payload for interface configuration
payload = json.dumps({
  "entry": [
    {
      "@name": "ethernet1/1",
      "layer3": {
        "ndp-proxy": {
          "enabled": "no"
        },
        "ip": {
          "entry": [
            {
              "@name": "192.168.101.1/24"
            }
          ]
        }
      }
    }
  ]
})

# Example headers with token
headers = {
  'X-PAN-KEY': 'LUFRPT1GenYxVm1iZThmQ0N3MEg3YnRpcjhrWlBUbHc9TkJUTEgxbTVlSzkyaTN4S1EvWmcvWnFXY1dFNVNuTFlWc05CUlJRTUdaakViMjN6R1hPUUQ3ZmlyY1RXdXNabA=='
}

# Swap out variables for interface name and IP address in JSON payload
payload = json.dumps({
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
})

# Swap out variable for interface name
url = "https://192.168.1.2/restapi/v10.2/Network/EthernetInterfaces?name=" + interface


# This will print out the concatination of the URL
interface = 'ethernet1/3'
url = "https://192.168.1.2/restapi/v10.2/Network/EthernetInterfaces?name=" + interface
print(url)


# Turn it into a function
def paloL3Interface(interface, ipAddr):
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
    body = json.dumps(payload)
    headers = {
    'X-PAN-KEY': 'LUFRPT1GenYxVm1iZThmQ0N3MEg3YnRpcjhrWlBUbHc9TkJUTEgxbTVlSzkyaTN4S1EvWmcvWnFXY1dFNVNuTFlWc05CUlJRTUdaakViMjN6R1hPUUQ3ZmlyY1RXdXNabA==',
    'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=body, verify=False)
    print(response.json())


# Call our function using hard coded strings
paloL3Interface('ethernet1/5', '192.168.105.1/24')

# Assigning values to a variable and calling our function with the variable
interface = 'ethernet1/5'
ipAddr = '192.168.105.1/24'
paloL3Interface(interface, ipAddr)
