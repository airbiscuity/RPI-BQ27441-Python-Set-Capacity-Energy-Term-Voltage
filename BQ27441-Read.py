#Version 1.0 Script to Read ALL BQ27441 Vaules and Data

import smbus
import time
import struct

bus=smbus.SMBus(1)

address = 0x55



e=bus.read_i2c_block_data(address,0x02,2)
(temperature,)=struct.unpack('H', bytearray(e)[0:2])
print("Temparature [Battery]:",format((temperature/10-273.0),'.1f'), 'Celcius')

e=bus.read_i2c_block_data(address,0x1e,2)
(tempint,)=struct.unpack('H', bytearray(e)[0:2])
print("Temparature [Internl]:",format((tempint/10-273.0),'.1f'), 'Celcius')


e=bus.read_i2c_block_data(address,0x04,2)
(volts,)=struct.unpack('H', bytearray(e)[0:2])
print("Voltage:",volts, 'mV')

e=bus.read_i2c_block_data(address,0x06,2)
(flags,)=struct.unpack('H', bytearray(e)[0:2])
print("BQ27441 Flags:",flags)

e=bus.read_i2c_block_data(address,0x08,2)
(nomavailcap,)=struct.unpack('H', bytearray(e)[0:2])
print("Nominal Available Capacity:",nomavailcap, 'mAh')

e=bus.read_i2c_block_data(address,0x0a,2)
(full_cap,)=struct.unpack('H', bytearray(e)[0:2])
print("Full Available Capacity:",full_cap, 'mAh')

e=bus.read_i2c_block_data(address,0x0c,2)
(rem_cap,)=struct.unpack('H', bytearray(e)[0:2])
print("Remaining Capacity:",rem_cap, 'mAh')

e=bus.read_i2c_block_data(address,0x0e,2)
(fcc,)=struct.unpack('H', bytearray(e)[0:2])
print("Full Charge Capacity:",fcc, 'mAh')

e=bus.read_i2c_block_data(address,0x10,2)
(avg_curr,)=struct.unpack('H', bytearray(e)[0:2])
if avg_curr >= 32267:
  avg_curr = avg_curr - 65536
print("Current [Average]:",avg_curr, 'mA')

e=bus.read_i2c_block_data(address,0x12,2)
(sby_curr,)=struct.unpack('H', bytearray(e)[0:2])
if sby_curr >= 32267:
  sby_curr = sby_curr - 65536
print("Current [Standby]:",sby_curr, 'mA')

e=bus.read_i2c_block_data(address,0x14,2)
(max_curr,)=struct.unpack('H', bytearray(e)[0:2])
if max_curr >= 32267:
  max_curr = max_curr - 65536
print("Current [MaxLoad]:",max_curr, 'mA')

e=bus.read_i2c_block_data(address,0x18,2)
(avg_pow,)=struct.unpack('H', bytearray(e)[0:2])
if avg_pow >= 32267:
  avg_pow = avg_pow - 65536
print("Average Power:",avg_pow, 'mW')

#USE THIS For State of Charge
e=bus.read_i2c_block_data(address,0x1c,2)
(soc,)=struct.unpack('H', bytearray(e)[0:2])
print("State of Charge    [NormalSOCF]:",soc, '%')

e=bus.read_i2c_block_data(address,0x30,2)
(socu,)=struct.unpack('H', bytearray(e)[0:2])
print("State of Charge    [Unfiltered]:",socu, '%')

e=bus.read_i2c_block_data(address,0x20,1)
print("State of Health    [BattHealth]:",e[0], '%')


e=bus.read_i2c_block_data(address,0x28,2)
(rcu,)=struct.unpack('H', bytearray(e)[0:2])
print("Remaining Capacity [Unfiltered]:",rcu, 'mAh')


#USE THIS For Remaining Capacity
e=bus.read_i2c_block_data(address,0x2a,2)
(rcf,)=struct.unpack('H', bytearray(e)[0:2])
print("Remaining Capacity [Filtered  ]:",rcf, 'mAh')

e=bus.read_i2c_block_data(address,0x2c,2)
(fccu,)=struct.unpack('H', bytearray(e)[0:2])
print("Full Charge Cap    [Unfiltered]:",fccu, 'mAh')

#USE THIS For Full Charge Capacity
e=bus.read_i2c_block_data(address,0x2e,2)
(fccf,)=struct.unpack('H', bytearray(e)[0:2])
print("Full Charge Cap    [Filtered  ]:",fccf, 'mAh')




e=bus.read_i2c_block_data(address,0x3c,2) #address for design capacity
(des_cap,)=struct.unpack('H', bytearray(e)[0:2])
print("Design Capacity:",des_cap, 'maH')

e=bus.read_i2c_block_data(address,0x4c,3) #address for design energy
#(des_en,)=struct.unpack('H', bytearray(e)[0:2])
des_energy = e[0]*16*16 + e[1]
print("Design Energy:",des_energy, 'mwH')

e=bus.read_i2c_block_data(address,0x50,3) #address for design energy
term_voltage = e[0]*16*16 + e[1]
print("Terminate Voltage:",term_voltage, 'mv')