'''
peptech GmbH
Authored By:
Qais Sunna
Qais.Sunna@peptech.de
'''

from hwControl import chooseSensor, openSPI, closeSPI, readADC101 as value
from time import sleep

tempArray = []  #Temporary variable for storing data

def main():
    openSPI()   #Open SPI Interface for communication with ADC
    printSensorValues() #Loop Function for printing out the data

def readSensorArray():  #Function with a return value of an array with the 8 sensor values
    tempArray.clear()
    try:
        for channel in range (8):
            chooseSensor(channel)
            tempArray.append (round((value()*5/1023),5))
        return tempArray
    except Exception as e:
        print("\nException Occured:",e)
        closeSPI()
        exit()

def printSensorValues():    #Visualizing the senosr values
    while True:
        try:
            values = readSensorArray()
            print ("#######################")
            for sensorNo in range (8):
                print (f"Sensor {sensorNo+1}: {values[sensorNo]} Volts")    #sensor+1 for matching the number on the shield
            print ("#######################\n")
            sleep (5e-1)
        except Exception as e:
            print("\nException Occured:",e)
            closeSPI()
            exit()

if __name__ == "__main__":
    main()