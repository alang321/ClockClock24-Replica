Disclaimer: I dont really know what im doing especially with PCB design

A clock consiting of 24 X40 stepper motors. There are 6 pcb where 4 of the X40 steppers are on a pcb. On each PCB 2 X40 (so 4 steppers, since X40 are dual axle) are controlled by a VID6606 stepper controller, so 2 VID6606 per PCB. These 2 are controlled by 1 MapleMini STM32F103. These 6 modules are controlled by a single RasberryPi Pico running MicroPython, this Pico communicates with the modules over I2C and also a DS3231 RTC for timekeeping. Setting the time and display modes is done via a button panel of 4 buttons. The PiPico uses asynchronous programming.



Additional notes: 
- The bus should be switched to CAN something else more robust then I2C, occasionally the clock stops working because I2C has no error correction and is not made for how it is used here. But Im currently too lazy to do it.
- there was a plan to automatically zero the steppers with a small magnet and hall sensor but this was not implemented, but the sensor mountings are present on the PCB
- I lubricated the X40 steppers with SuperLube which did definitely reduce noise.
- The main body is made of Korian which i had made by a professional using the drawing in the 3d parts folder


Video of clock in action: https://photos.google.com/share/AF1QipM3veQpQ0XkVU6mXYjfI77cDL8gVcDZlROT0_qATZYPRnyIRZsuLHRsqtRsNTrixQ?key=c0U2SFBVdGpubVNTWW43WENBeFczdWVBSk5FbmZB

