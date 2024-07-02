## FlaskRGB-controller

# set up.

1. 
connect the lights to the pi wired like this https://cdn-learn.adafruit.com/assets/assets/000/063/928/medium640/led_strips_raspi_NeoPixel_powered_bb.jpg?1539980907

2. as root run these two commands

`
    sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
    sudo python3 -m pip install --force-reinstall adafruit-blinka
`

3. 
`git clone https://github.com/MichaelMediaGroup/FlaskRGB-controller `
`cd  FlaskRGB-controller `

4. 
`sudo python setup.py install`

5.
`sudo shutdown -r`

then just connect to your raspberry pi using a web browser using the pis Port.
