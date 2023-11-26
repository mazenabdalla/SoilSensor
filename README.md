# SoilSensor
Python code to get the JXBS-J001-TR-RS 7-in-1 soil nutrient sensor readings.

Using the <a href="https://drive.google.com/file/d/1XYFCNVUlTv7XLex2lMuBQVzdD8rD1Mu2/view?usp=sharing">product datasheet</a> for reference, this Python program was written to quickly interface with the sensor.

We used the USB-RS485 adapter from peacefair to connect the PC to the sensor.

## Prerequisites
This program uses the pyserial and pymodbus libraries. They can be installed using:

```
$ pip install -r requirements.txt
```

## Running the program
Simply run the script using Python >= 3.10. The program loops infinitely, and can be exited using CTRL+C.

```
$ python SoilSensor.py
```
