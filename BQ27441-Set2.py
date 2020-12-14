import smbus
import time
import struct

bus=smbus.SMBus(1)

address = 0x55

e=bus.read_i2c_block_data(address,0x0a,2)
(full_cap,)=struct.unpack('H', bytearray(e)[0:2])
print("Full Available Capacity is",full_cap, 'mA')


#Trying to write the nominal capacity
bus.write_byte_data(address,0x00,0x00)
bus.write_byte_data(address,0x01,0x80)
bus.write_byte_data(address,0x00,0x00)
bus.write_byte_data(address,0x01,0x80)

bus.write_byte_data(address,0x00,0x13)
bus.write_byte_data(address,0x01,0x00)

bus.write_byte_data(address,0x61,0x00)
bus.write_byte_data(address,0x3e,0x52)

bus.write_byte_data(address,0x3f,0x00)

block=bus.read_i2c_block_data(address,0x40,32)
block=list(struct.unpack('32B',bytearray(block)[0:32]))
block[0x0a] = 0x05 # 05dc = 1500mah (first is 0x05)
block[0x0b] = 0xdc # 05dc = 1500mah (second is 0xdc)
#new_checksum = 0

new_checksum = 255 - ~sum(block) + 0xff
#new_checksum = ~sum(block) - 0xff

bus.write_byte_data(address,0x4a,0x05) #writing new capacity (0x05+0xdc=1500)
bus.write_byte_data(address,0x4b,0xdc) #writing new capacity (0x05+0xdc=1500)

time.sleep(1)

bus.write_byte_data(address,0x4c,0x15) #writing design energy (1500x3.7)
bus.write_byte_data(address,0x4d,0xae) #writing design energy (1500x3.7)
# 0x15+0xae = 5500 mwh (1500x3.7)

time.sleep(1)

bus.write_byte_data(address,0x50,0x0b) #writing termination voltage (3000)
bus.write_byte_data(address,0x51,0xb8) #writing termination voltage (3000)
# 0x0b+0xb8 = 3000 mv
# 0x0c+0x80 = 3200 mv

time.sleep(1)

x = bus.read_i2c_block_data(address,0x40,32)
csum = 0
for i in range(32):
  csum = csum + x[i]
  csum = csum & 0xff
#csum = 255 - csum
csum = 0xff - csum 

bus.write_byte_data(address,0x60,csum) #trying to write on BlockDataCheck

time.sleep(1)
bus.write_byte_data(address,0x00,0x42)
bus.write_byte_data(address,0x01,0x00)

bus.write_byte_data(address,0x00,0x20)
bus.write_byte_data(address,0x01,0x00)



print('Design Capacity:')
f=bus.read_i2c_block_data(address,0x3c,2) #address for design capacity
(des_cap,)=struct.unpack('H', bytearray(f)[0:2])
print(des_cap, 'maH')

print('Design Energy:')
f=bus.read_i2c_block_data(address,0x4c,3) #address for design energy
#(des_en,)=struct.unpack('H', bytearray(f)[0:2])
des_energy = f[0]*16*16 + f[1]
print(des_energy, 'mwH')

print('Terminate Voltage')
f=bus.read_i2c_block_data(address,0x50,3) #address for design energy
term_voltage = f[0]*16*16 + f[1]
print(term_voltage, 'mv')


