# College Assignment 1 (CA1) #

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

- A batch file "create file structure.bat" was created to automatically build the structure as outlined in the CA1
- When run this batch file prompts the user to type a name for the project which then creates a directory with this name and then completes the build of the directory structure.
- It also downloads the python files ,created later for part 2, from a [Github repository](https://github.com/EoinLyng/IAS--ca1) created for this CA1 and additional files from other online sources.
- These files are placed in the correct directories in the project folder.


#### Part 2 methodology ### 
- A [Github repository](https://github.com/EoinLyng/IAS--ca1) was created  to store the completed python scripts for download to project by batch file.
- A server script was created to listen for temperature data from the client sensors  [udp_server.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_server.py)
- A client script was created to send temperature data for client sensor 1 [udp_client1.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client1.py)
- A client script was created send temperature data for client sensor 1 [udp_client2.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client2.py)
- A client script was created to send temperature data for client sensor 1 [udp_client3.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client3.py)
- A settings file was created (udp.py not included in Github repository for security reasons) to provide network data to the other scripts in the settings directory  and also containing the email details and passwords required later for email notifications.
- A main script was created to run other scripts simultaneously [main.py](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/main.py)
- A batch file file was created to begin simulating the temperature monitoring from the three sensors, to start the server monitoring process and to send email notifications in the event of temperatures below 5 degrees or above 30 degrees.[StartMonitoring.bat](https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/StartMonitoring.bat)

#### Creating Project from Batch file ### 
1. Please ensure the latest version of Python is installed [Python.org Downloads](https://www.python.org/downloads/)
2. In CA1.zip you will files 4 files , create file structure.bat, readme.md, udp.py and a zip file ,Projectfiles.zip, containing all other fies for CA. These files should download from a Github repository, however I have included them incase this download fails to show the working files.
3. Run batch file 'create file structure.bat'.
4. This creates the file structure and also downloads the relevant files from the [Github repository](https://github.com/EoinLyng/IAS--ca1) and copies udp.py to settings folder.
5. Change recipient email address in settings/udp.py from receipient@gmail.com to a valid email address for farmer to receive email notifications **making sure to save the file**.
6. Run 'StartMonitoring.bat' to run main.py and thereby run all other scripts.
7. SensorOne is set to simulate data randomly from a list containing numbers from -5 to 35 and also letters a,b,c,d to simulate errors in the readings.The other two sensors randomly select data from a range between -5 and 35.
8. Monitoring begins after running StarMonitoring.bat, the output of the 3 loggers is stored in the data directory in three - files Sensor_One_Output.log, Sensor_Two_Output.log, Sensor_Three_Output.log and error logs are stored in error.log in error directory.
9. When sensor temperature reading goes below 5 degrees celsius an email is sent to the farmers email address (formerly receipient@gmail.com).
10. When  sensor temperature reading goes above 30 degrees celsius an email is sent to the farmers email address (formerly receipient@gmail.com).
