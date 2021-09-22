# module to use CMD
import os
 
# function to create XML profile (needed) - this contains key elements such as password
def createNewConnection(name, SSID, password):

    # optional: """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
    # optional: if you are using WPA instead of WPA2, change it in <authentication/>

    config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+name+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
    </WLANProfile>"""

    # CMD code to add the profile
    command = "netsh wlan add profile filename=\""+name+".xml\""+" interface=Wi-Fi"

    #creating the .xml profile
    with open(name+".xml", 'w') as file:
        file.write(config)

    # executing the command in CMD    
    os.system(command)
 
# function to connect to the specified Wi-Fi
def connect(name, SSID):
    command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    os.system(command)

# variables used
# optional:
# SSID = input("Type in SSID:\n")
# name = input("Type in name:\n")
# password = input("Type in password:\n")

# i've set the name to be equal to SSID
SSID = "Some random SSID"
name = SSID
password = "Th1sisN0taP4s5w0rd/*"

# establish new connection
createNewConnection(name, SSID, password)
 
# connect to the wifi network
connect(name, SSID)
print("If you aren't connected to this network, check the .xml file to confirm that all credentials are correct.")

# useful CMD commands:
# netsh wlan show profiles
# netsh wlan show profile (name of the profile) key=clear

# useful info:
# CMD uses some characters that need to be spaced out, e.g. & => &amp;

# errors
# „The network specified by profile "Some random SSID" is not available to connect."
    #   You have to be in the range of the SSID.
# „If you aren't connected to this network, check the .xml file to confirm that all credentials are correct."
    #   In most of the cases, password may be incorrect.