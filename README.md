# blink-kboard
Control arduino or nodemcu boards on keyboard press. This thing is very simple. When we press our keyboard, we send data(number) to the serial port. In the Arduino, we wait for incoming data from serial, then we process it, maybe to turn on led or anything else.

## The Keyboard Listener
The listener listens keyboard press. The program located in  /kboard. It's written in python3. It sends '\1' on key press, and sends '\0' on key release. You can customize it if needed.

Get the requirements
```
$ pip3 install -r requirements.txt    # run it inside /kboard dir
```

Then run it
```
$ python3 kboard.py
```

## The Arduino
We use platform io in vscode to compile the source code of the arduino. If you have not use it before, consider to learn it [here](https://platformio.org/). It's easier to get libraries and there are so many fancy things compared with Legacy Arduino IDE. 

Thank you, give a try and customize it!
