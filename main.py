""" Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from dnacentersdk import api
import pprint
import requests.packages.urllib3
import config
from netmiko import ConnectHandler


requests.packages.urllib3.disable_warnings()

dnac = api.DNACenterAPI(username=config.username,
                        password=config.password,
                        base_url=config.base_url,
                        version='2.1.2',
                        verify=False,
                        single_request_timeout=99999,
                        debug=False)

aps = dnac.devices.get_device_list(family="Unified AP")
ap_ids = []

for ap in aps["response"]:
    ap_ids.append(ap["id"])

switches = dnac.devices.get_device_list(family="Switches and Hubs")
switch_ids = []

for switch in switches["response"]:
    if switch['type'].startswith("Cisco Catalyst"):
        switch_ids.append(switch["id"])

links = dnac.topology.get_physical_topology()["response"]["links"]

# each entry will include the switch ip address , switchport, and ap name
data_set = []

for link in links:
    if link["source"] in ap_ids:
        if link["target"] in switch_ids:
            temp={}
            
            access_point = dnac.devices.get_device_by_id(id=link["source"])


            switch = dnac.devices.get_device_by_id(id=link["target"])
            temp["ip"] = switch["response"]["managementIpAddress"]
            temp["ap_hostname"] = access_point["response"]["hostname"]

            temp["switchport"] = link["endPortName"]

            file_obj1 = open("location.txt","a")
            file_obj1.write("Access point " + temp["ap_hostname"] + " connected to " + str(switch["response"]["hostname"]) + " on port " + str(link["endPortName"]))
            file_obj1.close()



            data_set.append(temp)

for data in data_set:
    pprint.pprint(data)
    username,password = input("Enter ssh username and password for device " + data["ip"] + " : " ).split()

    confirm = input("Enter e to continue")

    if confirm.lower() == "e ":
        desc = "description connected to AP " + data["ap_hostname"]
        device = {
                "ip":data["ip"],
                "username":username,
                "password":password,
                "device_type":"cisco_ios"
            }

        try:
            net_connect = ConnectHandler(**device)
            net_connect.send_config_set(["int " + data["switchport"],desc])

            file_obj2 = open("log.txt","a")
            file_obj2.write("Device " + data["ip"] + " port " + data["switchport"] + " description changed")
            file_obj2.close()
        except:
            error_text = "unable to connnect to " + data["ip"]
            print(error_text)
            continue

    else:
        print("shutting off")