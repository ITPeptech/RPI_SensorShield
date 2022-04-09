'''
peptech GmbH
Authored By: 
Qais Sunna
Qais.Sunna@peptech.de

This script does the following:
1- Update the system and install the required packages and dependencies.
2- Enables the SPI Interface. 
'''

from os import system, getcwd, geteuid

currentDir = getcwd()
configPath = "/boot/config.txt"

def checkPrivileges():
    if geteuid()!=0:
        print ("Permission Denied: Run Script as Root!")
        exit()
    else:
        return True

checkPrivileges()

def updateSystem():
    print ("\n \033[34m +++ Updating system +++\033[39m")
    print ("\033[93m Make sure you are connected to the internet\033[39m")
    system("sudo apt-get update -y")
    system("sudo apt-get upgrade -y")
    system("sudo apt-get dist-upgrade -y")
    system("sudo apt-get autoremove -y")
    system("pip3 install -r "+currentDir+"/requirements.txt")

updateSystem()

def interfaces():
    #Interfaces Initialization
    print ("\n \033[34m +++ Initializing SPI Interface +++\033[39m")
    with open(configPath) as f:
        if 'peptech' in f.read():
            print("SPI Interface is already initialized!")
            ans = input ("Revert changes? [Y/N]: ")
            if ans.capitalize()=="N":
                print ("No changes were made.\nTerminating...")
            elif ans.capitalize()=="Y":
                system("cp /boot/config.bkp /boot/config.txt") #Restore Backup
                print ("\033[32m All Changes Have Been Reverted !\033[39m")
            else:
                print ("\033[31m Wrong input. Terminating...\033[39m")
        else:
            print("Creating Backup ...")
            system("cp /boot/config.txt /boot/config.bkp") #Create Backup
            file_object = open(configPath,'a')
            file_object.write('\n\n[peptech]') #Enable SPI
            file_object.write('\ndtparam=spi=on') #Enable SPI
            file_object.close()
            print("\033[32m SPI is now initialized at boot!\033[39m")

interfaces()
    
print("\n \033[93m REBOOT RPI FOR CHANGES TO TAKE EFFECT\033[39m")
ans = input ("Reboot Now ? [Y/N]: ")
if ans.capitalize() == "Y":
    system("sudo reboot")
elif ans.capitalize() == "N":
    print ("Changes would take effect at next reboot.")
