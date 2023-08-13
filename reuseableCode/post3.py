import requests
import json


def paloGenerateToken(username, password, firewall):
    # Generate XPath for token on Palo Alto Firewall
    url = 'https://' + firewall + '/api/?type=keygen&user=' + username + '&password=' + password
    # Send token GET request with SSL Verify off
    response = requests.request("GET", url, verify=False)
    print(response.text)
    # Split XML response at <key>
    a = response.text.split('<key>')
    # Split XML again at </key>
    b = a[1].split('</key>')
    # Return just the token
    return(b[0])



def paloL3Interface(firewall, interface, ipAddr):
    # XPath for configuring interfaces
    url = 'https://' + firewall + '/restapi/v10.2/Network/EthernetInterfaces?name=' + interface
    # Interface configuration payload in JSON
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
    # Post payload
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload), verify=False)
    return(response.json())

# Create variables
username = 'admin'
password = 'S3cr3tsecret'
firewall = '192.168.1.2'

# Call Generate Token function
token = paloGenerateToken(username, password, firewall)

# Apply token to headers
headers = {'X-PAN-KEY': token,
            'Content-Type': 'application/json'}

# Interface mappings
interfaceData = {'ethernet1/1': '192.168.101.1', 'ethernet1/2': '192.168.102.1', 'ethernet1/3': '192.168.103.1', 'ethernet1/4': '192.168.104.1', 'ethernet1/5': '192.168.105.1'}

# Cycle through interface mapping and apply
for key in interfaceData:
    print(key, interfaceData[key])
    paloL3Interface(firewall, key, interfaceData[key])

