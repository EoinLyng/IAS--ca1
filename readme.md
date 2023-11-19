### College Assignment 1 ###

# Project Overview #

## Part 1 ##

1. Write a batch file/script in Linux or DOS (your choice!) to automate creating this structure.
2. Create a readme.md file which explains the project.
3. Build a main.py programme in the project root.
4. Complete the log analysis project described on the following page.

## Part 2 ##

*A farmer needs help!*

In several outbuildings, he needs to monitor temperature in several different locations. He has been
quoted an astronomical price for a professional system. He has asked me to help.
I can add Raspberry Pi Zero-W (RPi) for a few Euros each. I can put 1-wire sensors on them for less
than a Euro each. Job done!

*I need a hand.*

I need you to write me a simulator to demonstrate this. Write three UDP clients which will unicast a
single temperature to a server, with a time stamp and a sensor ID.

Write a server to receive this data and save it in separate logfiles.

*Extra*

It would be a real bonus if we can alert the farmer when temperature is <5c or >30c.

#### Part 1 methodology ### 

- I created a batch file "create file structure.bat" to automatically build the structure as outlined in the CA
- When run this batch file prompts the user to type a name for the project which then creates a folder with this name containing the necessary files.
- It also downloads the python files created later for part 2 from a [Github repository](https://github.com/EoinLyng/IAS--ca1) created for this CA.
- These files are placed in the correct directories in the project folder.


#### Part 2 methodology ### 

- I created a [Github repository](https://github.com/EoinLyng/IAS--ca1)  to store the completed python scripts for download to project by batch file.
- Created a server script to listen for temperature data from the client sensors  [udp_server.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_server.py)
- Created a client script to send temperature data for client sensor 1 [udp_client1.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client1.py)

- Created a client script to send temperature data for client sensor 1 [udp_client2.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client2.py)
- Created a client script to send temperature data for client sensor 1 [udp_client3.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client3.py)
- Created a udp script to send network data to the other scripts in the settings directory [udp.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp.py)
- Created a main script to run other scripts simultaneously [main.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/main.py)
- Created a batch file to run main.py when batch file is executed [StartMonitoring.bat](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/StartMonitoring.bat)

#### Creating Project from Batch file ### 
1. Run batch file 'create file structure.bat'.
2. This creates the file structure and also downloads the relevant files from the [Github repository](https://github.com/EoinLyng/IAS--ca1) 
3. Change recipient email address receiver@gmail.com in udp_server.py to a valid email address for farmer making sure to save the file.
4. Run 'StartMonitoring.bat' to run main.py and thereby run all other scripts.
5. Monitoring now begins, the output of the 3 loggers is stored in the data directory in 3 files Sensor_One_Output.txt, Sensor_Two_Output.txt, Sensor_Three_Output.txt.
6. When reading goes below 5 degrees celsius an email is sent to the farmers email address (formerly receiver@gmail.com)
7. When reading goes above 30 degrees celsius an email is sent to the farmers email address (formerly receiver@gmail.com)
