# Turret
 This program uses face detection to move a pair of servos to point at a face.
 I'll add more code to activate some harmful thing later...Maybe.
 

## To code for the Arduino in Python:  
 1) Download the Arduino IDE (if you don't already have it) and open it.
 2) Click on File > Examples > Firmata > StandardFirmata
 
  ![image](https://user-images.githubusercontent.com/67160289/169120878-b4f5e704-73fc-4431-b070-2679d942f5c7.png)
 
 3) Once you have the example file open, upload to an arduino board using the arrow at the top left.
 4) Go into your powershell and enter 'pip install pyfirmata'
 5) 'import pyfirmata' into your file and that's it.

 Any code written and executed in your file will automatically be uploaded to the Arduino.

 Here's a link to the pyfirmata docs: https://pyfirmata.readthedocs.io/en/latest/
 
 ## Installing OpenCV:
  1) Enter 'pip install opencv-contrib-python' into powershell
  2) When importing this package, you only need 'import cv2'
