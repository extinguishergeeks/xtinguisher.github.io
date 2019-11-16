# Extinguisher Geeks <img src="https://www.hrlcomp.com/wp-content/uploads/2018/08/Fire-Extinguisher-Training-1350x675.jpg" width="100">[Home](homepage.md)     [About]() [Tutorial](week 4 - ESP32.md)
### setting up the ESP 32

The ESP 32 is a microcontroller which offers wifi capacability. This blog will show how to flash and set up micropython into the ESP 32.

First you need to download python 3. Remember to select add to PATH when installing python 3. You can find python at https://www.python.org . 

Next, download the file needed to flash micropython into ESP 32 at https://micropython.org/download#esp32

Next open up command prompt (CMD) and run as administor.

In the CMD, type 

    pip3 install esptool

After installation, then type this command

    esptool.py --port /dev/ttyUSB0 erase_flash

Remember to change the port setting to match the port you are using for the ESP 32

After, that, open the folder that has the firmware for the ESP 32. Run CMD on the folder and type in the following command

    esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin

Remember to change the port setting to match the port you are using for the ESP 32

Next, type in this command

    pip install rshell

After that, type

    rshell

This will open up the rshell command line interface in your CMD

Next,visit https://micropython.org/download#esp32 and download the correct firmware file for your board.

Before writting the firmware,we have to erase the flash memory of esp32, check your port number again. In this case i will use COM3

    esptool --chip esp32 --port COM3 erase_flash

After the firmware is being installed, the device will reboot and then we are ready start our first MicroPython program.
esptool --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000    

    esptool --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 esp32spiram-20190529-v1.11.bin


Next connect the MicroPython repl using rshell
    
    rshell -p COM3 repl


And then, your Esp32 is ready to use, enjoy with your MicroPython.
