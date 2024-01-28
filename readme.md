# ClockClock 24 replica

Video of clock in action: https://photos.google.com/share/AF1QipM3veQpQ0XkVU6mXYjfI77cDL8gVcDZlROT0_qATZYPRnyIRZsuLHRsqtRsNTrixQ?key=c0U2SFBVdGpubVNTWW43WENBeFczdWVBSk5FbmZB


A clock consiting of 24 X40 stepper motors. There are 6 pcb where 4 of the X40 steppers are on a pcb. On each PCB 2 X40 (so 4 steppers, since X40 are dual axle) are controlled by a VID6606 stepper controller, so 2 VID6606 per PCB. These 2 are controlled by 1 MapleMini STM32F103. These 6 modules are controlled by a single RasberryPi Pico running MicroPython, this Pico communicates with the modules over I2C and also a DS3231 RTC for timekeeping. Additionally, as an optional addon a network model (a Pico W) can be added to get ITP time (This was added after everthing was finished so I didnt want to change the main control board to a Pico W). The clock works reliably with the newest addition of chekcsums and hasnt crashed since. Setting the time and display modes is done via a button panel of 4 buttons.


## Things to improve:
- The bus should be switched to CAN something else more robust then I2C, which is used here. I2C now works flawlessly for me but perhaps in a higher noise environment or over years errors would occur.
- Add pull down resistor for enable pin of vid 6606, connect to MCU pin (had to be botched in)
- Change microcontroller to smth cheaper/newer (RP2040?)
- Maybe switch to TMC2209 or smth for more silent driving (Some preliminary tests showed they do work with these steppers and are a bit more quiet, but they are much more expensive)


## Additional notes: 

- There was a plan to automatically zero the steppers with a small magnet and hall sensor but this was not implemented, but the sensor mountings are present on the PCB
- I lubricated the X40 steppers with SuperLube which did definitely reduce noise but this went back to normal levels after a few months.
- The main body is made of Korian which I had made by a professional using the drawing in the 3d parts folder
- Pointers where printed on a consumer FDM printer (Ender3V2) and where sanded and are friction fit.



