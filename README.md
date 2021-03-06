# RPi_RangeFinder
Raspberry Pi range finder script, designed to find ranges of stuff.

### Raspberry Pi
This is my first foray into coding to specifically control hardware. I am using the circuit designed by Python Programming in their [Input from a Sensor via GPIO](https://pythonprogramming.net/gpio-input-raspberry-pi-tutorials/) guide.

I have made a few modifications to their code and circuitry by adding LED output based on the distance of the object from the sensor

### Goal:
To eventually replace the LED output with power to a DC motor, which will be attached to a 3D printed chassis and drivetrain and will ultimately follow a previously identified person at a specific distance. Not sure yet how I will control the device...Perhaps by web app from a server which is ran off of another RPi.

---

### Version History
Version history in the form of major milestones:
* **v0** - 10/1/2020 - Sensor attached to an external breadboard. Code controls sensor & LEDs via GPIO. Takes inputs from sensor & calculates distance. Outputs result to console
  * **v0.1** - 10/2/2020 - Reworked the distance call into a function to make it persistent. Instead of outputting a blinking or steady light, I added another light from a different GPIO pin. Simulating power to the motor versus power to somewhere else based on distance measured.
  * **v0.2** - 10/6/2020 - Added scripts to that utilize an RPi camera to detect faces (will replace with obj later), define bounds in a still (will convert to bounds in a vid), and to stream an RPi video live. Separately, these files do not mean anything. The knowledge gained, however, will be part of the final product.
