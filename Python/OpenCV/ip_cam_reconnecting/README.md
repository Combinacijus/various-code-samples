# OpenCV IP Camera

## Features
- Self-contained class and example use of it.
- Automatically reconnects to the IP camera if video is lost.
- Forceful reconnection: *cam_force_address* must be specified (disconnects other clients). It's ensures that video won't be hijack by other clients.

## Tested
Tested on Ubuntu 18.04 with android as IP camera using DroidCam app.

## How to
### General setup
- Copy the code.
- Change IP adresses *CAM_ADDRESS* and *CAM_FORCE_ADDRESS (OPTIONAL)* to your IP camera addresses.
- (OPTIONAL) Find "NOTE:" comments in the code and modify lines if needed
- Run.

### Using Android phone as IP camera with DroidCam
- Download [DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam&hl=en "DroidCam") app.
- Refer to[ this link](https://www.dev47apps.com/droidcam/connect/ " this link") to setup your android as IP camera.
- Find DroidCam IP address eg.  *192.168.8.102:4747/video* (note *"/video"* part)
Try to open that address in your browser and if you see video feed you can put in the code.
- To find *cam_force_address* is a bit trickier. I found it by connecting to *192.168.8.102:4747* on two tabs. The second tab did not show video but gave option to "*Disconnect the other client and Take Over*" by inspecting where it redirected I found the address.

This should work with any IP camera but IP addresses will be different.