from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from pymodbus.constants import Defaults
from pymodbus.mei_message import ReadDeviceInformationRequest
Defaults.RetryOnEmpty = True
Defaults.Timeout = 5
Defaults.Retries = 5

client = ModbusClient(method = 'rtu', 
                        port = 'com3', 
                        timeout = 10, 
                        stopbits = 1, 
                        bytesize = 8, 
                        parity = 'N', 
                        baudrate = 115200)
client.connect()

ir = client.read_input_registers(address=0,count=3,unit=1)
print(ir.registers[0])
print(ir.registers[1])

client.close()


