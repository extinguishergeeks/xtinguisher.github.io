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

