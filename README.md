# Collect Temperature Data

 TAMK has a high-end sensor system on the rooftop to capture all types of weather data like temperature, light, rain, humidity, etc. In IOT, python is a great choice for the backend side of development as well as the software development of devices. There are low system requirements especially for microPython than C++. This project will guide users on how the software processes temperature data from the ESP32 board to the API.


## Requirements

### Hardaware:
 - ESP32(Wemos Lolin32)
 - Breadboard
 - Some wires
 - Resistor 120 ohm and 220 ohm
 - Temperature sensor
 - an USB and ethernet cable
 - Raspberry pi

### Software :
- Thonny IDE for using micropython.
- Esptool for deploying micropython to our esp32 development board.
- Python3 ruining for Esptool.
- Advanced IP Scanner for checking raspberry pi IP address.
- VNC Viewer for Raspberry pi.
- Mosquitto running on raspberry.

## Usages

Use the files for,

- Esp32 board- ESP32/sendToRpi.py

- Raspberry pi- RasberryPi/recived_inRpi.py

- Demo- output

More detailed information can be found on the technical document- document/weather_station_temperature.pdf


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update is appropriate.

