from flask import Flask, render_template, request, redirect, url_for
import time
import time
import board
import neopixel

app = Flask(__name__)

num_pixels = 100
pixel_pin = board.D18
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def setlight(colourin):
    pixels.fill((0,0,0))
    pixels.show()
    pixels.fill(colourin)
    pixels.show()


app = Flask(__name__)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        colour = request.form['colour_in']
        setlight(hex_to_rgb(colour))
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')