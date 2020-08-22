## hue_shortcuts
A couple of scripts to control Philips Hue lights

They are super simple, and are meant for people who want to be able to control their Philips Hue lights by desktop shortcuts, without having extra programs running in the background. Right now it controls all of the lights connected to your Bridge.

If lights are off, HueUp.py turns on all lights (50% brightness). If lights are already on, it increases brightness in 20% intervals (adjustable).

If lights are on, HueDown.py decreases brightness in the same intervals, until they turn off.  

You can adjust the increments (in percentage) in the second line of HueConf.txt. Default is 20.

Note: This controls **all** of the lights connected to the Bridge.

## How to use
1. Edit the first line in HueConf.txt so it matches the IP of your Bridge.
2. Press the button on your Bridge before you run either of the scripts the first time (only has to be done once in total)
3. Run programs

If you create a desktop shortcut for the executables, remember to adjust the "Start in:" field, so it matches the location of HueConf.txt. 

If you want to create a keyboard shortcut, you can do so by right-clicking on your new shortcut, going to properties and editing the "Shortcut key". Or use AutoHotKey, I guess. 

## Plans, maybe?
- Have it automatically find the IP of the Bridge

Made with the Phue library by studioimaginaire: https://github.com/studioimaginaire/phue
