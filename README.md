# RPI-BQ27441-Python-Set-Capacity-Energy-Term-Voltage
A python3 script for Raspberry Pi using I2C to set the design capacity, design energy and termination voltage of a BQ27441-G1 fuel gauge. Most of this code was from a person called Arthur Santos that posted it up on the TI Texas Instruments Forums. I've slightly modified the code so it works in setting all the values, some of the changes I made were from looking a C code developed by "Chintan", however I've never been able to get his code to actually update these parameters (it looks like it does write all the data... but for some reason it doesn't). Hopefully this will be of assistance to others as there's actually very little Python/Python3 code out there for using these BQ27441-G1 controllers with Raspberry Pi's!

This is a Python3 i2c script for the BQ27441-G1 fuel gauge by Texas Instruments

I've been searching everywhere on the internet for python scripts and C code to set the following parameters:

* Design Capacity (in maH)
* Design Energy (capacity in maH x 3.7)
* Termination Voltage (typically 3200 mv)

These are the following links that i've found for various C and Python Code - some of it on GitHub but still doesn't seem to work on RPI's and C/Python:

Chintanp (excellent code for reading BQ27441 data, just writing to i2c doesn't seem to work/commit on RPI)
https://github.com/chintanp/i2c-charger/tree/master/BQ-27441-Gauge

Arthur Santos (excellent start with the Python code, no update on TI's thread on this)
https://e2e.ti.com/support/power-management/f/196/t/658708

The code by Arthur is pretty much what I've got posted here, along with the suggested changes to checksum calculations

From Chintanp's code, I was able to get the addresses for writing design energey and termination voltage.

I have also modifed Chintanp's code which will read all the data without doing the whole config part. Chintanp's code for reading all the BQ274411 data works perfectly, but as I mentioned, I simply cant get his code to write he design capacity, energy or terminate voltage. It might be something I'm doing wrong, but on a raspberry Pi, it just doesn't work.

If anyone can help contribute to this, it would be greatly appreciated... there's many people out there that have worked on code for these controllers, so please dont take me wrong when I've had problems with other peoples code. But having some success with getting things set via Python3 on the RPI, I decided to help share my experiences and code that I've modified. Hopefully it helps and hopefully we can all get setting BQ27441 parameters sorted once and for all for Raspberry Pi's!!!
