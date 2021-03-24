# GVE_DevNet_DNA_AP_Locator
prototype script that locates which switchport an AP is connected to and updates the pertaining port description with the hostname of the AP


## Contacts
* Jorge Banegas

## Solution Components
* DNAC
* Catalyst 9K

## Installation/Configuration


1. First step will be to include the credentials of your DNAC instance into the config.py file

```python
  username=""
  password=""
  base_url=""
```
2. Create virtual environment and name it env, then activate it

```console
foo@bar:~$ virtualenv env
foo@bar:~$ source env/bin/activate
```

4. Install the dependencies required for the python script
```console
foo@bar(env):~$ pip install -r requirements.txt
```

## Usage

To launch script:


    ```console
    foo@bar(env):~$ python main.py
    ```

# Screenshots
After starting the script, it will log the location of the Access Point in the location.txt file

![/IMAGES/location.png](/IMAGES/location.png)

Afterwards, it will ask the user the ssh credentials in order to change the description of the switchport

![/IMAGES/step1.png](/IMAGES/step1.png)



![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
