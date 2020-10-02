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
