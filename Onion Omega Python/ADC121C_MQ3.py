# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADC121C_MQ3
# This code is designed to work with the ADC121C_I2CGAS_MQ3 I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Gas?sku=ADC121C_I2CGAS_MQ3#tabs-0-product_tabset-2

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# ADC121C_MQ3 address, 0x50(80)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
data = i2c.readBytes(0x50, 0x00, 2)

# Convert the data to 12-bits
raw_adc = (data[0] & 0x0F) * 256 + data[1]
concentration = (9.95 / 4096.0) * raw_adc + 0.05

# Output data to screen
print "Alcohol Concentration : %.2f mg/l" %concentration
