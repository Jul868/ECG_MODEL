import asyncio
from bleak import BleakClient

# Replace with your Nordic device's address
DEVICE_ADDRESS = "AA:BB:CC:DD:EE:FF"
# Replace with the service UUID you want to interact with
SERVICE_UUID = "0000180d-0000-1000-8000-00805f9b34fb"
# Replace with the characteristic UUID you want to read from
CHARACTERISTIC_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

received_data = []  # List to store received data

def save_data_to_file(data):
    with open("received_data.txt", "a") as file:
        file.write(data.hex() + "\n")

async def run():
    async with BleakClient(DEVICE_ADDRESS) as client:
        services = await client.get_services()
        print("Connected to device. Services:")
        for service in services:
            print(service)
        
        def notification_handler(sender, data):
            received_data.append(data)
            print(f"Received data: {data}")
            save_data_to_file(data)  # Save the data to a file

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("Stopping notification and closing connection.")
            await client.stop_notify(CHARACTERISTIC_UUID)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

# Print all received data after disconnecting
print("All received data:", [data.hex() for data in received_data])
