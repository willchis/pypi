# pypi
Collection of Python based Raspberry Pi scripts

## Pi Setup

Run pi config:  
`sudo raspi-config`  
Choose “5 Interfacing Options” then “P5 I2C” then “Yes” and then “Finish” in this order and restart your RPi.  
The I2C module will then be started.

Type a command to check whether the I2C module is started:  
`lsmod | grep i2c`  
If the I2C module has been started you'll see some info relating to the CPU model etc.  
Different models of Raspberry Pi display different contents depending on the CPU installed.

Install I2C-Tools:  
`sudo apt-get install i2c-tools`
I2C device address detection:  
`i2cdetect -y 1`

Install Smbus Module:  
`sudo apt-get install python3-smbus`

Get a weather API key from https://openweathermap.org/api

Get a stock price API key from https://finnhub.io/

