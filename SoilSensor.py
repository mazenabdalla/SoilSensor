from pymodbus.client import ModbusSerialClient
import time

# Define COM port and baud rate
port = 'COM4'  # Change this to your COM port
baudrate = 9600

# Modbus address dictionary
sensorRegs = {
    'ph': (0x06, 1, 0.01, ''),
    'moisture': (0x12, 1, 0.1, ' %'),
    'temperature': (0x13, 1, 0.1, ' °C'),
    'conductivity': (0x15, 1, 1, ' µS/cm'),
    'nitrogen': (0x1e, 1, 1, ' mg/kg'),
    'phosphorus': (0x1f, 1, 1, ' mg/kg'),
    'potassium': (0x20, 1, 1, ' mg/kg'),
    'sensor_address': (0x100, 1, 1, ' dec'),
    'sensor_baud': (0x101, 1, 1, ' setting')
}

def read_register(client, address, regLen):
    try:
        if client.connect():
            response = client.read_holding_registers(address = address, count = regLen, slave = 1)
            if response.isError():
                print(f"Modbus Error: {response}")
            else:
                return response.registers[0]
        else:
            print(f"Failed to connect to {port} at {baudrate} baudrate")
    except Exception as e:
        print("Exception:", str(e))
    finally:
        client.close()

def read_sensor_registers():
    client = ModbusSerialClient(method='rtu', port=port, baudrate=baudrate)
    for sensor, (address, regLen, coefficient, suffix) in sensorRegs.items():
        value = read_register(client, address, regLen)
        if value is not None:
            rounded_value = round(value * coefficient, 1)  # Round to one decimal place
            print(f"{sensor}: {rounded_value} {suffix}")
        else:
            print(f"Failed to read {sensor} register")

# Read sensor registers
def main():
    while True:
        print("Reading sensor values...")
        read_sensor_registers()
        print("")
        time.sleep(5)

if __name__ == "__main__":
    main()