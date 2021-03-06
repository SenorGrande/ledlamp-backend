sudo apt install python3-pip

I found I didn't need circuitpython, but here is the link for posterity:  
`https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi`  

Install neopixel library:  
`sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel`  
`sudo python3 -m pip install --force-reinstall adafruit-blinka`

Run the script (as root):  
`sudo python3 test.py`  


