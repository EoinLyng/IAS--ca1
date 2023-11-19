@echo off
cls
echo "**********************************************"
echo This batch file will create a project directory for Assignment 1
echo "**********************************************"
echo *** press [ctrl][c] to exit or any key to continue ***
pause 
set /p NAME=Enter the name (no spaces) of the project, then press [return]  
echo Creating %NAME%
mkdir %NAME%
cd %NAME%
mkdir Templates

@Echo Off
Set "out=.\Templates"
(
  Echo;# /usr/bin/env python3
  Echo;
  Echo;"""
  Echo;Project:
  Echo;File Name:  
  Echo;By:Eoin Lyng
  Echo;Initial %date%
  Echo;Version History
  Echo;
  Echo;v 0.1 Initial
  Echo; 
  Echo;"""  
) > "%out%\python_functions.py"
mkdir Documentation
:: Unit and integration tests for to project
mkdir Tests
mkdir Examples
mkdir Source
mkdir settings
mkdir data
mkdir error

:: Create main.py file in root directory

:: Download Raspberry Pi 0 Technical Data Sheet to documentation directory
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://datasheets.raspberrypi.com/rpizero2/raspberry-pi-zero-2-w-product-brief.pdf" -o ./Documentation/Raspberry_Pi_Zero_2_W.pdf
:: Download Sensor Technical Data Sheet to Documentation directory
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://www.mouser.com/datasheet/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf" -o ./Documentation/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://www.gnu.org/licenses/lgpl-3.0.txt" -o licence.txt
:: Download main.py file to root directory from Github
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/main.py" -o main.py
:: Download udp_server.py file to root directory from Github
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_server.py" -o udp_server.py
:: Download udp_client1.py file to root directory from Github
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client1.py" -o udp_client1.py
:: Download udp_client2.py file to root directory from Github
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client2.py" -o udp_client2.py
:: Download udp_client3.py file to root directory from Github
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/udp_client3.py" -o udp_client3.py
:: Download StartMonitoring.bat file to root directory from Github
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/StartMonitoring.bat" -o StartMonitoring.bat
:: Create readme.md file in root directory
curl -A "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64)" -L "https://raw.githubusercontent.com/EoinLyng/IAS--ca1/main/readme.md" -o readme.md

:: Copy udp.py file into settings directory - this file includes email app password and sender email address

xcopy ..\udp.py .\settings

::copy python_functions.py Templates
#del python_functions.py
cls
dir
echo "**********************************************"
echo Finished creating .project %NAME%
echo "**********************************************"
cd ..
