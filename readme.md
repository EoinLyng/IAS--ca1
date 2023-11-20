# College Assignment 1 #

## Project Overview ##

### Part 1 ###

1. Write a batch file/script in Linux or DOS (your choice!) to automate creating this structure.
2. Create a readme.md file which explains the project.
3. Build a main.py programme in the project root.
4. Complete the log analysis project described on the following page.

### Part 2 ###

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

- A batch file "create file structure.bat" was created to automatically build the structure as outlined in the CA
- When run this batch file prompts the user to type a name for the project which then creates a folder with this name creating the folder structure.
- It also downloads the python files created later for part 2 from a [Github repository](https://github.com/EoinLyng/IAS--ca1) created for this CAm and other online sources.
- These files are placed in the correct directories in the project folder.


#### Part 2 methodology ### 

- A [Github repository](https://github.com/EoinLyng/IAS--ca1) was created  to store the completed python scripts for download to project by batch file.
- Created a server script to listen for temperature data from the client sensors  [udp_server.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_server.py)
- Created a client script to send temperature data for client sensor 1 [udp_client1.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client1.py)

- Created a client script to send temperature data for client sensor 1 [udp_client2.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client2.py)
- Created a client script to send temperature data for client sensor 1 [udp_client3.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client3.py)
- Created a udp (udp.py not included in Github repository for security reasons) script to send network data to the other scripts in the settings directory  and also containing the email details and passwords required later for email notifications.
- Created a main script to run other scripts simultaneously [main.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/main.py)
- Created a batch file to begin simulating the temperature monitoring from the three sensors[StartMonitoring.bat](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/StartMonitoring.bat)

#### Creating Project from Batch file ### 
1. Run batch file 'create file structure.bat'.
2. This creates the file structure and also downloads the relevant files from the [Github repository](https://github.com/EoinLyng/IAS--ca1) and copies udp.py to settings folder.
3. Change recipient email address in settings/udp.py from receiver@gmail.com to a valid email address for farmer **making sure to save the file**.
4. Run 'StartMonitoring.bat' to run main.py and thereby run all other scripts.
5. SensorOne is set to simulate data randomly from a list containg numbers from -5 to 35 and also letters a,b,c,d to simulate errors in the readings.The other two sensors randomly select data from a range between -5 and 35.
5. Monitoring begins after running StarMonitoring.bat, the output of the 3 loggers is stored in the data directory in three - files Sensor_One_Output.log, Sensor_Two_Output.log, Sensor_Three_Output.log and error logs are stored in error.log in error directory.
6. When sensor temperature reading goes below 5 degrees celsius an email is sent to the farmers email address (formerly receiver@gmail.com).
7. When  sensor temperature reading goes above 30 degrees celsius an email is sent to the farmers email address (formerly receiver@gmail.com).
