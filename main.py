""""
Main.py

Run temperator client sensors and servers

By: Eoin Lyng
    v0.1    14NOV23     

"""
import subprocess

# Create and start the processes - UDP Server to listen and 3 client temperature sensors with temperature readings
#https://bobbyhadz.com/blog/how-to-run-multiple-python-files

proc1 = subprocess.Popen(['python', 'udp_server.py'])
proc2 = subprocess.Popen(['python', 'udp_client1.py'])
proc3 = subprocess.Popen(['python', 'udp_client2.py'])
proc4 = subprocess.Popen(['python', 'udp_client3.py'])

# Wait for the processes to finish
proc1.wait()
proc2.wait()
proc3.wait()
proc4.wait()

